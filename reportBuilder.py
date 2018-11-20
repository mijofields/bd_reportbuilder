# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 17:41:59 2018

@author: mikeh
"""

import pandas 
import seaborn as sns
import os
from datetime import date
from dateutil.relativedelta import relativedelta as rd


def makeDirs (indir="C:/Users/mikeh/Desktop/Projects/bd_reportBuilder/data", outdir="C:/Users/mikeh/Desktop/Projects/bd_reportBuilder/reports"):
    
    if not os.path.exists(indir):           
        os.makedirs(indir)
    os.chdir(indir)
   
    if not os.path.exists(outdir):           
        os.makedirs(outdir)
    
    print('Directories established')
    

def inputValidation ():

    monthInRange = False
    isAYear = False
    
    firmName = input("Enter the Firm Name: ")
    firmName = firmName.strip()
    
    """
    Firm name will be selected via a drop down called from db generated firm list
    
    """
    
    while not monthInRange:
        endMonth = input("Please enter a month by number, eg. for January use 1, December 12: ")
        endMonth = endMonth.strip()
        endMonth = int(endMonth)
                    
        if endMonth > 0 and endMonth < 13:
            monthInRange = True
    
    while not isAYear:
        endYear = input("Please enter a year, eg. 2018: ")
        endYear = endYear.strip()        
        if len(endYear) == 4:
            endYear = int(endYear)
            isAYear = True    
    
    print("To confirm the following will be calculated:")
    print("Firm:", firmName)
    print("End Month:", endMonth)
    print("End Year:", endYear)
    
    
    
    
def MakeRelevantDates (endMonth, endYear, yearEnd=12):
    
    endOfMonth = (31,28,31,30,31,30,31,31,30,31,30,31)
    leapYearEndOfMonth = (31,29,31,30,31,30,31,31,30,31,30,31)

    
    if endYear % 4 == 0:
        endDate = date(endYear, endMonth, leapYearEndOfMonth[endMonth-1])
        endDatePrior = endDate + rd(years=-1)
    elif (endYear-1) % 4 == 0:
        endDatePrior = date(endYear - 1, endMonth, leapYearEndOfMonth[endMonth-1])
        endDate = endDatePrior + rd(years=+1)
    else:
        endDate = date(endYear, endMonth, endOfMonth[endMonth-1])
        endDatePrior = endDate + rd(years=-1)
    
    if endMonth == 12:
        startMonth = 1
        startYear = endYear
    else:
        startMonth = endMonth + 1
        startYear = endYear - 1
        
    startDate = date(startYear, startMonth, 1)
    startDatePrior = startDate + rd(years=-1)
    
    if endMonth == yearEnd:
        fiscalYE = endDate
        fiscalYEm1 = endDatePrior
        fiscalYEm2 = endDatePrior + rd(years=-1)
        displayYTD = False
        
    elif endMonth < yearEnd:
        fiscalYE = date(endYear-1, yearEnd, endOfMonth[yearEnd-1])
        fiscalYEm1 = fiscalYE + rd(years=-1)
        fiscalYEm2 = fiscalYE + rd(years=-2)
        displayYTD = True
    
    else:
        fiscalYE = date(endYear, yearEnd, endOfMonth[yearEnd-1])
        fiscalYEm1 = fiscalYE + rd(years=-1)
        fiscalYEm2 = fiscalYE + rd(years=-2)
        displayYTD = True
   
    
    
    relevantDates = {            
            "YTD Start": startDate,
            "YTD End": endDate,
            "YTD Prior Start": startDatePrior,
            "YTD Prior End": endDatePrior,
            "FYE": fiscalYE,
            "FYE-1": fiscalYEm1,
            "FYE-2": fiscalYEm2,
            "Display YTD": displayYTD           
            }
    
    
    return relevantDates['YTD Start']
    
    

    
 
        
    


    
    
    
