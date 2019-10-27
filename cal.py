#!/usr/bin/env python3

# colors used to highlight current day
fg_day = '#212121'
bg_day = '#dfdfdf'

import calendar
from datetime import datetime
from os import system
import sys


def highlight_today(lines, day):
    for j, line in enumerate(lines[2:]):
        days = line.split(' ')
        for i, d in enumerate(days):
            if d.isnumeric() and int(d) == day:
                days[i] = f"<span foreground='{fg_day}' background='{bg_day}'>{day}</span>"
                line = ' '.join(days)
                lines[j+2] = line
                return lines


def get_highlighted_month(cal):
    lines = cal.splitlines()
    hl = highlight_today(lines, day)
    cal = '\n'.join(hl)
    return cal


def pad_cal(cal):
    lines = cal.splitlines()
    lines = [line.ljust(20, ' ') for line in lines]
    cal = '\n'.join(lines)
    return cal


def join_cals(cals):
    cals = [cal.splitlines() for cal in cals]
    n = len(cals[0])
    combined_lines = []
    for i in range(n):
        combined_lines.append(" | ".join([cal[i] for cal in cals]))

    cals = "\n".join(combined_lines)
    return cals


today = datetime.today()
day = today.day
month = today.month
year = today.year

args = sys.argv
if len(args) == 2 and args[1] == '-3':
    cal1 = calendar.month(year, month)
    cal1 = pad_cal(cal1)
    cal1 = get_highlighted_month(cal1)

    next_month = (month + 1) % 12
    if next_month == 1:
        cal2 = calendar.month(year + 1, next_month)
    else:
        cal2 = calendar.month(year, next_month)
    cal2 = pad_cal(cal2)

    previous_month = (month - 1) % 12
    if previous_month == 12:
        cal3 = calendar.month(year - 1, previous_month)
    else:
        cal3 = calendar.month(year, previous_month)

    cal = join_cals([cal2, cal1, cal3])

else:
    cal = calendar.month(year, month)
    lines = cal.splitlines()
    hl = highlight_today(lines, day)
    cal = '\n'.join(hl)

system(f'notify-send -u Low " " "{cal}"')
