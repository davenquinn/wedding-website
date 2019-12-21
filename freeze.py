from flask_frozen import Freezer
from test_app import app

app.config.update(FREEZER_RELATIVE_URLS=True, FREEZER_IGNORE_404_NOT_FOUND=True)

freezer = Freezer(app, with_static_files=False)

if __name__ == '__main__':
    freezer.freeze()
