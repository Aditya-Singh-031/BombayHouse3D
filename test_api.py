import requests
import os
from PIL import Image
import io  # Required for in-memory file handling

# The path to your original PNG file
IMAGE_PATH = 'first_floor.png' 

# The URL of the running API server
API_URL = 'http://127.0.0.1:5000/' 

def test_floorplan_api(image_path):
    """
    Opens an image, converts it to RGB (like a JPG), 
    and sends it to the API.
    """
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at '{image_path}'")
        return

    try:
        print(f"Opening and converting '{image_path}' to RGB format...")
        
        # 1. Open the image using Pillow
        img = Image.open(image_path)
        
        # 2. Convert the image to RGB, stripping the alpha channel
        rgb_img = img.convert('RGB')
        
        # 3. Create an in-memory binary stream (a virtual file)
        byte_buffer = io.BytesIO()
        
        # 4. Save the converted image into the buffer in JPEG format
        rgb_img.save(byte_buffer, format='JPEG')
        
        # 5. Rewind the buffer to the beginning
        byte_buffer.seek(0)

        # 6. Prepare the file for the POST request from the in-memory buffer
        # We give it a new name and specify the correct content type
        files = {'image': ('converted_image.jpg', byte_buffer, 'image/jpeg')} 
        
        print(f"Sending converted image to {API_URL}...")
        response = requests.post(API_URL, files=files)
        
        response.raise_for_status() 
        
        print("\nSuccess! API Response:")
        print(response.json())

    except requests.exceptions.RequestException as e:
        print(f"\nAn error occurred while making the request: {e}")
    except Exception as e:
        print(f"\nA general error occurred: {e}")

if __name__ == '__main__':
    test_floorplan_api(IMAGE_PATH)