import tkinter as tk #Creates GUI window
from tkinter import filedialog #Let the user select the image
from PIL import Image, ImageTk #Displays the image
import easyocr #Reads the text from file
import cv2 #image processing 
from sympy import sympify #solves math

root=tk.Tk()
root.title("Calculator")

panel=tk.Label(root)
panel.pack()
output_text=tk.Text(root,height=15,width=50)
output_text.pack()
#initialize ocr
reader= easyocr.Reader(['en'],gpu='false')

#extracts texts from image
def extract_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    results = reader.readtext(gray, detail=0)
    return results
def solve_expression(expr):
    try:
        expr=expr.replace("x","*").replace("X","*")
        return sympify(expr)
    except:
        return "Error"
    
#Upload Image function 
def upload_image():
    file_path=filedialog.askopenfilename()
    if file_path:
        img=Image.open(file_path)#open image
        img=img.resize((250,250))#image reszie
        img=ImageTk.PhotoImage(img)#convert Tkinter display
        #displays image in GUI
        panel.config(image=img)
        panel.image=img
        lines= extract_image(file_path)#calls OCR 
        
        output_text.delete("1.0",tk.END)        
        output_text.insert(tk.END, "Detected:\n")
        for line in lines:
            output_text.insert(tk.END,line+ "\n")#displays OCR text
        output_text.insert(tk.END, "\nResults:\n")
        
        for line in lines:
            result = solve_expression(line)
            output_text.insert(tk.END,f"{line}={result}\n")#calculates each line and shows result
            
#GUI Window
root=tk.Tk()
root.title("Handwritten Calculator")
root.geometry("500x600")

#Upload button
btn =tk.Button(root, text="Upload image",command=upload_image, font=("Arial",14))
btn.pack(pady=10)
