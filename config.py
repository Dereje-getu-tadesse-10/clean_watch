import os
import psycopg2
from dotenv import load_dotenv, dotenv_values

load_dotenv('.flaskenv')

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)
