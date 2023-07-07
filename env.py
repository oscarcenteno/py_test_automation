# https://pypi.org/project/python-dotenv/

from dotenv import load_dotenv
import os

load_dotenv()

def get(PARAM):
    value = os.getenv(PARAM)
    print(f'Getting Environment variable {PARAM}={value}')
    return value
