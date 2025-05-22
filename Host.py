import streamlit as st
from diffusers import DiffusionPipeline
import torch

# ---------- STYLING ----------
st.set_page_config(page_title="Image Prompt Tool", layout="centered")

st.markdown("""
    <style>
        .centered-title {
            text-align: center;
            font-family: Arial, sans-serif;
            font-size: 32px;
            color: #333;
            margin-top: 30px;
            margin-bottom: 20px;
        }
        .prompt-box input {
            font-size: 18px !important;
            padding: 12px !important;
            border-radius: 8px;
            border: 1px solid #ccc;
            width: 100% !important;
        }
        .submit-button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            font-size: 18px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        .submit-button:hover {
            background-color: #45a049;
        }
        .image-container {
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<div class='centered-title'>Image Prompt Interface</div>", unsafe_allow_html=True)

# ---------- INPUT ----------
prompt = st.text_input(" ", placeholder="Describe your image...", key="prompt")

# ---------- LOAD PIPELINE ----------
@st.cache_resource(show_spinner=False)
def load_pipeline():
    pipe = DiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",   # lighter, more compatible model
        torch_dtype=torch.float32           # float32 for CPU compatibility
    )
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe.to(device)
    return pipe

pipe = load_pipeline()

# ---------- SUBMIT ----------
if st.button("Submit", use_container_width=True):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Creating your image..."):
            image = pipe(prompt=prompt).images[0]
            st.markdown("<div class='image-container'>", unsafe_allow_html=True)
            st.image(image, caption="Generated Image", use_column_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
