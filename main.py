from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    
    try:
        # Navigate to a website
        driver.get("https://www.google.com")
        
        # Wait for the search box to be present
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        
        # Enter search term and submit
        search_box.send_keys("Selenium with Python")
        search_box.send_keys(Keys.RETURN)
        
        # Wait for results
        time.sleep(3)
        
        # Get search results
        search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
        
        # Print the titles of search results
        for result in search_results:
            try:
                title = result.find_element(By.TAG_NAME, "h3").text
                print(title)
            except:
                continue
                
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
