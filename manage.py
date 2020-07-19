from flask_script import Manager
# manage.py は script のため、実行時には application が作成されていない状態にあります。
# この場合は、create_app 関数を用いて、application を作成して script を実行する必要があります。
from flask_blog import create_app
from flask_blog.scripts.db import InitDB

if __name__ == "__main__":
    manager = Manager(create_app)
    # 作成した InitDB() module を init_db という名前で実行できるようにしています。
    manager.add_command('init_db', InitDB())
    manager.add_command('drop_db', DropDB())
    manager.run()
