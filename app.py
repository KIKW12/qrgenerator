from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import qrcode
import os
import io
import base64
from PIL import Image
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-this')

# Create uploads directory if it doesn't exist
UPLOAD_FOLDER = 'static/qr_codes'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def create_qr_code(url, filename=None, size=10, border=4):
    """
    Create a QR code that redirects to the specified URL
    
    Args:
        url (str): The URL to redirect to
        filename (str): The filename to save the QR code as
        size (int): The size of each box in the QR code
        border (int): The border size around the QR code
    
    Returns:
        str: The file path of the generated QR code
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Generate filename if not provided
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        domain = url.replace('https://', '').replace('http://', '').split('/')[0]
        filename = f"qr_{domain.replace('.', '_')}_{timestamp}.png"
    
    # Save the image
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    img.save(file_path)
    
    return file_path

def create_qr_code_base64(url, size=10, border=4):
    """
    Create a QR code and return it as base64 string for immediate display
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to base64
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    img_base64 = base64.b64encode(img_io.getvalue()).decode()
    
    return img_base64

@app.route('/')
def index():
    """Home page with QR code generator form"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    """Generate QR code from form submission"""
    url = request.form.get('url', '').strip()
    size = int(request.form.get('size', 10))
    border = int(request.form.get('border', 4))
    
    if not url:
        flash('Please enter a valid URL!', 'error')
        return redirect(url_for('index'))
    
    # Add protocol if not present
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        # Create QR code file
        file_path = create_qr_code(url, size=size, border=border)
        
        # Create base64 version for immediate display
        img_base64 = create_qr_code_base64(url, size=size, border=border)
        
        # Get filename for download link
        filename = os.path.basename(file_path)
        
        flash('QR code generated successfully!', 'success')
        
        return render_template('result.html', 
                             url=url, 
                             qr_image=img_base64,
                             download_filename=filename)
        
    except Exception as e:
        flash(f'Error generating QR code: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    """Download generated QR code file"""
    try:
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            flash('File not found!', 'error')
            return redirect(url_for('index'))
    except Exception as e:
        flash(f'Error downloading file: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/gallery')
def gallery():
    """Show gallery of generated QR codes"""
    try:
        qr_files = []
        if os.path.exists(UPLOAD_FOLDER):
            files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.png')]
            files.sort(key=lambda x: os.path.getctime(os.path.join(UPLOAD_FOLDER, x)), reverse=True)
            
            for file in files[:20]:  # Show last 20 files
                file_path = os.path.join(UPLOAD_FOLDER, file)
                creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                qr_files.append({
                    'filename': file,
                    'creation_time': creation_time.strftime('%Y-%m-%d %H:%M:%S')
                })
        
        return render_template('gallery.html', qr_files=qr_files)
    except Exception as e:
        flash(f'Error loading gallery: {str(e)}', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    # Use environment variables for production deployment
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
