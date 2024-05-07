import tkinter as tk
from tkinter import ttk, colorchooser, filedialog,Scale,HORIZONTAL
from PIL import Image, ImageTk, ImageFilter, ImageEnhance,ImageDraw,ImageOps

pen_color = "black"
pen_size = 5
current_image = None

def display_image(img):
    global canvas_image
    canvas_image = ImageTk.PhotoImage(img)
    canvas.config(width=canvas_image.width(), height=canvas_image.height())
    canvas.create_image(0, 0, image=canvas_image, anchor="nw")

def draw(event):
    global draw_object
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')
    draw_object.ellipse([x1, y1, x2, y2], fill=pen_color)

def choose_color():
    color = colorchooser.askcolor(title="Choose Color")
    if color:
        global pen_color
        pen_color = color[1]

def change_brush_size(size):
    global pen_size
    pen_size = int(float(size))

def clear_canvas():
    global current_image
    canvas.delete("all")
    display_image(current_image)

def apply_filter(filter):
    global current_image,original_image
    if filter == "None":
        display_image(original_image)
    if filter == "Black and White":
        current_image = ImageOps.grayscale(original_image)
        display_image(current_image)
    elif filter == "Blur":
        current_image = original_image.filter(ImageFilter.BLUR)
        display_image(current_image)
    elif filter == "Sharpen":
        current_image = original_image.filter(ImageFilter.SHARPEN)
        display_image(current_image)
    elif filter == "Smooth":
        current_image = original_image.filter(ImageFilter.SMOOTH)
        display_image(current_image)
    elif filter == "Emboss":
        current_image = original_image.filter(ImageFilter.EMBOSS)   
        display_image(current_image)
    elif filter == "Contour":
        current_image = original_image.filter(ImageFilter.CONTOUR)  
        display_image(current_image)
    elif filter == "Detail":
        current_image = original_image.filter(ImageFilter.DETAIL)
        display_image(current_image)
    elif filter == "UnsharpMask":
        current_image = original_image.filter(ImageFilter.UnsharpMask) 
        display_image(current_image)

def rotate_image():
    global current_image
    if current_image:
        current_image = current_image.rotate(90)
        display_image(current_image)

def adjust_brightness(brightness):
    global current_image,original_image
    if current_image:
        brightness = float(brightness)
        enhancer = ImageEnhance.Brightness(original_image)
        current_image = enhancer.enhance(brightness)
        display_image(current_image)

def adjust_contrast(contrast):
    global current_image,original_image
    if current_image:
        contrast = float(contrast)
        enhancer = ImageEnhance.Contrast(original_image)
        current_image = enhancer.enhance(contrast)
        display_image(current_image)

def adjust_color(color):
    global current_image,original_image
    if current_image:
        color = float(color)
        enhancer = ImageEnhance.Color(original_image)
        current_image = enhancer.enhance(color)
        display_image(current_image)

def flip_image():
    global current_image
    if current_image:
        current_image = current_image.transpose(Image.FLIP_LEFT_RIGHT)
        display_image(current_image)

def save_image():
    global current_image, drawing_image
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG Files", "*.png"),
                                                        ("JPEG Files", "*.jpg;*.jpeg"),
                                                        ("TIFF Files", "*.tiff;*.tif")])
    if save_path:
        if drawing_image.mode != "RGBA":
            drawing_image = drawing_image.convert("RGBA")
        combined_image = Image.alpha_composite(current_image.convert("RGBA"), drawing_image)
        combined_image.save(save_path)


def import_image():
    global current_image, original_image, drawing_image, draw_object
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp *.gif")])
    if file_path:
        original_image = Image.open(file_path)
        original_image = original_image.resize((600, 400), Image.LANCZOS)
        current_image = original_image.resize((600, 400), Image.LANCZOS)
        drawing_image = Image.new("RGBA", current_image.size) 
        draw_object = ImageDraw.Draw(drawing_image)
        display_image(current_image)


root = tk.Tk()
root.title("Image Editor")
root.geometry("1000x700")
root.state('zoomed')

options_frame = tk.Frame(root, width=200, bg='white')
options_frame.pack(side="left", fill="y")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack(padx=10, pady=10)

import_button = tk.Button(options_frame, text="Import Image", command=import_image)
import_button.pack(pady=10)

brush_label=tk.Label(options_frame,text="Select Brush Size",bg="white")
brush_label.pack()
brush_size_scale = ttk.Scale(options_frame, from_=1, to=20, orient=tk.HORIZONTAL,command=change_brush_size, length=150)
brush_size_scale.set(pen_size)
brush_size_scale.pack(pady=10)

color_button = tk.Button(options_frame, text="Choose Color", command=choose_color)
color_button.pack(pady=5)

clear_button=tk.Button(options_frame,text="Clear",command=clear_canvas,bg="#FF9797")
clear_button.pack(pady=10)

filter_label=tk.Label(options_frame,text="Select Filter",bg="white")
filter_label.pack()
filter_combobox = ttk.Combobox(options_frame, values=["None","Black and White", "Blur","Emboss", "Sharpen", "Smooth", "Contour", "Detail", "UnsharpMask"])
filter_combobox.pack()
filter_combobox.bind("<<ComboboxSelected>>",lambda event:apply_filter(filter_combobox.get()))

rotate_button = tk.Button(options_frame, text="Rotate Image", command=rotate_image)
rotate_button.pack(pady=5)

flip_button = tk.Button(options_frame, text="Flip Image", command=flip_image)
flip_button.pack(pady=5)

brightnessSlider = Scale(options_frame, label="Brightness", from_=0, to=2, orient=HORIZONTAL, length=200,resolution=0.1, command=adjust_brightness, bg="cyan")
brightnessSlider.set(1)
brightnessSlider.configure(font=('consolas',10,'bold'),foreground='black')
brightnessSlider.pack(pady=10)

contrastSlider = Scale(options_frame, label="Contrast", from_=0, to=2, orient=HORIZONTAL, length=200,command=adjust_contrast, resolution=0.1, bg="cyan")
contrastSlider.set(1)
contrastSlider.configure(font=('consolas',10,'bold'),foreground='black')
contrastSlider.pack(pady=10)

ColorSlider = Scale(options_frame, label="Color", from_=0, to=2, orient=HORIZONTAL, length=200,command=adjust_color, resolution=0.1, bg="cyan")
ColorSlider.set(1)
ColorSlider.configure(font=('consolas',10,'bold'),foreground='black')
ColorSlider.pack(pady=10)

save_button = tk.Button(options_frame, text="Save Image", command=save_image,bg="orange")
save_button.pack(pady=70)

canvas.bind("<B1-Motion>",draw)
root.mainloop()
