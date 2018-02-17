VERSION=`cat VERSION`

default: help

# Test

.PHONY: test
test:	## Execute tests suites
	python3 test_worker.py

.PHONY: cover
cover:	## Generate coverage information
	coverage3 run test_worker.py

.PHONY: coverage-html
coverage-html:	## HTML report
	coverage3 html --omit="*.venv*" -d .cover

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