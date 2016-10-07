import os
import calendar
import unittest
import tempfile
import mzgtfs.feed
import zipfile

from utils import GtfsHandler

boroughs = ['staten_island']
# boroughs = ['bronx', 'brooklyn', 'manhattan', 'queens', 'staten_island']
path = "../flaskr/gtfs_files/"
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

	def test_gtfs_feed_load(self):
		self.assertIsNotNone(os.path.isfile(self.gtfs_file))

	def test_files_exist_in_feed(self):
		filenames = ['calendar.txt', 'calendar_dates.txt', 'trips.txt']
		for filename in filenames:
			load_gtfs = zipfile.ZipFile(self.gtfs_file)
			list_of_files = load_gtfs.namelist()
			self.assertIn(filename, list_of_files)

	def test_get_serviceid_from_calendar(self):
		gtfs_calendar_handler = GtfsHandler()
		list_service_id = gtfs_calendar_handler.get_service_id(self.gtfs_feed)
		self.assertTrue(len(list_service_id) > 0)

	def test_trips_count(self):
		gtfs_calendar_handler = GtfsHandler()
		list_service_id = gtfs_calendar_handler.get_service_id(self.gtfs_feed)
		for service_id in list_service_id:
			trips_with_service_id = gtfs_calendar_handler.get_trips_count(self.gtfs_feed, service_id)
			for trip in SI_trips_by_service_id:
				if trip['service_id'] == str(service_id):
					self.assertEqual(len(trips_with_service_id), trip['trip_count'])
	
if __name__ == '__main__':
	unittest.main()