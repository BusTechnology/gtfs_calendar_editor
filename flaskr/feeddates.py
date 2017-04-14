import os
import mzgtfs.feed
import zipfile
import time
import sys
import json
from gtfshandler import gtfshandler

path = "flaskr/gtfs_files/"
boroughs = ['staten_island', 'queens', 'manhattan', 'bronx', 'brooklyn', 'mtabc']
gtfs_calendar = gtfshandler()

class FeedDates():

	def load_gtfs(self):
		user_borough = os.environ['flaskr_borough']
		if user_borough not in boroughs:
			print "Borough not defined, try again"
			sys.exit(0)
		if user_borough == 'mtabc':
			self.gtfs_file = path + 'google_transit.zip'
		else:
			self.gtfs_file = path + 'google_transit_' + user_borough  + '.zip'
		self.gtfs_feed = mzgtfs.feed.Feed(filename=self.gtfs_file)

	def get_calendar_bookends(self):
		self.load_gtfs()

		start_and_ends = gtfs_calendar.get_starting_and_ending_dates_for_feed(self.gtfs_feed)
		return start_and_ends

	def get_full_calendar_object(self):
		self.load_gtfs()

		full_calendar = gtfs_calendar.get_calendars_for_feed(self.gtfs_feed)
		full_calendar_dates = gtfs_calendar.get_calendar_dates_for_feed(self.gtfs_feed)
		
		for c in full_calendar:
			full_calendar[c] = gtfs_calendar.get_active_calendars_for_date(c, full_calendar, full_calendar_dates)

		return full_calendar

	def get_all_service_id(self):
		all_service_id = gtfs_calendar.get_service_id(self.gtfs_feed)

		return all_service_id

	def add_new_service(self, cal_to_add):
		cal_to_add = {'date': str(svc_date), 'service_id': str(svc), 'exception_type': '1'}
		og_cal.append(cal_to_add)
		print('added new service')

	def create_new_calendar_file(self, calObj):
		self.load_gtfs()
		user_borough = os.environ['flaskr_borough']
		og_cal = self.gtfs_feed.service_exceptions()

		svc_date = calObj['calendar']['d']
		active_service = calObj['calendar']['s']
		inactive_service = calObj['calendar']['i']

		#go through calendar_dates objects, and turn on/off services that were edited in the webapp 
		for entry in og_cal:
			
			if entry.get('date') == svc_date:
				s_id = entry.get('service_id')
				e_type = entry.get('exception_type') 
				
				for svc in active_service:
					print(json.dumps(svc))
					if s_id == svc and e_type == '2':
						entry.set('exception_type', '1')

				for svc in inactive_service:
					if s_id == svc and e_type == '1':
						entry.set('exception_type', '2')

		#go through active/inactive services from the calendar object passed in from the webapp, and append to the calendar_dates.txt file
		for svc in active_service:
			cal_to_add = {'date': str(svc_date), 'service_id': str(svc), 'exception_type': '1'}
			if cal_to_add not in og_cal:
				og_cal.append(cal_to_add)

		for svc in inactive_service:
			cal_to_add = {'date': str(svc_date), 'service_id': str(svc), 'exception_type': '2'}
			if cal_to_add not in og_cal:
				og_cal.append(cal_to_add)			

		for entry in og_cal:
			if entry.get('date') == svc_date:
				print(entry.get('service_id'))
				print(entry.get('exception_type'))

		ts = str(int(time.time()))

		self.gtfs_feed.write('calendar_dates' + ts + '.txt', og_cal)
		self.gtfs_feed.write('calendar' + ts + '.txt', self.gtfs_feed.serviceperiods())
		for filename in os.listdir("."):
			if filename.startswith("calendar_dates"):
				os.rename(filename, filename[:14] + '.txt')
			elif filename.startswith("calendar"):
				os.rename(filename, filename[:8] + '.txt')
		if user_borough == 'mtabc':
			self.gtfs_feed.make_zip('google_transit.zip', files=['calendar.txt', 'calendar_dates.txt'])
			os.rename("google_transit.zip", "flaskr/gtfs_files/google_transit.zip")
		else:
			self.gtfs_feed.make_zip('google_transit_' + user_borough + '.zip', files=['calendar.txt', 'calendar_dates.txt'])
			os.rename("google_transit_" + user_borough + ".zip", "flaskr/gtfs_files/google_transit_" + user_borough + ".zip")
		os.remove("calendar.txt")
		os.remove("calendar_dates.txt")