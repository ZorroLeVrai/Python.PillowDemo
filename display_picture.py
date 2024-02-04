from PIL import Image
import sys

def display_image(file_path):
    try:
        image = Image.open(file_path)
        image.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python display_image.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    display_image(file_path)
