# -*- coding: utf-8 -*-
"""
	Flaskr
	~~~~~~

	A microblog example application written as Flask tutorial with
	Flask and sqlite3.

	:copyright: (c) 2015 by Armin Ronacher.
	:license: BSD, see LICENSE for more details.
"""

import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, Response, session, g, redirect, url_for, abort, \
	 render_template, flash, send_from_directory, jsonify

from gtfsHandler import GtfsHandler
from feeddates import FeedDates
from datepicker import DatePicker
from flask_cors import CORS, cross_origin

# create our little application :)
app = Flask(__name__)
CORS(app)

# Load default config and override config from an environment variable
app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'flaskr.db'),
	DEBUG=True,
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/templates/<path:path>')
def send_static(path):
    return send_from_directory('templates', path)


@app.route('/calendars')
def calendars():
	
	gtfs_calendar = FeedDates()
	start_and_ends = gtfs_calendar.get_calendar_bookends()

	full_calendar = gtfs_calendar.get_full_calendar_object()

	all_service_id = gtfs_calendar.get_all_service_id()

	datepicker = DatePicker()

	return jsonify(
		start_date=start_and_ends['start_date'],
		end_date=start_and_ends['end_date'],
		full_calendar=full_calendar,
		all_service_id=all_service_id
		)


@app.route('/updatecalendars', methods=['POST'])
def updatecalendars():
	resp = request.get_json()
	gtfs_calendar = FeedDates()
	gtfs_calendar.create_new_calendar_file(resp)
	return render_template('show_entries.html')


@app.route('/')
def show_entries():
	return render_template('show_entries.html')


@app.route('/add', methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	db = get_db()
	db.execute('insert into entries (title, text) values (?, ?)',
			   [request.form['title'], request.form['text']])
	db.commit()
	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('show_entries'))
	return render_template('login.html', error=error)


@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))
