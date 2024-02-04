from PIL import Image
import struct

def read_binary_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            # Read the binary data from the file
            binary_data = file.read()

            # Check if the length of the binary data is a multiple of 3
            if len(binary_data) % 3 != 0:
                print("Invalid binary file format. Each RGB tuple should be represented by 3 bytes.")
                return None

            # Interpret each set of 3 bytes as an RGB tuple
            rgb_tuples = [struct.unpack('BBB', binary_data[i:i+3]) for i in range(0, len(binary_data), 3)]

            return rgb_tuples

    except Exception as e:
        print(f"Error: {e}")
        return None
    

def create_image(pixel_array, width, height, output_file):
    array_nb_pixels = len(pixel_array)

    def get_pixel(position):
        return pixel_array[position] if position < array_nb_pixels else (0,0,0)
    
    try:
        # Create a new image with the specified width and height
        image = Image.new("RGB", (width, height))

        # Put the RGB values into the image
        for y in range(height):
            for x in range(width):
                pixel = get_pixel(y * width + x)
                image.putpixel((x, y), pixel)

        # Save the image to the specified output file
        image.save(output_file)
        print(f"Image created and saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'path/to/your/output_image.jpg' with the desired output file path
    input_file = "result.mtx"
    output_file = "output_image.jpg"

    #returns an array of RGB tuples
    pixel_array = read_binary_file(input_file)

    # Specify the width and height of the image
    width = 500
    height = 500

    create_image(pixel_array, width, height, output_file)
