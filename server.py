from flask_blog import app

# server.py を実行された時に(python server.go)
# 実行される処理を記述することができます。
if __name__ == '__main__':
    app.run(host='0.0.0.0')
