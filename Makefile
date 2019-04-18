
.PHONY: install
install:
	sudo python setup.py install

.PHONY: clean
clean:
	rm -rf build/ dist/ *.png *.pdf *.wav unittest/*.png unittest/*.pdf unittest/test.wav

.PHONY: register
register:
	python setup.py register

.PHONY: upload
upload:
	python setup.py sdist upload

.PHONY: tag
tag:
	git tag $$(python setup.py --version)

.PHONY: test
test:
	nosetests unittest/

.PHONY: lint
lint:
	pylint3 mingus/ 

.PHONY: release
release: clean register upload tag
