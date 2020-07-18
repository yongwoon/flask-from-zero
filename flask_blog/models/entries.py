
from flask_blog import db
from datetime import datetime


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()

    def __repr__(self):
        # 実際に記事 model が参照されたときの console での 出力形式を記載しています。
        return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)
