from report_portal.log import log_png_content


def log_screenshot(driver):
    screenshot_as_png = driver.get_screenshot_as_png()
    title = f'Screenshot for "{driver.title}" ({driver.current_url})'
    log_png_content(title, "screenshot.png", screenshot_as_png)
