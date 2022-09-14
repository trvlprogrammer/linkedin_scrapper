from flask import Blueprint

bp = Blueprint('api', __name__)

from apps.api import linkedin_scraper, utils