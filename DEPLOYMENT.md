# Deployment Guide - ResumeBooster on Streamlit Cloud

## Prerequisites
- GitHub account
- Streamlit Cloud account (free at https://share.streamlit.io)
- Your project pushed to GitHub

## Step-by-Step Deployment

### 1. Prepare Your GitHub Repository
```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit for ResumeBooster deployment"

# Add your GitHub remote
git remote add origin https://github.com/YOUR_USERNAME/CareerBooster.git
git branch -M main
git push -u origin main
```

### 2. Create Streamlit Cloud Account
1. Go to https://share.streamlit.io
2. Sign up with your GitHub account
3. Authorize Streamlit to access your repositories

### 3. Deploy on Streamlit Cloud
1. Click **"New app"** button
2. Select your repository: `CareerBooster`
3. Select branch: `main`
4. Set main file path: `app.py`
5. Click **"Deploy"**

### 4. Monitor Deployment
- Your app URL: `https://share.streamlit.io/YOUR_USERNAME/CareerBooster/main/app.py`
- First deployment takes 2-5 minutes
- Check logs during deployment for any issues

## Project Structure for Deployment
```
CareerBooster/
├── .streamlit/
│   ├── config.toml          # Streamlit configuration
│   └── secrets.toml         # (Optional) for environment secrets
├── data/                    # Role profiles and datasets
├── app.py                   # Main Streamlit app
├── requirements.txt         # Python dependencies
├── README.md
├── DEPLOYMENT.md           # This file
└── [Other Python modules]
```

## Important Configuration Notes

### File Size Limitations
- Streamlit Cloud has a **default 200MB upload limit** per session
- For large PDF resumes, ensure `maxUploadSize = 200` in `.streamlit/config.toml`

### Performance Optimization (Important for CPU-only deployment)
- BERT model initialization takes ~30-60 seconds on first run
- Consider caching the embedder model using Streamlit's `@st.cache_resource`
- Session state is preserved during user interaction

### Memory Management
- CPU-only environment has ~1GB allocated memory
- Model is cached in memory after first load
- For heavy usage, consider GPU-enabled tier (paid)

## Environment Variables & Secrets
If you need to add environment variables:

1. Create `.streamlit/secrets.toml` (do NOT commit this file):
```toml
api_key = "your-secret-key"
database_url = "your-database-url"
```

2. Update `.gitignore` (already done):
```
.streamlit/secrets.toml
```

3. Access in code:
```python
import streamlit as st
secret_value = st.secrets["api_key"]
```

## Troubleshooting

### App takes too long to load
- First load initializes BERT model (~30s) - this is normal
- Subsequent loads are faster due to caching
- Consider using smaller model or GPU tier for faster initialization

### Memory errors
- Clear browser cache
- Reduce simultaneous users
- Optimize PDF processing in `document_processor.py`

### Upload fails
- Ensure PDFs are under 50MB each
- Check PDF format is valid
- Try different PDF files to isolate the issue

## Monitoring & Logs
1. Go to your app on https://share.streamlit.io
2. Click the menu (3 dots) → Settings
3. View deployment logs in "Logs" section

## Updating Your App
To push updates:
```bash
git add .
git commit -m "Update: description of changes"
git push origin main
```
Streamlit automatically redeploys within 1-2 minutes.

## Switching to Paid Tier (Optional)
For better performance:
1. Go to https://share.streamlit.io/settings
2. Upgrade your workspace
3. Enable GPU acceleration for faster BERT inference

---

**Need Help?**
- Streamlit Docs: https://docs.streamlit.io
- Community Forum: https://discuss.streamlit.io
- CLI Debugging: Run `streamlit run app.py` locally first
