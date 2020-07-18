from flask import Flask

# Flask application 全体を作成
app = Flask(__name__)

# config file の有効化
app.config.from_object('flask_blog.config')

from flask_blog.views import views, entries
