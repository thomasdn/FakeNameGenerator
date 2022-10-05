#setup: requirements.txt
#	pip install -r requirements

clean:
	rm -rf __pycache__
	rm -rf venv

venv: requirements.txt
	python3 -m venv venv
	./venv/bin/pip3 install -r requirements.txt

.PHONY: clean
