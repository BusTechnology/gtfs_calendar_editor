import os
import calendar
import unittest
import tempfile
import mzgtfs.feed
import zipfile

class CalendarTestCase(unittest.TestCase):

	def test_gtfs_feed_load(self):
		boroughs = ['staten_island']
		# boroughs = ['bronx', 'brooklyn', 'manhattan', 'queens', 'staten_island']
		path = "flaskr/gtfs_files/"
		for borough in boroughs:
			rv = os.path.isfile(path + 'google_transit_' + borough + '.zip')
			self.assertTrue(rv)

	def test_files_exist_in_feed(self):
		boroughs = ['staten_island']
		# boroughs = ['bronx', 'brooklyn', 'manhattan', 'queens', 'staten_island']
		filenames = ['calender', 'calendar_dates', 'trips']
		path = "flaskr/gtfs_files/"
		for borough in boroughs:
			for filename in filenames:
				tempZipFile = zipfile.ZipFile(path + 'google_transit_' + borough + '.zip')
				list_of_files = tempZipFile.namelist()
				if filename in list_of_files:
					self.assertTrue()

if __name__ == '__main__':
	unittest.main()