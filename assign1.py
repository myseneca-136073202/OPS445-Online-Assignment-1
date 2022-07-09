#!/usr/bin/env python3
import sys

'''
OPS445 Assignment 1 - Winter 2022

Program: assign1.py
Author: Chuanlong Zhu - 105009211

The python code in this file (assign1.py) is original work written by
Chuanlong Zhu. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

Date: 2022-07-06
'''

from asyncio.windows_events import NULL
from contextlib import nullcontext


def usage():
    "TODO enter docstring"
    pass # TODO: delete this line, replace with valid code.

def days_in_mon(year):
    "TODO enter docstring"
    lyear = year % 4 # TODO: put this into the function leap_year.
    if lyear == 0:
        feb_max = 29 # this is a leap year
    else:
        feb_max = 28 # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        feb_max = 28 # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        feb_max = 29 # this is a leap year

    mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return mon_max

def valid_date(date):
    "TODO enter docstring"
    # return True or False 
    try:
        str_day, str_month, str_year = date.split('-')
        if not str_day.isnumeric() or not str_month.isnumeric() or not str_year.isnumeric():
            print("Error: wrong date entered")
            return False
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        lyear = leap_year(year)
        if lyear == 0:
            feb_max = 29 # this is a leap year
        else:
            feb_max = 28 # this is not a leap year

        lyear = year % 100
        if lyear == 0:
            feb_max = 28 # this is not a leap year

        lyear = year % 400
        if lyear == 0:
            feb_max = 29 # this is a leap year
        mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

        if day<1 or day>mon_max[month]:
            print("Error: wrong day entered")
            return False
        if month<1 or month>12:
            print("Error: wrong month entered")
            return False
        return True
    except:
        print("Error: wrong date entered")
        return False

   
    

def leap_year(year):
    "takes a year in YYYY format, and returns True if it's a leap year, False otherwise."
    lyear = year % 4 
    return lyear


def after(today):
    "after takes a valid date string in DD-MM-YYYY format and returns"
    "a date string for the next day in DD-MM-YYYY format."
    check = valid_date(today)
    if not check:
        return check
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        lyear = leap_year(year)
        if lyear == 0:
            feb_max = 29 # this is a leap year
        else:
            feb_max = 28 # this is not a leap year

        lyear = year % 100
        if lyear == 0:
            feb_max = 28 # this is not a leap year

        lyear = year % 400
        if lyear == 0:
            feb_max = 29 # this is a leap year

        tmp_day = day + 1 # next day

        mon_max = days_in_mon(year)
        if tmp_day > mon_max[month]:
            to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1
            tmp_month = month + 1
        else:
            to_day = tmp_day
            tmp_month = month + 0

        if tmp_month > 12:
            to_month = 1
            year = year + 1
        else:
            to_month = tmp_month + 0

        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
        return next_date

def before(today):
    "after takes a valid date string in DD-MM-YYYY format and returns"
    "a date string for the pass day in DD-MM-YYYY format."
    check = valid_date(today)
    if not check:
        return check
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        lyear = leap_year(year) 
        if lyear == 0:
            feb_max = 29 # this is a leap year
        else:
            feb_max = 28 # this is not a leap year

        lyear = year % 100
        if lyear == 0:
            feb_max = 28 # this is not a leap year

        lyear = year % 400
        if lyear == 0:
            feb_max = 29 # this is a leap year

        tmp_day = day - 1 # past day
        mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        
        if tmp_day < 1 and month - 1 > 0:
            to_day = mon_max[month-1]
            to_month = month-1
            to_year = year
            
        elif tmp_day < 1 and month -1 < 1:
            to_month = 12
            to_day = mon_max[to_month]
            to_year = year-1
        
        else:
            to_day = tmp_day
            to_month = month
            to_year = year


        pass_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(to_year)
        return pass_date
    

def dbda(start_date, num_days):
    end_date = "00-00-0000"
    days = int(num_days)
    # create a loop
    # call before() or after() as appropriate
    # return end_date
    check = valid_date(start_date)

    if not check:
        return check
    if days > 0:
        for x in range(days):
            start_date = after(start_date)
        end_date = start_date
    else:
        for x in range(abs(days)):
            start_date = before(start_date)
        end_date = start_date
    return end_date
        
    
if __name__ == "__main__":
    # process command line arguments
    # call dbda()
    # output the result
    program_name = sys.argv[0]
    arguments = sys.argv[1:]
    count = len(arguments)
    print(dbda(arguments[0],arguments[1]))


    



