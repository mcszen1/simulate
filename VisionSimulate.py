import streamlit as st
from PIL import Image, ImageFilter, ImageOps

def simulate_blurred_vision(image: Image.Image) -> Image.Image:
    """Simula visão embaçada."""
    return image.filter(ImageFilter.GaussianBlur(radius=5))

def adjust_gamma(image: Image.Image, gamma=1.0) -> Image.Image:
    """Ajusta a correção gama da imagem."""
    invGamma = 1.0 / gamma
    table = [((i / 255.0) ** invGamma) * 255 for i in range(256)]
    return image.point(table * len(image.getbands()))

def simulate_deuteranopia(image: Image.Image) -> Image.Image:
    """Simula deuteranopia (forma de daltonismo)."""
    image = image.convert("L")  # Convertendo a imagem para escala de cinza
    image = adjust_gamma(image, gamma=1.5)  # Aplicando a correção gama
    data = [
        0.625, 0.375, 0.0, 0.0,
        0.7, 0.3, 0.0, 0.0,
        0.0, 0.3, 0.7, 0.0
    ]
    return ImageOps.colorize(image, "black", "white", data)


st.title("LABCOM - Simulador de Visão")

uploaded_file = st.file_uploader("Escolha uma imagem", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagem original.', use_column_width=True)

    option = st.radio(
        'Escolha a simulação',
        ('Original', 'Visão Embaçada', 'Deuteranopia (daltonismo)')
    )

    if option == 'Visão Embaçada':
        st.image(simulate_blurred_vision(image), caption='Simulação de visão embaçada.', use_column_width=True)
    elif option == 'Deuteranopia (daltonismo)':
        st.image(simulate_deuteranopia(image), caption='Simulação de deuteranopia.', use_column_width=True)
