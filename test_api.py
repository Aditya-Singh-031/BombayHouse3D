import requests
import os

# The filename of the floor plan image you downloaded
IMAGE_PATH = 'first_floor.png'

# The URL of the running API server
API_URL = 'http://127.0.0.1:5000/predict'

def test_floorplan_api(image_path):
    """Sends a floor plan image to the API and prints the response."""
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at '{image_path}'")
        return

    try:
        # Open the image file in binary read mode
        with open(image_path, 'rb') as f:
            files = {'file': (image_path, f, 'image/jpeg')}

            print(f"Sending '{image_path}' to {API_URL}...")
            response = requests.post(API_URL, files=files)

            # Raise an exception if the request was unsuccessful
            response.raise_for_status() 

            print("\nSuccess! API Response:")
            # The response is likely JSON, so we can try to print it as such
            print(response.json())

    except requests.exceptions.RequestException as e:
        print(f"\nAn error occurred: {e}")
    except Exception as e:
        print(f"\nA general error occurred: {e}")

if __name__ == '__main__':
    test_floorplan_api(IMAGE_PATH)