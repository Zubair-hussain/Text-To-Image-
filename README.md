#  Text to Image Generator

A modern web application that generates images from text descriptions using Stable Diffusion AI model. Built with Streamlit and designed with a sleek dark theme interface.

##  Features

- **Text-to-Image Generation**: Convert text prompts into high-quality images using Stable Diffusion
- **Modern UI**: Dark theme with gradient styling and responsive design
- **Real-time Processing**: Instant image generation with loading indicators
- **Public Access**: Automatically exposed via ngrok for easy sharing
- **GPU Support**: Optimized for CUDA when available, falls back to CPU

##  Prerequisites

- Python 3.7+
- GPU with CUDA support (recommended) or CPU
- Internet connection for model downloads

##  Installation

### Option 1: Google Colab (Recommended)

1. Upload all files to Google Colab
2. Run the Colab-specific runner:
```python
!python run_colab.py
```

### Option 2: Local Installation

1. Clone or download all files to your local machine
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

### Option 3: Quick Local Setup

Use the local runner that automatically checks and installs dependencies:
```bash
python local_run.py
```

##  Configuration

### Environment Variables (Optional)

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Add your ngrok auth token (optional):
```env
NGROK_AUTH_TOKEN=your_ngrok_auth_token_here
```

**Note**: Ngrok auth token is optional for basic usage but recommended for persistent URLs.

##  Usage

1. **Start the Application**: 
   - Local: `python main.py`
   - Colab: `python run_colab.py`

2. **Access the Interface**: Click the ngrok URL that appears in the console

3. **Generate Images**: 
   - Enter a descriptive text prompt
   - Click "Generate ➤"
   - Wait for the AI to process your request
   - View your generated image

### Example Prompts

```
"A futuristic city skyline at night, cyberpunk style, neon lights"
"A serene mountain landscape with crystal clear lake, morning mist"
"Portrait of a wise old wizard, fantasy art style, detailed"
"Abstract art with vibrant colors and geometric patterns"
"A cute robot playing with butterflies in a magical garden"
```

##  Interface Features

- **Responsive Design**: Works on desktop and mobile devices
- **Dark Theme**: Easy on the eyes with blue gradient accents
- **Input Validation**: Prevents empty prompt submissions
- **Loading States**: Visual feedback during image generation
- **Error Handling**: User-friendly error messages
- **Image Display**: Rounded corners with glowing effects

## 🔧 Technical Details

### Model Information
- **Base Model**: CompVis/stable-diffusion-v1-4
- **Framework**: Hugging Face Diffusers
- **Precision**: Float32 (configurable)

### Performance Optimization
- **Model Caching**: Uses Streamlit's `@st.cache_resource` for efficient loading
- **GPU Acceleration**: Automatically detects and uses CUDA when available
- **Background Processing**: Runs Streamlit in a separate thread

### Project Structure
```
text-to-image-generator/
├── main.py              # Main application entry point
├── app.py               # Auto-generated Streamlit app
├── requirements.txt     # Python dependencies
├── setup.py            # Package setup configuration
├── .env.example        # Environment variables template
├── .env                # Your environment variables (create from example)
├── local_run.py        # Local development runner
├── run_colab.py        # Google Colab runner
└── README.md           # This file
```

### Dependencies
- `streamlit>=1.28.0` - Web application framework
- `diffusers>=0.21.0` - Stable Diffusion model implementation
- `transformers>=4.34.0` - Hugging Face transformers library
- `torch>=2.0.0` - PyTorch deep learning framework
- `accelerate>=0.21.0` - Hugging Face acceleration library
- `safetensors>=0.3.0` - Safe tensor serialization
- `pyngrok>=6.0.0` - Python wrapper for ngrok tunneling
- `python-dotenv>=1.0.0` - Environment variable management

##  Important Notes

### First Run
- The first execution will download the Stable Diffusion model (~4GB)
- This may take several minutes depending on your internet connection
- Subsequent runs will be faster due to model caching

### Hardware Requirements
- **GPU**: NVIDIA GPU with 4GB+ VRAM (recommended)
- **CPU**: Multi-core processor (fallback option)
- **RAM**: 8GB+ system memory
- **Storage**: 10GB+ free space for model files

### Limitations
- Image generation can take 30-60 seconds per image
- CPU generation is significantly slower than GPU
- Some prompts may not produce expected results

##  Troubleshooting

### Common Issues

**"CUDA out of memory"**
```bash
# Solution: The app will automatically fall back to CPU
# Or close other GPU-intensive applications
```

**"Model download failed"**
```bash
# Check internet connection
# Verify sufficient disk space (10GB+)
# Try running again (downloads can resume)
```

**"Ngrok tunnel failed"**
```bash
# Check if port 8501 is available
# Verify ngrok installation: pip install pyngrok
# Try restarting the application
```

**"ModuleNotFoundError"**
```bash
# Install missing dependencies
pip install -r requirements.txt

# Or use the local runner
python local_run.py
```

**"Streamlit not found"**
```bash
# Install Streamlit
pip install streamlit

# Or reinstall all dependencies
pip install -r requirements.txt
```

### Getting Help
- Check the console output for detailed error messages
- Ensure all dependencies are properly installed
- Verify your Python version compatibility (3.7+)
- Make sure you have sufficient disk space for model downloads

##  Development

### Running in Development Mode
```bash
# Install in development mode
pip install -e .

# Run with auto-reload
streamlit run app.py --server.runOnSave=true
```

### Creating a Distribution
```bash
# Build the package
python setup.py sdist bdist_wheel

# Install locally
pip install dist/text-to-image-generator-1.0.0.tar.gz
```

##  Security Notes

- The application uses ngrok to create public tunnels
- Be cautious when sharing ngrok URLs publicly
- Consider using ngrok auth tokens for better security
- The app runs on your local machine and processes are isolated

##  License

This project uses the Stable Diffusion model which has specific licensing terms. Please review the [model's license](https://huggingface.co/CompVis/stable-diffusion-v1-4) before commercial use.

##  Contributing

Feel free to submit issues, feature requests, or pull requests to improve this application.

### Development Setup
1. Fork the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Make your changes
6. Test thoroughly
7. Submit a pull request

##  Future Enhancements

- [ ] Multiple model support (SD 2.0, DALL-E, etc.)
- [ ] Batch image generation
- [ ] Image editing capabilities
- [ ] Custom model fine-tuning
- [ ] Advanced prompt engineering tools
- [ ] Image upscaling options
- [ ] Style transfer features
- [ ] API endpoint creation
- [ ] Docker containerization
- [ ] Database integration for image storage

## 📊 Performance Benchmarks

| Hardware | Generation Time | Memory Usage |
|----------|----------------|--------------|
| RTX 3090 | 15-30 seconds | 8GB VRAM |
| RTX 3060 | 30-45 seconds | 6GB VRAM |
| CPU (16 cores) | 2-5 minutes | 8GB RAM |

##  Acknowledgments

- [Hugging Face](https://huggingface.co/) for the Diffusers library
- [Stability AI](https://stability.ai/) for the Stable Diffusion model
- [Streamlit](https://streamlit.io/) for the web framework
- [ngrok](https://ngrok.com/) for public URL tunneling

## Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Look for similar issues in the project issues
3. Create a new issue with detailed information
4. Include your system specs and error messages

---

**Happy generating! **

Made with ❤️ by Zubair Hussain
