import os
import sys
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Response
from wtforms import Form, StringField, FieldList, FormField
from wtforms_components import read_only
import logging
from pythonjsonlogger import jsonlogger


app = Flask(__name__)
app.secret_key = "flask_table"



if __name__ == "__main__":
    app.run(debug=True, threaded=True)