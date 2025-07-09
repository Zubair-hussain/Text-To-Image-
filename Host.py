#  Install dependencies before running (in Colab or locally)
# !pip install streamlit diffusers transformers accelerate safetensors pyngrok python-dotenv --quiet

import os
import threading
from dotenv import load_dotenv
from pyngrok import ngrok
import streamlit as st
from diffusers import StableDiffusionPipeline
import torch

#  Load environment variables from .env (Optional)
load_dotenv()

# OPTIONAL: Set Ngrok token (if using ngrok auth token)
NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN")  # <-- Make sure to define this in your local .env
if NGROK_AUTH_TOKEN:
    ngrok.set_auth_token(NGROK_AUTH_TOKEN)

# Kill previous tunnels
ngrok.kill()

# ---------- Streamlit App ----------
def write_app():
    st.set_page_config(page_title="Text to Image", layout="centered")

    st.markdown("""<style>
        .main { background-color: #0f0f0f; color: white; min-height: 100vh; padding: 30px 20px; }
        .centered-title {
            font-size: 42px; font-weight: 700;
            background: linear-gradient(90deg, #4facfe, #00f2fe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 40px; text-align: center;
        }
        .input-container input {
            width: 100%; max-width: 700px; font-size: 18px;
            padding: 14px 20px; border-radius: 30px;
            border: 2px solid #4facfe; background-color: #1e1e1e;
            color: white; margin-bottom: 20px;
        }
        .image-container img {
            border-radius: 20px; max-width: 100%;
            box-shadow: 0 0 15px #00f2fe88;
        }
    </style>""", unsafe_allow_html=True)

    st.markdown('<div class="centered-title">Text to Image</div>', unsafe_allow_html=True)
    prompt = st.text_input("", placeholder="Describe an image...")

    if st.button("Generate ➤"):
        if not prompt.strip():
            st.warning("Please enter a prompt.")
        else:
            with st.spinner("Generating image..."):
                pipe = load_pipeline()
                result = pipe(prompt)
                image = result.images[0]
                st.markdown('<div class="image-container">', unsafe_allow_html=True)
                st.image(image, caption="Generated Image", use_column_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style='color:#bbb; text-align:center; margin-top:40px;'>
    <strong>Tip:</strong> Use rich prompts like 
    <br><em>"A futuristic city skyline at night, in cyberpunk style"</em><br>
    for best results.
    </div>
    """, unsafe_allow_html=True)

@st.cache_resource(show_spinner=False)
def load_pipeline():
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        torch_dtype=torch.float32
    )
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe

# Write the app code to app.py
with open("app.py", "w") as f:
    f.write("\n".join([line for line in write_app.__code__.co_consts if isinstance(line, str)]) or "")

# Run app in background thread
def run():
    os.system("streamlit run app.py")

threading.Thread(target=run, daemon=True).start()

# Expose via ngrok (no token needed if public/free usage)
public_url = ngrok.connect(8501)
print(f"🔗 App is live at: {public_url}")
