VERSION=`cat VERSION`

# Test

.PHONY: test
test:	## Execute tests suites
	python3 -m unittest discover -v


.PHONY: cover
cover:	## Generate coverage information
	coverage3 run --omit=*.venv*,main.py --source=. -m unittest discover

.PHONY: coverage-html
coverage-html:	cover ## HTML report
	coverage3 html --directory=.cover --omit=*.venv*,main.py

.PHONY: coveralls
coveralls:	## Coverage to coveralls report
	coveralls --data_file=.coverage --coveralls_yaml=.coveralls.yml --base_dir=.

# Docker container images

.PHONY: docker
docker: docker-build docker-publish

.PHONY: docker-build
docker-build:	## Builds container and tag resulting image
	docker build --force-rm --tag vtalks/twitter-worker .
	docker tag vtalks/twitter-worker vtalks/twitter-worker:$(VERSION)

.PHONY: docker-publish
docker-publish:	## Publishes container images
	docker push vtalks/twitter-worker:$(VERSION)
	docker push vtalks/twitter-worker:latest

.PHONY: help
help:	## Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.DEFAULT_GOAL: help