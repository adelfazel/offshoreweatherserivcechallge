init:
	pip install -r requirements.txt

test:
	pytest

run:
	python3 src/main.py

.PHONY: init test run