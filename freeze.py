from flask_frozen import Freezer
from test_app import app

freezer = Freezer(app, with_static_files=False)

if __name__ == '__main__':
    freezer.freeze()
