import sys
sys.stdout = sys.__stdout__

import streamlit as st
import requests
from time import sleep
import logging

# Configure logging to print logs in the command prompt
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
console_handler.setFormatter(formatter)
root_logger.addHandler(console_handler)

# Set up the Streamlit page configuration with title, icon, and wide layout
st.set_page_config(
    page_title="Aniket Shopping Mart",
    page_icon="🛒",
    layout="wide"
)

# Set the title of the Streamlit app
st.title(" 🛒 Aniket Shopping Mart 🛒")

# Add sky blue background color and dark font color
st.markdown(
    """
    <style>
        .stApp {
            background-color: #87CEEB;
            color: black;
        }
        .stMarkdown, .stTitle, .stTextInput > label, .stCheckbox > label {
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Dictionary containing product names, image file paths, and details
products = {
    "Smart TV": {
        "image": "images/tv.jpg",
        "details": "55-inch 4K Ultra HD Smart LED TV\nPrice: $599.99\nDimensions: 48.5 x 28.2 x 3.0 inches\nWeight: 35.7 lbs\nShipping: Fast"
    },
    "Refrigerator": {
        "image": "images/fridge.jpg",
        "details": "French Door Refrigerator with Ice Maker\nPrice: $1299.99\nDimensions: 35.75 x 70 x 35.25 inches\nWeight: 320 lbs\nShipping: Priority"
    },
    "Laptop Charger": {
        "image": "images/laptop_charger.jpg",
        "details": "Universal 90W Laptop Charger\nPrice: $39.99\nCompatible with most laptops\nWeight: 0.8 lbs\nShipping: Regular"
    },
    "Portable Fan": {
        "image": "images/portable_fan.jpg",
        "details": "Rechargeable Portable Fan\nPrice: $24.99\nDimensions: 6.3 x 3.9 x 7.5 inches\nWeight: 1.2 lbs\nShipping: Regular"
    },
    "Office Chair": {
        "image": "images/office_chair.jpg",
        "details": "Ergonomic Mesh Office Chair\nPrice: $149.99\nWeight capacity: 250 lbs\nProduct Weight: 35 lbs\nShipping: Fast"
    },
    "Microphone": {
        "image": "images/microphone.jpg",
        "details": "USB Condenser Microphone\nPrice: $79.99\nFrequency Response: 20Hz - 20kHz\nWeight: 1.5 lbs\nShipping: Regular"
    },
    "USB Flash Drive": {
        "image": "images/usb_drive.jpg",
        "details": "128GB USB 3.0 Flash Drive\nPrice: $19.99\nRead speed: up to 100MB/s\nWeight: 0.03 lbs\nShipping: Regular"
    },
    "Coffee Maker": {
        "image": "images/coffee_maker.jpg",
        "details": "12-Cup Programmable Coffee Maker\nPrice: $89.99\nCapacity: 60 oz\nWeight: 7 lbs\nShipping: Fast"
    },
    "Wireless Earbuds": {
        "image": "images/wireless_earbuds.jpg",
        "details": "True Wireless Bluetooth Earbuds\nPrice: $129.99\nBattery Life: Up to 6 hours\nWeight: 0.18 lbs (with case)\nShipping: Priority"
    }
}

def send_post_request(product_name, product_details):
    """
    Sends a POST request to the specified URL with the selected product details.

    Args:
        product_name (str): The name of the selected product.
        product_details (str): The details of the selected product.

    Returns:
        dict: The response data from the API.
    """
    url = "http://127.0.0.1:8080/llm"
    payload = {"product_name": product_name, "product_details": product_details}
    st.write(f"Payload: {payload}")
    response = requests.post(url, json=payload)

    # Wait for the response to be received
    while response.status_code != 200:
        sleep(0.1)

    response_data = response.json()
    st.write(f"Response: {response_data}")
    return response_data


# Organize the products into rows
all_products = list(products.items())


def display_product(col, product_name, product_info, index):
    with col:
        st.image(product_info["image"], use_column_width=True)
        st.markdown(f"**{product_name}**")  # Bold product name
        if st.checkbox(f"Select {product_name}", key=f"checkbox_{index}"):
            details_html = product_info["details"].replace('\n', '<br>')
            st.markdown(
                f"""
                <div style="background-color: white; padding: 10px; border-radius: 5px;">
                    <p style="white-space: pre-wrap; word-wrap: break-word; font-weight: bold; color: black;">
{details_html}
                    </p>
                </div>
                </br>
                """,
                unsafe_allow_html=True
            )
            if st.button(f"Submit {product_name}", key=f"button_{index}"):
                response = send_post_request(product_name, product_info["details"])


# Display products in rows of 3
for i in range(0, len(all_products), 3):
    row_products = all_products[i:i + 3]
    cols = st.columns(3)

    for j, (product_name, product_info) in enumerate(row_products):
        display_product(cols[j], product_name, product_info, i + j)

    # Add spacing between rows
    st.write("")
    st.write("")