# title           :A Flask demo project
# description     :This is a demo project. It utilizes tool including Flask, Docker, Javascript, Datatables, Bootstrap,
#                 CSS and etc..
# author          :Yi Fu
# date            :20190411
# version         :0.1
# python_version  :3.6.8
# status          :Development
# ==============================================================================

# Import the modules needed to run the script.
import os
import sys
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Response
from wtforms import Form, StringField, FieldList, FormField
from wtforms_components import read_only
import logging
from pythonjsonlogger import jsonlogger

# create an Flask app instance
app = Flask(__name__)
app.secret_key = "flask_table"


class RowForm(Form):
    """ This is a class for a row in a table """
    column_1 = StringField('Column 1')
    column_2 = StringField('Column 2')
    column_3 = StringField('Column 3')

    def __int__(self):
        """ The constructor for RowForm class """
        super().__init__()
        read_only(self.column_1)
        read_only(self.column_2)
        read_only(self.column_3)


class TableForm(Form):
    """ This is a class for the table """
    title = StringField('')
    tableForm = FieldList(FormField(RowForm))


# This is the API to display the table in HTML
@app.route('/', mehtod=['GET'])
def display_table():
    """ This function create an instance of TableForm class and populate data in it """
    mytableform = TableForm()
    rowform = RowForm()
    rowform.column_1 = 'data in column 1'
    rowform.column_2 = 'data in column 2'
    rowform.column_3 = 'data in column 3'

    mytableform.tableForm.append_entry(rowform)

    return create_ui(mytableform)


def create_ui(wtform):
    """ render a HTML from the template """
    return render_template('ui.html', wtform=wtform)


# run the Flask app on debug mode
if __name__ == "__main__":
    app.run(debug=True, threaded=True)
