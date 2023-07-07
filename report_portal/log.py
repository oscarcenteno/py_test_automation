import logging
from reportportal_client import RPLogger
import sys


def log_txt(message, file_name, content):
    log_info(message, file_name, content, "application/octet-stream")


def log_png(message, file_name, full_file_path):
    with open(full_file_path, "rb") as image_file:
        content = image_file.read()
    log_png_content(message, file_name, content)


def log_png_content(message, file_name, content):
    log_info(message, file_name, content, "image/png")


def log_info(message, file_name, content, mime):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)

    if report_portal_is_enabled():
        logger.info(
            message,
            attachment={  # type: ignore
                "name": file_name,
                "data": content,
                "mime": mime
            },
        )

def report_portal_is_enabled():
    return "--reportportal" in sys.argv
