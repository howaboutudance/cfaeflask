# Copyright 2020-2021 Michael Penhallegon 
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0

from flask import Flask
from flask.templating import render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("base.html")