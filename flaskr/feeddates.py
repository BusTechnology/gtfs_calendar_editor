import os
import mzgtfs.feed
import zipfile
import time
from gtfsHandler import GtfsHandler

path = "flaskr/gtfs_files/"
boroughs = ['staten_island', 'brooklyn', 'manhattan', 'queens', 'bronx']
gtfs_calendar = GtfsHandler()

class FeedDates():

	def load_gtfs(self):
		self.gtfs_file = path + 'google_transit_' + boroughs[0] + '.zip'
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

	def create_new_calendar_file(self, svcDate):
		self.load_gtfs()
		og_cal = self.gtfs_feed.service_exceptions()

		svc_date = svcDate['calendar']['d']
		active_service = svcDate['calendar']['s']
		inactive_service = svcDate['calendar']['i']

		for entry in og_cal:
			
			if entry.get('date') == svc_date:
				s_id = entry.get('service_id')
				e_type = entry.get('exception_type') 
				
				for svc in active_service:
					if s_id == svc and e_type == '2':
						entry.set('exception_type', '1')

				for svc in inactive_service:
					if s_id == svc and e_type == '1':
						entry.set('exception_type', '2')
						
		for entry in og_cal:
			if entry.get('date') == svc_date:
				print(entry.get('service_id'))
				print(entry.get('exception_type'))

		ts = str(int(time.time()))

		self.gtfs_feed.write('calendar' + ts + '.txt', og_cal)
		for filename in os.listdir("."):
			if filename.startswith("calendar"):
				os.rename(filename, filename[:8] + '.txt')
		self.gtfs_feed.make_zip(ts + '.zip', files=['calendar.txt'])

