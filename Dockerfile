# Copyright 2020-2021 Michael Penhallegon 
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0

FROM python:3.7 AS compile-image


RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY cfaeflask/. ./cfaeflask
COPY README.md .
COPY setup.py .
RUN python setup.py bdist_wheel

FROM python:3.7-slim AS build-image
COPY --from=compile-image /opt/venv/ /opt/venv
COPY --from=compile-image /app/dist /dist

# Make sure scripts in .local are usable:
ENV PATH=/opt/venv/bin:$PATH
RUN pip install dist/cfaeflask-*.whl
ENV FLASK_APP=cfaeflask
CMD gunicorn cfaeflask:app -b 127.0.0.1:5000