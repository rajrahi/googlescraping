import requests
import os

def download_audio(url, output_path='audio.mp3'):
    """
    Download audio from a URL and save it to the specified path

    Args:
        url (str): URL of the audio file to download
        output_path (str): Path where the audio file will be saved

    Returns:
        bool: True if download successful, False otherwise
    """
    try:
        # Send GET request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Write the content to file
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return True

    except requests.exceptions.RequestException as e:
        print(f"Error downloading audio (Request Error): {str(e)}")
        return False
    except Exception as e:
        print(f"Error downloading audio (Other Error): {str(e)}")
        return False


url = "https://www.google.com/recaptcha/api2/payload?p=06AFcWeA5P53m8PQnBJz-UT1Wrx96r3ovAjOsG0o_6tRjHxe0hzQy1h0BChJdLWiSLq-WTGvHD1lUwrSKm4tfEDl3tFvWNCmlUZ9asku2SVqqAnuaRfQGLncwTD16a1myDZcwHYbh16VGd2YRQfyIo2g22_MC3joSVMuERnutDMQDwMWh6Xl5kyccOfdq-xMotmVZTQKWx7_35&k=6LfwuyUTAAAAAOAmoS0fdqijC2PbbdH4kjq62Y1b"

download_audio(url)