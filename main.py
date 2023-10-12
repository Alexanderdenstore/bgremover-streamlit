from rembg import remove
from io import BytesIO
from PIL import Image

import streamlit as st


def remove_background(uploaded_image):
    """
    Removes the background from an uploaded image and provides a download link.
    """
    try:
        # Open the uploaded image and process it
        image = Image.open(uploaded_image)
        output = remove(image)

        # Convert to bytes for download
        img_byte_arr = BytesIO()
        output.save(img_byte_arr, format="PNG")
        img_bytes = img_byte_arr.getvalue()

        st.download_button(
            label="Download Image",
            data=img_bytes,
            file_name="result.png",
            mime="image/png",
        )

        st.image(output, use_column_width=True)

    except Exception as e:
        st.error(f"An error occured: {e}")


st.title("Background Remover")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    with st.spinner("Removing background..."):
        remove_background(uploaded_file)
