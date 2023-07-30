from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask

db = SQLAlchemy()
cors = CORS(support_credentials=True)
app = Flask(__name__)
