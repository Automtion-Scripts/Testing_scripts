"""
Wikipedia search automation (Python + Selenium)

Requirements:
  pip install selenium
  Optionally: pip install webdriver-manager

Two driver options included:
  - OPTION A: require chromedriver on PATH
  - OPTION B: uses webdriver-manager to auto-download chromedriver

Usage:
  - Change SEARCH_QUERY or call search_wikipedia("your query")
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Optional: uncomment to use webdriver_manager (auto-download chromedriver)
# from webdriver_manager.chrome import ChromeDriverManager

def create_driver(use_webdriver_manager=False, headless=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")  # run headless if desired
        options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    # OPTION A: chromedriver in PATH
    if not use_webdriver_manager:
        driver = webdriver.Chrome(options=options)
    else:
        # OPTION B: webdriver-manager (uncomment import above if using)
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    return driver

def search_wikipedia(search_query, driver=None, timeout=10):
    """Search Wikipedia for search_query and return the article title (first heading)."""
    close_driver_when_done = False
    if driver is None:
        driver = create_driver(use_webdriver_manager=False, headless=False)
        close_driver_when_done = True

    wait = WebDriverWait(driver, timeout)
    try:
        # 1) Open Wikipedia home page
        driver.get("https://en.wikipedia.org/")

        # 2) Wait for the search input to be visible (expected condition)
        search_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "search"))
        )

        # 3) Type the query and press ENTER
        search_input.clear()
        search_input.send_keys(search_query)
        search_input.send_keys(Keys.ENTER)

        # 4) Wait until the page title contains the search term (or an article heading is visible)
        # This handles both direct article pages and search-results pages.
        wait.until(EC.or_(
            EC.title_contains(search_query),
            EC.visibility_of_element_located((By.ID, "firstHeading"))
        ))

        # 5) Get the first heading on the resulting page (article title or search results heading)
        heading_el = driver.find_element(By.ID, "firstHeading")
        article_title = heading_el.text.strip()
        print(f"Search query: {search_query!r}")
        print(f"Top heading on page: {article_title!r}")

        # Optional: print the first paragraph if available
        try:
            first_paragraph = driver.find_element(By.CSS_SELECTOR, "div.mw-parser-output > p")
            p_text = first_paragraph.text.strip()
            if p_text:
                print("\nFirst paragraph (snippet):")
                print(p_text[:800])  # print up to 800 chars
        except Exception:
            pass

        return article_title

    finally:
        if close_driver_when_done:
            # keep browser open for a short time so you can see it (remove time.sleep in CI)
            time.sleep(1)
            driver.quit()

if __name__ == "__main__":
    # Example usage
    SEARCH_QUERY = "Selenium (software)"
    search_wikipedia(SEARCH_QUERY)
