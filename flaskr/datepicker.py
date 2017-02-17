from feeddates import FeedDates
from gtfshandler import gtfshandler

gtfs_calendar = gtfshandler()

class DatePicker():

	def get_cal_for_date(self, service_date):
		
		f = FeedDates()
		f.load_gtfs()
		gtfs_calendar.set_up(f.gtfs_feed)
		active_cal = gtfs_calendar.get_active_calendars_for_date(service_date)

		return active_cal
	
	def deactivate_cal_for_date(self, service_date):
		f = FeedDates()
		f.load_gtfs()
		gtfs_calendar.set_up(f.gtfs_feed)
		
		return gtfs_calendar.deactivate_calendar(service_date)


	def activate_cal_for_date(self, service_date):
		return gtfs_calendar.activate_calendar(service_date)
		