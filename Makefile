run-dev:
	export FLASK_APP=homeapp
	export FLASK_ENV=development
	flask run

build:
	source ./venv39/bin/activate
	pip install -r requirements.txt
	python setup.py bdist_wheel
