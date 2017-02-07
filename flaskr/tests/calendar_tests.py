import os
import calendar
import unittest
import tempfile
import mzgtfs.feed
import zipfile
import time

from gtfsHandler import GtfsHandler 

boroughs = ['staten_island']
path = "tests/gtfs_files/"
gtfs_calendar_handler = GtfsHandler()
reg_service = '20160927'

SI_trips_by_service_id = [
	{'trip_count': 990, 'service_id':'CA_D6-Saturday'}, 
	{'trip_count': 865, 'service_id':'CA_D6-Sunday'},
	{'trip_count': 1714, 'service_id': 'CA_D6-Weekday'},
	{'trip_count': 1787, 'service_id': 'CA_D6-Weekday-SDon'},
	{'trip_count': 1445, 'service_id': 'CA_S6-Weekday'},
 	{'trip_count': 372, 'service_id': 'CH_D6-Saturday'},
 	{'trip_count': 323, 'service_id': 'CH_D6-Sunday'},
 	{'trip_count': 793, 'service_id': 'CH_D6-Weekday'},
 	{'trip_count': 842, 'service_id': 'CH_D6-Weekday-SDon'},
 	{'trip_count': 560, 'service_id': 'CH_S6-Weekday'},
 	{'trip_count': 164, 'service_id': 'MA_D6-Weekday'},
 	{'trip_count': 164, 'service_id': 'MA_D6-Weekday-SDon'},
  	{'trip_count': 84, 'service_id': 'MA_S6-Weekday'},
 	{'trip_count': 911, 'service_id': 'YU_D6-Saturday'},
 	{'trip_count': 738, 'service_id': 'YU_D6-Sunday'},
	{'trip_count': 1393, 'service_id': 'YU_D6-Weekday'},
	{'trip_count': 1462, 'service_id': 'YU_D6-Weekday-SDon'},
	{'trip_count': 1096, 'service_id': 'YU_S6-Weekday'}
]

class CalendarTestCase(unittest.TestCase):

	def setUp(self):
		self.gtfs_file = path + 'google_transit_' + boroughs[0] + '.zip'
		self.gtfs_feed = mzgtfs.feed.Feed(filename=self.gtfs_file)
		# print 'calendars', calendars
		# self.temp = gtfs_calendar_handler.set_up(self.gtfs_feed)


	def test_gtfs_feed_load(self):
		self.assertIsNotNone(os.path.isfile(self.gtfs_file))

	def test_files_exist_in_feed(self):
		filenames = ['calendar.txt', 'calendar_dates.txt', 'trips.txt']
		for filename in filenames:
			load_gtfs = zipfile.ZipFile(self.gtfs_file)
			list_of_files = load_gtfs.namelist()
			self.assertIn(filename, list_of_files)

	def test_get_serviceid_from_calendar(self):
		list_service_id = gtfs_calendar_handler.get_service_id(self.gtfs_feed)
		self.assertTrue(len(list_service_id) > 0)

	def test_trips_count(self):
		list_service_id = gtfs_calendar_handler.get_service_id(self.gtfs_feed)
		for service_id in list_service_id:
			trips_with_service_id = gtfs_calendar_handler.get_trips_count(self.gtfs_feed, service_id)
			for trip in SI_trips_by_service_id:
				if trip['service_id'] == str(service_id):
					self.assertEqual(len(trips_with_service_id), trip['trip_count'])

	def test_mod_cal_file(self):
		og_cal = self.gtfs_feed.serviceperiods()
		for entry in og_cal:
			entry.set('saturday', '1')
		ts = str(int(time.time()))
		self.gtfs_feed.write('calendar' + ts + '.txt', og_cal)
		for filename in os.listdir("."):
			if filename.startswith("calendar"):
				os.rename(filename, filename[:8] + '.txt')
		self.gtfs_feed.make_zip(ts + '.zip', files=['calendar.txt'])
		new_gtfs = mzgtfs.feed.Feed(filename=ts+'.zip')
		new_cal = new_gtfs.serviceperiods()
		self.assertNotEqual(og_cal, new_cal)

	def test_start_end_dates(self):
		start_and_end = gtfs_calendar_handler.get_starting_and_ending_dates_for_feed(self.gtfs_feed)
		self.assertEqual(start_and_end['start_date'], '20160904')
		self.assertEqual(start_and_end['end_date'], '20170107')

	def test_get_regular_service_date(self):
		#list of calendars that are active
		gtfs_calendar_handler.set_up(self.gtfs_feed)
		cals = gtfs_calendar_handler.get_calendars_for_date('20160927')
		for c in cals:
			self.assertTrue('SD' in c )

	def test_get_modified_service_date(self):
		gtfs_calendar_handler.set_up(self.gtfs_feed)
		cals = gtfs_calendar_handler.get_calendar_dates_for_date(self.gtfs_feed, '20161010')
		for c in cals:
			self.assertTrue('SD' not in c)

	def test_get_modified_service_feed(self):
		gtfs_calendar_handler.set_up(self.gtfs_feed)
		cals = gtfs_calendar_handler.get_calendar_dates_for_feed(self.gtfs_feed)
		for k,v in cals.iteritems():
			for item in v:
				if item.get('exception_type') == str(1):
					self.assertTrue('SD' not in str(item.get('service_id')))
				#other service_ids are days that end in 'y'
				else: 
					self.assertTrue(str(item.get('service_id')[-1] == 'y'))
				#run on acive calendars

	def test_get_calendar_date_only(self):
		gtfs_calendar_handler.set_up(self.gtfs_feed)
		cals = gtfs_calendar_handler.get_calendars_for_date('20170101')
		for c in cals:
			self.assertTrue('Sunday' in c)

	def test_deactivate_calendar_dates(self):
		gtfs_calendar_handler.set_up(self.gtfs_feed)
		cals = gtfs_calendar_handler.deactivate_calendar('20170102')
		for c in cals:
			self.assertTrue(c.get('exception_type'), '2')

	def test_activate_calendar_dates(self):
		gtfs_calendar_handler.set_up(self.gtfs_feed)
		cals = gtfs_calendar_handler.activate_calendar('YU_D6-Sunday','20170102')
		# print cals['20160102']
		for k, v in cals.iteritems():
			if k == "exception_type":
				self.assertTrue(v, '1')




if __name__ == '__main__':
	globals()
	unittest.main()
