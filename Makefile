default: buildout test

buildout: bin/buildout
	bin/buildout -c buildout.cfg -N -t 3

travis: bin/buildout
	bin/buildout -c travis.cfg -N -t 10

test:
	bin/test ploneintranet.core
	bin/flake8 src/ploneintranet

bin/buildout: bin/python buildout-cache/downloads
	bin/python bootstrap.py -v 2.2.1

bin/python:
	virtualenv --clear --no-site-packages --setuptools --python=python2.7 .

buildout-cache/downloads:
	[ -d buildout-cache ] || mkdir -p buildout-cache/downloads

clean:
	rm -rf bin/* .installed.cfg parts/download


# this assumes you're in a ploneintranet.suite buildout
GENERATED=../ploneintranet.theme/src/ploneintranet/theme/static/generated
TARGET=src/ploneintranet/core/browser/

sync:
	rsync -av --exclude colours.css $(GENERATED)/style/ $(TARGET)/stylesheets/
	cat $(GENERATED)/bundles/ploneintranet.min.js > $(TARGET)/javascripts/ploneintranet.min.js

