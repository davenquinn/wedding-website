This is the wedding website for Daven Quinn and Beth Sams.
Our marriage on October 14, 2014 was a great
success, which is at least 2% attributable to the code
right here.

This package is a simple `Flask` blueprint that
provides a static site plus RSVP functionality (with
emails notifications). There's also a custom Google Maps
style in our wedding colors. I implemented it as part of
[my website](http://davenquinn.com) but have lately
pulled it out into a modular component. A frozen version
is available at http://davenquinn.com/wedding.

The website includes a basic testing server (`test-app.py`).
The package can be used as a blueprint, either at the root
of a website or as part of a larger `Flask` app.

Serving should be accomplished via a performant web + WSGI
server stack (e.g. `nginx` + `gunicorn`) but
I'll leave that to you!

The blueprint is a standard Python package and installation
is best accomplished via `pip`:

    > pip install git+https://github.com/davenquinn/wedding-website.git

This was a fun project (both building the site and packaging it up as a standalone app)! I'd encourage
you to fork the code and make it your own. It provides
a basic starting point for a wedding or any sort of
simple site with a contact form.
