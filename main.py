import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


# Create a function to add the watermark to the image
def add_watermark(image_path, text, pos):
    # Open the image
    image = Image.open(image_path)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Set the font and text color for the watermark
    font = ImageFont.truetype("arial.ttf", 36)
    text_color = (255, 255, 255)

    # Get the size of the text
    text_size = draw.textsize(text, font)

    # Calculate the position of the watermark
    if pos == "top-left":
        position = (0, 0)
    elif pos == "top-right":
        position = (image.width - text_size[0], 0)
    elif pos == "bottom-left":
        position = (0, image.height - text_size[1])
    elif pos == "bottom-right":
        position = (image.width - text_size[0], image.height - text_size[1])
    else:
        position = (image.width // 2 - text_size[0] // 2, image.height // 2 - text_size[1] // 2)

    # Add the watermark to the image
    draw.text(position, text, font=font, fill=text_color)

    # Save the watermarked image
    watermarked_image_path = f"{image_path[:-4]}_watermarked{image_path[-4:]}"
    image.save(watermarked_image_path)

    # Show a message box when the watermarking is finished
    tk.messagebox.showinfo("Watermarking", "Watermarking finished!")


# Create a function to select an image file
def select_image_file():
    image_path = filedialog.askopenfilename(filetypes=(("Image Files", "*.jpg;*.jpeg;*.png;*.bmp"),))
    image_path_entry.delete(0, tk.END)
    image_path_entry.insert(0, image_path)


# Create a function to watermark the image
def watermark_image():
    # Get the image path, watermark text, and watermark position from the entry fields
    image_path = image_path_entry.get()
    text = watermark_text_entry.get()
    pos = watermark_position_var.get()

    # Call the add_watermark function to add the watermark to the image
    add_watermark(image_path, text, pos)


# Create the main window
root = tk.Tk()
root.title("Image Watermarking App")

# Create a label and entry field for the image path
image_path_label = tk.Label(root, text="Image Path:")
image_path_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")
image_path_entry = tk.Entry(root)
image_path_entry.grid(row=0, column=1, padx=5, pady=5, sticky="WE")
select_image_file_button = tk.Button(root, text="Select", command=select_image_file)
select_image_file_button.grid(row=0, column=2, padx=5, pady=5)

# Create a label and entry field for the watermark text
watermark_text_label = tk.Label(root, text="Watermark Text:")
watermark_text_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")
watermark_text_entry = tk.Entry(root)
watermark_text_entry.grid(row=1, column=1, padx=5, pady=5, sticky="WE")

# Create a label and radio buttons for the watermark position
watermark_position_label = tk.Label(root, text="Watermark Position:")
watermark_position_label.grid(row=2, column=0, padx=5, pady=5, sticky="W")
watermark_position_var = tk.StringVar(value="center")

positions = [("Top Left", "top-left", "W"),
             ("Top Right", "top-right", "E"),
             ("Bottom Left", "bottom-left", "W"),
             ("Bottom Right", "bottom-right", "E"),
             ("Center", "center", "WE")]

for i, (position_text, position_value, position_sticky) in enumerate(positions):
    position_radio = tk.Radiobutton(root, text=position_text, variable=watermark_position_var, value=position_value)
    position_radio.grid(row=3+i, column=1, padx=5, pady=5, sticky=position_sticky)

# Create a button to watermark the image
watermark_button = tk.Button(root, text="Watermark Image", command=watermark_image)
watermark_button.grid(row=8, column=0, columnspan=3, padx=5, pady=5, sticky="WE")

# Run the main event loop
root.mainloop()
