# pip install playwright
# pip install pytest-playwright
# python -m playwright install


from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    assert page.title() == 'Example Domain'
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
