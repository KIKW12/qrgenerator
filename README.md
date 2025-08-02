# QR Code Generator 🔗

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Deploy](https://img.shields.io/badge/Deploy-Render-purple?style=flat-square&logo=render)](https://render.com)

A modern, responsive web application for generating high-quality QR codes from URLs. Built with Flask and optimized for cloud deployment.

## ✨ Features

- 🔗 **URL to QR Code**: Convert any URL into a scannable QR code instantly
- 🎨 **Customizable Options**: Adjust QR code size, border thickness, and error correction
- 💾 **High-Quality Downloads**: Generate crisp PNG files ready for print or digital use
- 📱 **Responsive Design**: Seamless experience across desktop, tablet, and mobile devices
- 🖼️ **Gallery Management**: View, organize, and re-download previously generated QR codes
- ⚡ **Lightning Fast**: Generate QR codes in milliseconds with optimized processing
- � **Secure & Validated**: Input sanitization and secure file handling
- 🌐 **Production Ready**: Optimized for cloud deployment with proper configuration

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git (for cloning)

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KIKW12/qr-generator.git
   cd qr-generator
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   ```bash
   cp .env.example .env
   # Edit .env with your preferred settings
   ```

5. **Run the application:**

   ```bash
   python app.py
   ```

6. **Open your browser:**

   ```text
   http://localhost:5000
   ```

## 🌐 Cloud Deployment

### Deploy to Render

This application is optimized for [Render](https://render.com) deployment:

1. **Fork this repository** to your GitHub account

2. **Connect to Render:**
   - Sign up at [render.com](https://render.com)
   - Connect your GitHub account
   - Create a new Web Service

3. **Configuration:**
   - **Build Command:** `pip install --upgrade pip setuptools wheel && pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Environment Variables:**
     - `SECRET_KEY`: Your secure secret key
     - `PYTHON_VERSION`: `3.11.9`
     - `FLASK_ENV`: `production`

4. **Deploy** and your app will be live at `https://your-app-name.onrender.com`

For detailed deployment instructions, see [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md).

## 📖 Usage

### Web Interface

1. **Generate QR Code:**
   - Enter any URL (http/https optional - will be auto-added)
   - Customize size (5-15px per box) and border (2-8px)
   - Click "Generate QR Code"
   - Preview instantly in your browser

2. **Download & Save:**
   - High-quality PNG format
   - Timestamped filenames for organization
   - Direct download or save for later

3. **Gallery Management:**
   - Browse all generated QR codes
   - Re-download previous codes
   - View creation timestamps and settings

## 🏗️ Project Architecture

```text
qrGenerator/
├── app.py                    # Main Flask application
├── requirements.txt          # Production dependencies
├── requirements-alt.txt      # Alternative dependency versions
├── runtime.txt              # Python version specification
├── setup.cfg               # Build configuration
├── .env                    # Environment variables (local)
├── .env.example           # Environment template
├── .gitignore            # Git ignore rules
├── README.md            # Project documentation
├── RENDER_DEPLOYMENT.md # Deployment guide
├── templates/          # Jinja2 HTML templates
│   ├── base.html      # Base layout template
│   ├── index.html     # Homepage with QR form
│   ├── result.html    # QR code display page
│   └── gallery.html   # QR code gallery
└── static/
    └── qr_codes/      # Generated QR codes (auto-created)
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `SECRET_KEY` | Flask session security key | Generated | Yes |
| `FLASK_ENV` | Flask environment mode | `development` | No |
| `PORT` | Application port | `5000` | No |
| `PYTHON_VERSION` | Python runtime version | `3.11.9` | Deploy only |

### Customization Options

**QR Code Settings:**
- **Box Size:** 5-15 pixels (controls QR code resolution)
- **Border:** 2-8 pixels (white space around code)
- **Error Correction:** Level L (~7% restoration capability)
- **Format:** PNG with transparent background support

**Application Settings:**
- **File Storage:** Local filesystem (`static/qr_codes/`)
- **Gallery Limit:** 20 most recent codes (configurable)
- **File Naming:** Auto-generated with timestamp and domain

## 🔧 API Reference

### Core Functions

```python
create_qr_code(url, filename=None, size=10, border=4)
```

**Parameters:**
- `url` (str): Target URL for QR code
- `filename` (str, optional): Custom filename
- `size` (int): Box size in pixels (5-15)
- `border` (int): Border size in pixels (2-8)

**Returns:** File path of generated QR code

## 🚨 Troubleshooting

### Common Issues

**Build Errors:**

```bash
# Update build tools
pip install --upgrade pip setuptools wheel

# Clear cache and reinstall
pip cache purge
pip install -r requirements.txt
```

**Permission Errors:**

```bash
# Ensure write permissions
chmod 755 static/
mkdir -p static/qr_codes/
```

**Port Conflicts:**

```bash
# Change port in app.py or via environment
export PORT=5001
python app.py
```

**Deployment Issues:**
- Verify `runtime.txt` has correct Python version
- Check environment variables are set correctly
- Review build logs for specific error messages

### Dependencies

**Core Requirements:**
- Python 3.11+ (recommended)
- Flask 3.0+ (web framework)
- qrcode 7.4+ (QR generation)
- Pillow 10.0+ (image processing)
- gunicorn 23.0+ (WSGI server)

**Build Tools:**
- setuptools 65.0+
- wheel 0.38+
- pip 22.0+

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/qr-generator.git
cd qr-generator

# Create development environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install -e .

# Run tests (if available)
python -m pytest

# Start development server
flask --app app run --debug
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [qrcode](https://github.com/lincolnloop/python-qrcode) - Python QR code generation library
- [Flask](https://flask.palletsprojects.com/) - Lightweight web framework
- [Pillow](https://pillow.readthedocs.io/) - Python Imaging Library
- [Bootstrap](https://getbootstrap.com/) - Frontend framework
- [Font Awesome](https://fontawesome.com/) - Icon library

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/KIKW12/qr-generator/issues)
- **Discussions:** [GitHub Discussions](https://github.com/KIKW12/qr-generator/discussions)
- **Documentation:** This README and inline code comments

---

## 🎯 Happy QR Code Generating!

Built with ❤️ for developers who need reliable QR code generation.
