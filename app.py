import logging

from docarray import DocumentArray
import streamlit as st

from utils import Status, get_prompt, get_images

if 'status' not in st.session_state:
    st.session_state['status'] = Status.PROMPT


def main():
    if 'fav_docs' not in st.session_state:
        logging.info(f'reset fav_docs')
        st.session_state.fav_docs = DocumentArray.empty()
    num_fav_imgs = len(st.session_state.fav_docs)
    logging.info(f'num_fav_img: {num_fav_imgs}')
    new_da = get_images(skip=num_fav_imgs)
    if new_da:
        st.session_state.fav_docs.extend(new_da)
        logging.info(f'load data successfully. len(da): {len(new_da)}')
    get_prompt()


main()
