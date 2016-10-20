import datetime
from datetime import timedelta

def get_date_from_gtfs_date(gtfs_date):
	return datetime.datetime.strptime(gtfs_date, "%Y%m%d")

def get_gtfs_date_from_date(d):
	return d.strftime("%Y%m%d")


def daterange(start_date, end_date):
	for n in range(int ((end_date - start_date).days)):
		yield start_date + timedelta(n)

