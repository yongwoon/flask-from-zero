from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask application 全体を作成
app = Flask(__name__)

# config file の有効化
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

import flask_blog.views
