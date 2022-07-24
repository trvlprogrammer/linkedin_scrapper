
import os
from dotenv import load_dotenv
from datetime import datetime,timedelta,timezone

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES'))) 
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(days=int(os.environ.get('JWT_REFRESH_TOKEN_EXPIRES'))) 
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=int(os.environ.get('ACCESS_EXPIRES')))
    SCRAPER_USERNAME = os.environ.get('SCRAPER_USERNAME')
    SCRAPER_PASSWORD = os.environ.get('SCRAPER_PASSWORD')
    USER_AGENT = os.environ.get('USER_AGENT')