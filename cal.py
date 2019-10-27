#!/usr/bin/env python3

# colors used to highlight current day
fg_day = '#212121'
bg_day = '#dfdfdf'

def highlight_today(lines, day):
    res = ""
    for j, line in enumerate(lines[2:]):
        days = line.split(' ')
        for i, d in enumerate(days):
            if d.isnumeric() and int(d) == day:
                days[i] = f"<span foreground='{fg_day}' background='{bg_day}'>{day}</span>"
                line = ' '.join(days)
                lines[j+2] = line
                return lines

import calendar
from datetime import datetime
from os import system

today = datetime.today()
day = today.day
month = today.month
year = today.year

cal = calendar.month(year, month)

res = ""

lines = cal.splitlines()
hl = highlight_today(lines, day)
cal = '\n'.join(hl)

system(f'notify-send -u Low " " "{cal}"')
