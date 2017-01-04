import datetime
from datetime import timedelta
import calendar
import utils

class GtfsHandler():

	def set_up(self, gtfs_feed):
		global calendar_dates 
		calendar_dates = self.get_calendar_dates_for_feed(gtfs_feed)
		global calendars
		calendars = self.get_calendars_for_feed(gtfs_feed)

	def get_service_id(self, gtfs_feed):
		calendar_list = gtfs_feed.read('calendar')
		list_service_id = set()
		for entry in calendar_list:
			list_service_id.add(entry['service_id'])
		calendar_dates_list = gtfs_feed.read('calendar_dates')
		for entry in calendar_dates_list:
			list_service_id.add(entry['service_id'])
		list_service_id = list(list_service_id)
		return list_service_id

	def get_trips_count(self, gtfs_feed, service_id):
		trips = gtfs_feed.trips()
		list_trips = []
		for trip in trips:
			if trip['service_id'] == str(service_id):
				list_trips.append(trip)
		return list_trips

	def get_calendars_for_date(self,d):
		return calendars[d]

	def get_starting_and_ending_dates_for_feed(self, gtfs_feed):
		mindate = 99999999
		maxdate = -1
		for p in gtfs_feed.serviceperiods():

			start_date = int(p.get('start_date'))
			end_date = int(p.get('end_date'))
			if mindate > start_date:
				mindate = start_date
			if maxdate < end_date:
				maxdate = end_date

		for p in gtfs_feed.service_exceptions():

			end_date = int(p.get('date'))
			if mindate > end_date:
				mindate = end_date
			if maxdate < end_date:
				maxdate = end_date

		return {'start_date': str(mindate), 'end_date':str(maxdate)}

	def get_blank_calendar_object(self, start_and_end):
		start = utils.get_date_from_gtfs_date(start_and_end['start_date'])
		end = utils.get_date_from_gtfs_date(start_and_end['end_date'])

		calendarObject = {}
		for d in utils.daterange(start, end):
			d = utils.get_gtfs_date_from_date(d)
			calendarObject[d] = None

		return calendarObject

	def get_calendars_for_feed(self, gtfs_feed):
		# get list of service periods from feed
		svc_pd_list = gtfs_feed.serviceperiods()
		
		# dictionary of the start and end date for the entire feed
		start_and_end = self.get_starting_and_ending_dates_for_feed(gtfs_feed)
		
		# build a list of all the dates between the start and end dates \
		# each element is a dictionary with the \
		# key being the date and the value with None as a placeholder
		calendars = self.get_blank_calendar_object(start_and_end)	
		# calendars_by_date = {}
		for d in calendars.keys():
			d = utils.get_date_from_gtfs_date(d)
			day_of_week = calendar.day_name[d.weekday()]
			cal_list = []

			for svc_pd in svc_pd_list:
				if d >= svc_pd.start() and d <= svc_pd.end():
					if svc_pd[day_of_week.lower()] == '1':
						cal_list.append(str(svc_pd['service_id']))
			d = utils.get_gtfs_date_from_date(d)
			calendars[d] = cal_list
			
			# service_date_dict = {day_of_week: cal_list}
			# calendars_by_date.append(service_date_dict) 
		return calendars

	def get_calendar_dates_for_date(self, gtfs_feed, service_date):
		parsed_date = datetime.datetime.strptime(service_date, "%Y%m%d")
		cal_date_list = gtfs_feed.service_exceptions()

		exception_list = []

		for c in cal_date_list:
			if c.get('date') == parsed_date:
				exception_list.append(CalendarDate(\
					c.get('service_id'),\
					c.get('date'),\
					c.get('exception_type')))

		return exception_list	

	def get_calendar_dates_for_feed(self, gtfs_feed):
		feed_dates = {}
		cal_date_list = gtfs_feed.service_exceptions()

		for c in cal_date_list:
			# create dictionary to describe exception date
			e = {'service_id': c.get('service_id'), \
					'exception_type': c.get('exception_type')}

			# get exception date
			d = c.get('date')

			# if feed_dates doesn't have exception date, \
			# create a dictionary with date as key and a list of service descriptions
			if not feed_dates.has_key(d):
				feed_dates[d] = [e]

			# else, append exception description to value of the date
			else:
				feed_dates[d].append(e)

		# pass back the dictionary of the exception dates with associated service
		return feed_dates



	def get_active_calendars_for_date(self, service_date, calendars, calendar_dates):
		try:
			date_to_modify = calendar_dates.get(service_date)
			for item in date_to_modify:
				if item.get('exception_type') == '2':
					cal_to_modify = calendars.get(service_date)
					for sid in cal_to_modify:
						if sid == item.get('service_id'):
							cal_to_modify.remove(sid)

				if item.get('exception_type') == '1':
					cal_to_modify = calendars.get(service_date)
					if item.get('service_id') not in cal_to_modify: 
						cal_to_modify.append(str(item.get('service_id')))
		except TypeError:
			date_to_modify = None	

		return calendars[service_date]

	def deactivate_calendar(self, service_date):

		global calendar_dates

		date_to_modify = calendar_dates.get(service_date)
		for item in date_to_modify:
			if item.get('exception_type') == '1':
				item['exception_type'] = '2'
			# elif item.get('exception_type')	== '2': 
				# item['exception_type'] = '1'
		return calendar_dates[service_date]

	def activate_calendar(self, service_id, service_date):

		global calendar_dates

		calendar_dates[service_date] = {'service_id': service_id, \
					'exception_type': '1'}

		return calendar_dates
