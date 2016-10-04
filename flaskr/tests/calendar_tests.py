import os
import calendar
import unittest
import tempfile
import mzgtfs.feed
import zipfile

boroughs = ['staten_island']
# boroughs = ['bronx', 'brooklyn', 'manhattan', 'queens', 'staten_island']
path = "../../flaskr/gtfs_files/"

class CalendarTestCase(unittest.TestCase):

	def setUp(self):
		# for borough in boroughs:
		self.gtfs_file = path + 'google_transit_' + boroughs[0] + '.zip'
		self.gtfs_feed = mzgtfs.feed.Feed(filename=self.gtfs_file)

	def test_gtfs_feed_load(self):
		self.assertIsNotNone(os.path.isfile(self.gtfs_file))

	def test_files_exist_in_feed(self):
		filenames = ['calendar.txt', 'calendar_dates.txt', 'trips.txt']
		# for borough in boroughs:
		for filename in filenames:
			load_gtfs = zipfile.ZipFile(self.gtfs_file)
			list_of_files = load_gtfs.namelist()
			self.assertIn(filename, list_of_files)

	def test_get_serviceid_from_calendar(self):
		for borough in boroughs:
			calendar_list = self.gtfs_feed.read('calendar')
			list_service_id = []
			for entry in calendar_list:
				list_service_id.append(entry['service_id'])
			self.assertTrue(len(list_service_id) > 0)

	def test_trips_count(self):
		for borough in boroughs:
			calendar_list = self.gtfs_feed.read('calendar')
			list_service_id = []
			trips = self.gtfs_feed.trips()
			for entry in calendar_list:
				list_service_id.append(entry['service_id'])
			for service_id in list_service_id:
				i = 0
				list_trips = []
				for trip in trips:
					if trip['service_id'] == str(service_id):
						i += 1
						list_trips.append(trip)
				self.assertEqual(len(list_trips), i)

	
if __name__ == '__main__':
	unittest.main()