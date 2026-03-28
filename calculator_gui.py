import tkinter as tk #Creates GUI window
from tkinter import filedialog #Let the user select the image
from PIL import Image, ImageTk #Displays the image
import easyocr #Reads the text from file
import cv2 #image processing 
from sympy import sympify #solves math

#initialize ocr
reader= easyocr.Reader(['en'],gpu='false')
