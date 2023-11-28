from pydantic import BaseModel
from flask import Flask, request

# views
from views import scrapers as scraper_view
from views import openai as openai_view

app = Flask(__name__)
app.register_blueprint(scraper_view.router)
app.register_blueprint(openai_view.router)
