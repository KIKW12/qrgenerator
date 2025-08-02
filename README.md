# QR Code Generator Web App

A simple and elegant web application for generating QR codes that redirect to any URL. Built with Flask and Python.

## Features

- 🔗 **URL to QR Code**: Convert any URL into a scannable QR code
- 🎨 **Customizable**: Adjust QR code size and border thickness
- 💾 **Download Ready**: Generate high-quality PNG files
- 📱 **Responsive Design**: Works perfectly on desktop and mobile
- 🖼️ **Gallery View**: See all your previously generated QR codes
- ⚡ **Instant Generation**: Create QR codes in seconds
- 🔄 **Never Ending**: Generate unlimited QR codes

## Installation

1. **Clone or download this repository**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or install individually:
   ```bash
   pip install Flask==2.3.3
   pip install qrcode[pil]==7.4.2
   pip install Pillow==10.0.1
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

## Usage

### Web Interface

1. **Generate QR Code:**
   - Enter any URL (with or without http/https)
   - Choose your preferred size and border settings
   - Click "Generate QR Code"

2. **Download:**
   - View the generated QR code instantly
   - Download as PNG file
   - Access from the gallery later

3. **Gallery:**
   - View all your previously generated QR codes
   - Download any previous QR code
   - See creation timestamps

### Command Line (Original Script)

You can still use the original command-line version:

```bash
python qr.py
```

This will start an interactive session where you can generate QR codes from the terminal.

## Project Structure

```
qrGenerator/
├── app.py                 # Main Flask application
├── qr.py                  # Original command-line QR generator
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html         # Base template with common layout
│   ├── index.html        # Home page with form
│   ├── result.html       # QR code result page
│   └── gallery.html      # Gallery of generated QR codes
└── static/
    └── qr_codes/         # Generated QR code files (auto-created)
```

## Configuration

You can modify these settings in `app.py`:

- **Port**: Change `port=5000` to your preferred port
- **Host**: Change `host='0.0.0.0'` to restrict access
- **Upload folder**: Modify `UPLOAD_FOLDER` path
- **Gallery limit**: Change the `[:20]` limit in gallery route

## Features Details

### QR Code Customization
- **Box Size**: Controls the pixel size of each QR code box (5-15px)
- **Border**: Controls the white border around the QR code (2-8px)
- **Format**: All QR codes are generated as PNG files

### Security
- Input validation for URLs
- File name sanitization
- Secure file uploads to designated folder

### Responsive Design
- Bootstrap 5 for modern, mobile-friendly interface
- Font Awesome icons for better UX
- Gradient backgrounds and smooth animations

## Troubleshooting

### Common Issues

1. **Import Errors:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. **Permission Errors:**
   - Make sure you have write permissions in the project directory
   - The app will automatically create the `static/qr_codes/` folder

3. **Port Already in Use:**
   - Change the port in `app.py`: `app.run(port=5001)`
   - Or kill the process using port 5000

### Dependencies

- **Python 3.7+**
- **Flask**: Web framework
- **qrcode**: QR code generation library
- **Pillow**: Image processing library

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## Support

If you encounter any issues or have questions, please create an issue in the repository.

---

**Happy QR Code Generating! 🎉**
