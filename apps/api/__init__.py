from flask import Blueprint

bp = Blueprint('api', __name__)

from apps.api import auth, linkedin_scraper