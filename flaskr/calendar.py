import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

# create calendar app
app = Flask(__name__)
