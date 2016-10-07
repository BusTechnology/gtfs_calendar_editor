import os
import mzgtfs.feed

class GtfsHandler():

	def get_service_id(self, gtfs_feed):
		calendar_list = gtfs_feed.read('calendar')
		list_service_id = []
		for entry in calendar_list:
			list_service_id.append(entry['service_id'])
		return list_service_id

	def get_trips_count(self, gtfs_feed, service_id):
		trips = gtfs_feed.trips()
		list_trips = []
		for trip in trips:
			if trip['service_id'] == str(service_id):
				list_trips.append(trip)
		return list_trips


