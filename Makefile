# This makefile implements a basic code compilation workflow
# for the static files used by this application. Browserify
# and coffeeify can both be installed using npm, and Compass
# (along with SASS) can be installed using Ruby Gems.

all: scripts styles

scripts: frontend/*.coffee
	browserify -t coffeeify frontend/index.coffee > static/wedding.js

styles: frontend/wedding.scss frontend/styles/*.scss
	compass compile -e production

install:
	npm install -g browserify
	npm install coffeeify
	gem install compass susy breakpoint
