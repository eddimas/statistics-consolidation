import rrd_files
import db

from rrd_files import *
from db import *


print "==============================       TEST RRD -> Relational DB  ========================================"
db = DB_Stats('statistics', 'root', 'gustavo')
db.create()

DATE_START =datetime(year=2012, 
			month=12, 
                        day=13, 
                        hour=0, 
                        minute=0, 
                        second=0).strftime("%s")


DATE_END = datetime(year=2012, 
			        month=12, 
                                day=14, 
                                hour=0, 
                                minute=0, 
                                second=0).strftime("%s")

DATE_START = db.get_date_last_record()
DATE_END = datetime.now().strftime("%s")

act_rrd = RRD (path = "/home/gustavo/AC/xo_stats", name="pippy.rrd", date_start=DATE_START, date_end=DATE_END)
"""
act_rrd.show_valid_ds("uptime")
act_rrd.show_valid_ds("resumed")
act_rrd.show_valid_ds("new")
act_rrd.show_valid_ds("instances")
act_rrd.show_valid_ds("buddies")
"""
data = {}
for item in act_rrd.get_uptime_by_interval ():
	data['date_start'] = item[0]
	data['data'] = item[1]
	data['resource_name'] = act_rrd.get_name()
	"""FIXME implement all data load inside of RRD object""" 
	db.store_activity_uptime(act_rrd, data)