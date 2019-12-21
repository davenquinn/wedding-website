# This makefile implements a basic code compilation workflow
# for the static files used by this application. Browserify
# and coffeeify can both be installed using npm, and Compass
# (along with SASS) can be installed using Ruby Gems.

all: scripts styles

scripts: frontend/*.coffee | install
	node_modules/.bin/browserify -t coffeeify frontend/index.coffee > wedding_website/static/wedding.js

styles: frontend/wedding.scss frontend/styles/*.scss | install
	compass compile -e production

install:
	npm install browserify coffeeify
	-gem install compass susy breakpoint

freeze:
	pip install -r requirements.txt
	rm -rf build
	mkdir -p build
	# This doesn't quite work without errors
	-python freeze.py
	rm -rf build/wedding/static
	cp -r wedding_website/static build/wedding/static

serve:
	python -m http.server -d build

deploy:
	rclone copy --progress build/wedding davenquinn-spaces:davenquinn-wedding-website
