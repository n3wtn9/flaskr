# all imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
            abort, render_template, flash

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'dev key'
USER_NAME = 'admin'
PASSWORD = 'default'

# create app
app = Flask(__name__)
app.config.from_object(__name__)
