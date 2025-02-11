from PIL import Image, ImageDraw
# PIL (Pillow (worst package name ever)) is the Python Imaging Library,
#   provides image processing capabilities

# Following functions will generate PNG images with different sizes and text
# Image1: 400x400 pixels with text "PNG Generator", background color: (0, 210, 100) (dark green)
# Image2: 800x800 pixels with text "PNG Generator", background color: (0, 15, 200) (dark blue)
# Image3: 1920x1080 pixels with text "PNG Generator", background color: (175, 70, 0) (orange)

def create_png_400pixel_image(filename, text="PNG Generator"):
    # Create a new image with the given size and color, RGB mode is usually the default
    nu_image = Image.new('RGB', (400, 400), color=(0, 210, 100))
    # draw is PIL's ImageDraw object
    draw = ImageDraw.Draw(nu_image)
    # draw text on the image at the given position
    draw.text((150, 190), text, fill=(255, 0, 15), stroke_width=.4)
    filename = filename + "_400px.png" # append filename
    nu_image.save(filename, "PNG") # save the image as PNG
    return filename # return the new filename to the caller

def create_png_800pixel_image(filename, text="PNG Generator"):
    nu_image = Image.new('RGB', (800, 800), color=(0, 15, 200)) # 800x800 pixels, dark blue background
    draw = ImageDraw.Draw(nu_image)
    draw.text((300, 380), text, fill=(255, 0, 15), stroke_width=.4)
    filename = filename + "_800px.png"
    nu_image.save(filename, "PNG")
    return filename

def create_png_1080p_pixel_image(filename, text="PNG Generator"):
    nu_image = Image.new('RGB', (1920, 1080), color=(175, 70, 0)) # 1920x1080, orange background
    draw = ImageDraw.Draw(nu_image)
    draw.text((300, 380), text, fill=(255, 222, 222), stroke_width=.4)
    filename = filename + "_1080p.png"
    nu_image.save(filename, "PNG")
    return filename



create_png_1080p_pixel_image("oj_test_image")