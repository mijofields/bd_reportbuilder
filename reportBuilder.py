# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 17:41:59 2018

@author: mikeh
"""

import pandas 
import seaborn as sns
import os
from datetime import date


def TableBuild (indir="C:/Users/mikeh/Desktop/Projects/bd_reportBuilder/data", outdir="C:/Users/mikeh/Desktop/Projects/bd_reportBuilder/report"):
    
   
    
    
    if not os.path.exists(indir):           
        os.makedirs(indir)
    os.chdir(indir)
    
    firmName = input("Enter the Firm Name: ")
    firmName = firmName.strip()
    
    monthInRange = False
    isAYear = False
    
    endMonth = input("Please enter a month by number, eg. for January use 1, December 12: ")
    endMonth = endMonth.strip()
    while not monthInRange:
        
        endMonth = int(endMonth)
        if endMonth > 0 and endMonth < 13:
            monthInRange = True
    
    while not isAYear:
        endYear = input("Please enter a year, eg. 2018: ")
        endYear = endYear.strip()        
        if len(endYear) == 4:
            endYear = int(endYear)
            isAYear = True
            
    print("To confirm the following will be calculated")
    print("Firm:", firmName)
    print("End Date:", endDate)
    print("Start Date:", startDate)
    

  
    
   
    
    
    
    if not os.path.exists(outdir):           
        os.makedirs(outdir)
    os.chdir(outdir)
    
    
def relevantDates (endMonth, endYear):
    
    endOfMonth = (31,28,31,30,31,30,31,31,30,31,30,31)
    leapYearEndOfMonth = (31,29,31,30,31,30,31,31,30,31,30,31)
    endMonth = int(endMonth)
    endYear = int(endYear)
    print("end month: ", endMonth)
    print("end year: ", endYear)
    print(leapYearEndOfMonth[endMonth-1])
    print(endOfMonth[endMonth-1])
    
    if endYear%4 == 0:
        endDate = date(endYear, endMonth, leapYearEndOfMonth[endMonth-1])
        endDatePrior = date(endYear - 1, endMonth, endOfMonth[endMonth-1])
    elif (endYear-1) % 4 == 0:
        endDate = date(endYear, endMonth, endOfMonth[endMonth-1])
        endDatePrior = date(endYear - 1, endMonth, leapYearEndOfMonth[endMonth-1])
    else:
        endDate = date(endYear, endMonth, endOfMonth[endMonth-1])
        endDatePrior = date(endYear -1 , endMonth, endOfMonth[endMonth-1])
    
    if endMonth == 12:
        startMonth = 1
        startYear = endYear
        financialYearEnd = endDate
    else:
        startMonth = endMonth + 1
        startYear = endYear - 1
        financialYearEnd = date(endYear - 1, 12, 31)
        
    startDate = date(startYear, startMonth,1)
    startDatePrior = date(startYear - 1, startMonth, 1)
    
    
    relevantDates = {
            
            "YTD Start": startDate,
            "YTD End": endDate,
            "YTD Prior Start": startDatePrior,
            "YTD Prior End": endDatePrior,
            "FYE": financialYearEnd
            
            }
    
    print(relevantDates)
    return relevantDates
   
    

    
 
        
    


    
    
    
