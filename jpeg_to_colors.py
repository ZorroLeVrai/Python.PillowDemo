from PIL import Image

def jpeg_to_pixel_array(file_path):
    try:
        # Open the image using Pillow
        image = Image.open(file_path)

        # Get the width and height of the image
        width, height = image.size

        # Get the RGB values for each pixel
        pixel_array = []
        for y in range(height):
            for x in range(width):
                pixel = image.getpixel((x, y))
                pixel_array.append(pixel)

        return pixel_array

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    file_path = './dog1.jpg'

    pixel_array = jpeg_to_pixel_array(file_path)

    if pixel_array is not None:
        with open("result.mtx", "wb") as binary_file:
            for pixel in pixel_array:
                binary_file.write(bytes(pixel))
