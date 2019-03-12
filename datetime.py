#! /usr/bin/env python3
import datetime

current_date = datetime.datetime.now()

future_date = current_date + datetime.timedelta(days = 72)

date_format = ("%I: %m %p on %B %w, %Y")

current_date.strftime(date_format)

future_date.strftime(date_format)
print ("-------------------------")
print ("Today's date: {}".format(current_date))
print ("-------------------------")
print ("Date on four weeks from now: {}".format(future_date))
print ("-------------------------")
