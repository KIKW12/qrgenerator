# Deploy QR Generator to Render

## Step-by-Step Render Deployment Guide

### 1. Prepare Your Code
✅ Your app is already configured for Render deployment!

### 2. Push to GitHub
1. Create a new repository on GitHub
2. Push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: QR Code Generator"
   git branch -M main
   git remote add origin https://github.com/yourusername/qr-generator.git
   git push -u origin main
   ```

### 3. Deploy on Render
1. Go to [https://render.com](https://render.com)
2. Sign up/Login with your GitHub account
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Use these settings:

**Basic Settings:**
- **Name**: `qr-generator` (or your preferred name)
- **Region**: Choose closest to your users
- **Branch**: `main`
- **Root Directory**: Leave blank
- **Runtime**: `Python 3`

**Build Settings:**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

**Advanced Settings:**
- **Environment Variables**:
  - `SECRET_KEY`: Generate a secure random string
  - `PYTHON_VERSION`: `3.11.0`

### 4. Environment Variables Setup
In Render dashboard, add these environment variables:

| Key | Value | Description |
|-----|-------|-------------|
| `SECRET_KEY` | `your-super-secret-random-string-here` | Flask secret key for sessions |
| `PYTHON_VERSION` | `3.11.0` | Python version |

**Generate a secure SECRET_KEY:**
```python
import secrets
print(secrets.token_hex(32))
```

### 5. Deploy!
1. Click "Create Web Service"
2. Render will automatically:
   - Clone your repository
   - Install dependencies
   - Start your application
3. Your app will be live at: `https://your-app-name.onrender.com`

### 6. Custom Domain (Optional)
- In your service settings, you can add a custom domain
- Render provides free SSL certificates

## Expected Deployment Time
- First deployment: 2-5 minutes
- Subsequent deployments: 1-3 minutes

## Render Features You Get
- ✅ **Automatic HTTPS** - Free SSL certificate
- ✅ **Auto-deploy** - Deploys when you push to GitHub
- ✅ **Free tier** - 750 hours/month free
- ✅ **Custom domains** - Add your own domain
- ✅ **Environment variables** - Secure config management
- ✅ **Logs** - Real-time application logs

## Troubleshooting

### Build Fails
- Check your `requirements.txt` file
- Ensure Python version compatibility
- Check build logs in Render dashboard

### App Won't Start
- Verify `Procfile` contains: `web: gunicorn app:app`
- Check that your Flask app variable is named `app`
- Review application logs

### File Upload Issues
- Note: Render's free tier has ephemeral storage
- Generated QR codes will be lost on app restart
- Consider using cloud storage for persistence

## Post-Deployment
Once deployed, your QR Generator will be accessible at your Render URL. You can:
- Generate QR codes from any device
- Share the URL with others
- Use it for personal or business projects

## Free Tier Limitations
- **Sleep after inactivity**: App sleeps after 15 minutes of no requests
- **750 hours/month**: Free usage limit
- **Ephemeral storage**: Files don't persist between deployments

## Upgrade Options
If you need more features:
- **Starter Plan ($7/month)**: No sleep, more resources
- **Standard Plan ($25/month)**: Even more resources, custom domains

Your QR Generator is now ready for the world! 🎉
