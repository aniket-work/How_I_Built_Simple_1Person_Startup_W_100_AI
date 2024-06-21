import streamlit as st
from ui.layout import set_page_config, apply_custom_style
from ui.product_display import display_products
from data.products import products
from config import APP_TITLE
from utils.logging_config import configure_logging


def main():
    configure_logging()
    set_page_config()
    apply_custom_style()

    st.title(APP_TITLE)

    display_products(products)


if __name__ == "__main__":
    main()