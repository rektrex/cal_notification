#!/usr/bin/env python3

import calendar
from datetime import datetime
from os import system

today = datetime.today()

day = today.day
month = today.month
year = today.year

cal = calendar.month(year, month)

system(f'notify-send -u Low " " "{cal}"')
