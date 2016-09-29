import mzgtfs.feed

gtfs_feed = mzgtfs.feed.Feed(filename='google_transit_staten_island.zip')

gtfs_feed.validate()

