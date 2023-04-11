import pygame
import pygame.camera
from pygame.locals import *
import streamlit as st

st.write("Hello Motherfuckers")

pygame.init()
pygame.camera.init()

cam = pygame.camera.Camera("/path/to/camera",(640,480))
cam.start()

image = cam.get_image()
st.image(image)
