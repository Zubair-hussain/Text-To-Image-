import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import os

# ---------- STREAMLIT PAGE CONFIG ----------
st.set_page_config(page_title="Premium Text to Image", layout="centered")

# ---------- CUSTOM STYLES ----------
st.markdown("""
    <style>
        body {
            background-color: #0f0f0f;
            font-family: 'Helvetica Neue', sans-serif;
        }
        .centered-title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            background: linear-gradient(270deg, #ffffff, #aaaaaa, #ffffff);
            background-size: 400% 400%;
            color: transparent;
            -webkit-background-clip: text;
            animation: shimmer 6s ease infinite;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        @keyframes shimmer {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .stTextInput>div>div>input {
            font-size: 18px;
            padding: 12px 16px;
            border-radius: 50px;
            border: 2px solid #555;
            background-color: #1f1f1f;
            color: white;
        }
        .submit-button {
            position: absolute;
            right: 20px;
            top: 6px;
            background-color: #4CAF50;
            border-radius: 50%;
            border: none;
            height: 42px;
            width: 42px;
            color: white;
            font-size: 18px;
            cursor: pointer;
        }
        .image-container {
            text-align: center;
            margin-top: 30px;
        }
        .description {
            color: #bbb;
            font-size: 16px;
            margin-top: 20px;
            text-align: center;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<div class='centered-title'>Premium Text to Image</div>", unsafe_allow_html=True)

# ---------- INPUT PROMPT ----------
col1, col2 = st.columns([8, 1])
with col1:
    prompt = st.text_input("", placeholder="Describe an image...", key="prompt")
with col2:
    submit = st.button("➤", key="submit_btn")  # Unicode for ➤

# ---------- LOAD PIPELINE ----------
@st.cache_resource
def load_pipeline():
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        torch_dtype=torch.float32
    )
    pipe.to("cpu")
    return pipe

pipe = load_pipeline()

# ---------- GENERATE IMAGE ----------
if submit:
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating your premium image..."):
            result = pipe(prompt)
            image = result.images[0]
            st.markdown('<div class="image-container">', unsafe_allow_html=True)
            st.image(image, caption="Generated Image", use_column_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

# ---------- DESCRIPTION ----------
st.markdown("""
<div class='description'>
    <strong>How to write great prompts:</strong><br>
    Be specific! Instead of "a cat", try "a white fluffy cat lounging on a cozy chair in sunlight".<br>
    Use styles like "in cyberpunk style", "as a 3D render", or "with oil painting effect" for better results.<br>
    You can include lighting (golden hour, neon), locations (in a desert, on Mars), moods (dramatic, peaceful), and more!
</div>
""", unsafe_allow_html=True)
