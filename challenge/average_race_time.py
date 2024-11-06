# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('challenge/10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    times = []
    races = get_data().splitlines()

    for result in races:
        parts = result.split()

        if "Jennifer" in parts[1] and "Rhines" in parts [2]:
            times.append(parts[0])

    return times


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    totalTime = 0
    count = 0
    
    for time in racetimes:
        parts = time.split(":")

        mins = int(parts[0])
        secs = int(float(parts[1]))

        wholeTime = mins + (secs/60)
        totalTime += wholeTime
        count = count + 1
    
    avgTime = totalTime/count
    avgMins = int(avgTime)
    avgSecs = (avgTime - avgMins)*60
    avgMillis = avgSecs*10
    avgMillis = int(avgMillis)/10
    avgMillis = avgMillis - int(avgMillis)
    avgMillis = int(round(avgMillis, 1) * 10)
    avgSecs = int(avgSecs)

    avgTimeFormatted = str(avgMins) + ":" + str(avgSecs) + "." + str(avgMillis)
    
    return avgTimeFormatted

get_average()