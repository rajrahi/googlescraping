from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch the browser in non-headless mode for debugging
    browser = p.chromium.launch(headless=False)  # Set headless=False to see the browser
    page = browser.new_page()

    # Go to the Google search page
    page.goto("https://www.google.com")

    # Wait for page load and check what's happening
    print("Waiting for search input...")
    try:
        page.wait_for_selector('input[name="q"]', state='visible', timeout=60000)
        print("The search input is visible!")
    except Exception as e:
        print(f"Error: {str(e)}")

    # Close the browser
    browser.close()