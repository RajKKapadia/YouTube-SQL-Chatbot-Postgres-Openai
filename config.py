import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GPT_MODEL = os.getenv('GPT_MODEL')

POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_DB_NAME = os.getenv('POSTGRES_DB_NAME')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')


cwd = os.getcwd()

DEFINITION_DIR = 'data_definition'

os.makedirs(
    os.path.join(
        cwd,
        DEFINITION_DIR
    ),
    exist_ok=True
)

ERROR_MESSAGE = 'We are facing an issue at this moment, please try after sometime.'
