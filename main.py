import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import requests
from selenium.webdriver.common.action_chains import ActionChains
import speech_recognition as sr
import urllib.request
import os
from pydub import AudioSegment
import undetected_chromedriver as uc  # Import undetected-chromedriver


def solve_recaptcha(driver):
    """Attempts to solve a reCAPTCHA challenge, handling both checkbox and audio challenges."""

    time.sleep(2)
    # Wait for the reCAPTCHA iframe to be present
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
    )
    driver.switch_to.frame(iframe)

    # Click the "I'm not a robot" checkbox
    checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "recaptcha-checkbox-border"))
    )
    checkbox.click()
    time.sleep(2)
    # Switch to the reCAPTCHA challenge iframe
    driver.switch_to.default_content()
    iframe_challenge = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@title, 'recaptcha challenge')]"))
    )
    driver.switch_to.frame(iframe_challenge)

    # Click the audio challenge button
    audio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "recaptcha-audio-button"))
    )
    audio_button.click()
    time.sleep(2)

    # Get the audio source
    audio_source = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "audio-source"))
    )
    audio_href = audio_source.get_attribute('src')

    # Download and save the audio file
    urllib.request.urlretrieve(audio_href, "audio.mp3")

    # Convert mp3 to wav
    audio = AudioSegment.from_mp3("audio.mp3")
    audio.export("audio.wav", format="wav")

    # Use speech recognition to get text
    r = sr.Recognizer()
    with sr.AudioFile('audio.wav') as source:
        audio_data = r.record(source)
    try:
        text = r.recognize_google(audio_data)
        print("Recognized Text:", text)

        # Enter the recognized text
        answer_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "audio-response"))
        )
        answer_input.send_keys(text)
        time.sleep(1) # Give time for the text to be entered

        # Click verify button (you might need to adjust the selector)
        verify_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "recaptcha-verify-button"))
        )
        verify_button.click()
        time.sleep(5) # Give time for verification

        # Switch back to default content
        driver.switch_to.default_content()
        return True

    except sr.UnknownValueError:
        print("Could not understand audio")
        return False
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return False
    finally:
        # Clean up temporary files
        if os.path.exists("audio.mp3"):
            os.remove("audio.mp3")
        if os.path.exists("audio.wav"):
            os.remove("audio.wav")
        driver.switch_to.default_content() # Ensure we are back in the main frame


def main():
    try:
        # Use undetected-chromedriver
        driver = uc.Chrome(options=Options())

    
     
        
        driver.get("https://www.google.com/")
        search_box = driver.find_element(By.NAME, "q")
        time.sleep(2)
        for char in "emp monitor":
            search_box.send_keys(char)
            time.sleep(random.uniform(0.1, 0.8))
        time.sleep(random.uniform(0.1, 0.8))
        search_box.send_keys(Keys.ARROW_DOWN)
        time.sleep(random.uniform(0.1, 0.8))
        search_box.send_keys(Keys.RETURN)

        time.sleep(5) # Give time for potential reCAPTCHA to appear

        try:
            # Attempt to solve reCAPTCHA if present
            solve_recaptcha(driver)
        except Exception as e:
            print(f"Error during reCAPTCHA solving: {e}")
            pass

        # Wait for search results to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "search")))

        # Get the page source
        page_source = driver.page_source

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        print(soup.prettify())


    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()