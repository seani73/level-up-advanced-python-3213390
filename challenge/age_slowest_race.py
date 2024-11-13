# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days

import re
import datetime

def get_data():
    with open('challenge/10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
    dates = re.findall(r'\d{2} \w{3} \d{4}', line)
    raceDate = datetime.datetime.strptime(dates[0], '%d %b %Y')
    doB = datetime.datetime.strptime(dates[1], '%d %b %Y')

    age = raceDate.year - doB.year

    if raceDate.month < doB.month:
        age -= 1

    parts = line.split()
    output = (age, parts[0])

    return output

def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()

# content = get_data()
# line = content.splitlines()
# # print(get_event_time(line[0]))