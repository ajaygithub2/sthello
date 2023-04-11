import pygame
import pygame.camera
from pygame.locals import *
import streamlit as st

st.write("Hello Motherfuckers")

pygame.init()
pygame.camera.init()

camlist = pygame.camera.list_cameras()
if camlist:
    cam = pygame.camera.Camera(camlist[0],(640,480))
cam.start()

image = cam.get_image()
st.image(image)
