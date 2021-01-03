# Copyright 2020 Michael Penhallegon 
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0

run-dev:
	export FLASK_APP=homeapp
	export FLASK_ENV=development
	flask run

build:
	source ./venv39/bin/activate
	pip install -r requirements.txt
	python setup.py bdist_wheel
