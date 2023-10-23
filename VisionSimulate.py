import streamlit as st
from PIL import Image, ImageFilter, ImageOps

def simulate_blurred_vision(image: Image.Image) -> Image.Image:
    """Simula visão embaçada."""
    return image.filter(ImageFilter.GaussianBlur(radius=5))

def simulate_deuteranopia(image: Image.Image) -> Image.Image:
    """Simula deuteranopia (forma de daltonismo)."""
    data = [
        0.625, 0.375, 0.0, 0.0,
        0.7, 0.3, 0.0, 0.0,
        0.0, 0.3, 0.7, 0.0
    ]
    image = image.convert("RGB")
    return ImageOps.colorize(image, "RGB", data)

st.title("Simulador de Visão")

uploaded_file = st.file_uploader("Escolha uma imagem", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagem original.', use_column_width=True)

    option = st.selectbox(
        'Escolha a simulação',
        ('Original', 'Visão Embaçada', 'Deuteranopia (daltonismo)')
    )

    if option == 'Visão Embaçada':
        st.image(simulate_blurred_vision(image), caption='Simulação de visão embaçada.', use_column_width=True)
    elif option == 'Deuteranopia (daltonismo)':
        st.image(simulate_deuteranopia(image), caption='Simulação de deuteranopia.', use_column_width=True)
