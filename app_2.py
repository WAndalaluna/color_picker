import streamlit as st
from PIL import Image
from colorthief import ColorThief
import io

# Set up page configuration
st.set_page_config(page_title="Dominant Color Picker", page_icon="🎨", layout="centered")

# Define function to get color palette
def get_palette(image, color_count=5):
    color_thief = ColorThief(image)
    palette = color_thief.get_palette(color_count=color_count)
    return palette

# Title and description
st.title('Dominant Color Picker 🎨')
st.write('Unggah sebuah gambar dan dapatkan palet warna dominan.')

# File uploader for image upload
uploaded_file = st.file_uploader("Pilih sebuah gambar", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar yang diunggah', use_column_width=True)

    # Convert image to format readable by ColorThief
    image_io = io.BytesIO()
    image.save(image_io, format='PNG')
    image_io.seek(0)

    # Get palette and display colors
    with st.spinner('Memproses gambar...'):
        palette = get_palette(image_io)

    st.write('Palet warna dominan:')
    for color in palette:
        st.write(f'RGB: {color}')
        st.markdown(
            f'<div style="background-color: rgb{color}; width: 100px; height: 50px; margin: 10px auto; border-radius: 5px;"></div>',
            unsafe_allow_html=True
        )

# Add custom CSS for styling
st.markdown(
    """
    <style>
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stFileUploader {
        text-align: center;
    }
    .css-1cpxqw2 {
        text-align: center;
    }
    .css-17eq0hr {
        margin: 0 auto;
    }
    .css-1d391kg {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)
