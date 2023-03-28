import streamlit as st
import cv2
import dlib
import numpy as np
import face_swaping as fw
from PIL import Image
import face_swaping_video as fvd
st.title("OpenCV Demo face swapping")

uploaded_mask = st.file_uploader("Chọn ảnh nguồn...", type="jpg")
if uploaded_mask is not None :
    
    uploaded_img = st.file_uploader("Ảnh cần đích ...", type="jpg")

    if  uploaded_img is not None:
        img_mask1 = Image.open(uploaded_mask )
        img1 = Image.open(uploaded_img)
        col1, col2=  st.columns(2)

        with col1:
            st.header("Ảnh nguồn")
            st.image(img_mask1)

        with col2:
            st.header("Ảnh đích")
            st.image(img1)
        if st.button('RUN'):
            img1 = np.array(img1 )
            img_mask1 = np.array(img_mask1)
            seamlessclone = fw.faces_waping(img_mask1,img1)
            st.balloons()
            st.write("Result")
            st.image(seamlessclone)
