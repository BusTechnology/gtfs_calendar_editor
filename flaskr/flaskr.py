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
from flask import Flask, request, Response, session, g, redirect, url_for, abort, \
	 render_template, flash, send_from_directory, jsonify

from gtfsHandler import GtfsHandler
from feeddates import FeedDates
from datepicker import DatePicker
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

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
	return("Update complete")