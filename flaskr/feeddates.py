import mzgtfs.feed
from gtfsHandler import GtfsHandler

path = "gtfs_files/"
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

		return full_calendar
