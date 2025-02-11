import pytest
import os
from PIL import Image
import task7


def test_create_png_image():
    filename = "PIL_test_image"
    file_1 = task7.create_png_400pixel_image(filename)
    file_2 = task7.create_png_800pixel_image(filename)
    file_3 = task7.create_png_1080p_pixel_image(filename)

    assert os.path.exists(file_1)
    assert os.path.exists(file_2)
    assert os.path.exists(file_3)

    with Image.open(file_1) as img:
        assert img.format == "PNG" # check that the image is a PNG
        assert img.size == (400, 400) # check that the image is 400x400 pixels
        assert img.mode == "RGB" # check that the image is in RGB mode

    with Image.open(file_2) as img:
        assert img.format == "PNG"
        assert img.size == (800, 800)
        assert img.mode == "RGB"

    with Image.open(file_3) as img:
        assert img.format == "PNG"
        assert img.size == (1920, 1080) # check that the image is 1920x1080 pixels
        assert img.mode == "RGB"
        assert img.getpixel((800, 1000)) == (175, 70, 0) # check that the bg color is orange
