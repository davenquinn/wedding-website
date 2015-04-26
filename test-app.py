#! /usr/bin/env python

from flask import Flask
from wedding_website import wedding

class TestConfig(object):
    """
    Contains dummy values for the configuration
    variables that need to be set for maps and
    RSVP functionality to work.
    """

    # If you want to monitor Google Maps
    # usage, set a key! Not required though...
    GOOGLE_MAPS_KEY = None

    # Setup values for Flask-Mail
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME = 'you@gmail.com'
    MAIL_PASSWORD = '*************'
    DEFAULT_MAIL_SENDER = MAIL_USERNAME

    # If desired, set to a directory to
    # enable saving of responses locally
    # as plain text (useful as a backstop
    # for weird email issues).
    STORAGE_BASE = None

app = Flask(__name__)
app.config.from_object(TestConfig)
app.register_blueprint(wedding, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)
