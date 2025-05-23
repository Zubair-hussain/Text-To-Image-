import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# ---------- STYLING ----------
st.set_page_config(page_title="Text to Image", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #111;
        }
        .centered-title {
            text-align: center;
            font-family: Arial, sans-serif;
            font-size: 32px;
            color: #ffffff;
            margin-top: 30px;
            margin-bottom: 20px;
        }
        .stTextInput input {
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
            width: 100%;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            font-size: 18px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .image-container {
            text-align: center;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<div class='centered-title'>Text to Image</div>", unsafe_allow_html=True)

# ---------- INPUT ----------
prompt = st.text_input("Enter a prompt to generate image", placeholder="e.g. A futuristic city in the clouds")

# ---------- LOAD PIPELINE ----------
@st.cache_resource
def load_pipeline():
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        torch_dtype=torch.float32
    )
    pipe.to("cpu")  # Required for Streamlit Cloud (no GPU)
    return pipe

pipe = load_pipeline()

# ---------- SUBMIT ----------
if st.button("Generate Image"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating image..."):
            image = pipe(prompt).images[0]
            st.markdown('<div class="image-container">', unsafe_allow_html=True)
            st.image(image, caption="Generated Image", use_column_width=True)
            st.markdown('</div>', unsafe_allow_html=True)