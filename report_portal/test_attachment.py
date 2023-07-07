import pytest

from .log import log_png, log_png_content, log_txt


@pytest.mark.rp
def test_log_text_file():
    log_txt("Case1. Step1", "free_memory.txt", "free_memory")


@pytest.mark.rp
def test_log_image_content():
    with open("report_portal/example.png", "rb") as image_file:
        content = image_file.read()
    log_png_content("www.example.com", "example.png", content)


@pytest.mark.rp
def test_log_image_file():
    log_png("www.example.com", "example.png", "report_portal/example.png")
