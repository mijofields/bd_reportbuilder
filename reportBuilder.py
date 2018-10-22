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
    
    dayOfMonth = (31,28,31,30,31,30,31,31,30,31,30,31)
    
    
    if not os.path.exists(indir):           
        os.makedirs(indir)
    os.chdir(indir)
    
    firmName = input("Enter the Firm Name: ")
    firmName = firmName.strip()
    
    endMonth = input("Please enter a month by number, eg. for January use 1: ")
    endMonth = endMonth.strip()
    endMonth = int(endMonth)
    while not endMonth > 0 and endMonth < 13:
        endMonth = input("Please enter a month between 1 for January and 12 for December: ")
        endMonth = endMonth.strip()
        endMonth = int(endMonth)
    endYear = input("Please enter a year, eg. 2018: ")
    endYear = endYear.strip()
    endYear = int(endYear)
   
    endDate = date(endYear, endMonth, dayOfMonth[endMonth-1])
    startDate = date(endYear-1, endMonth+1, dayOfMonth[endMonth])
    
    print("To confirm the following will be calculated")
    print("Firm:", firmName)
    print("End Date:", endDate)
    print("Start Date:", startDate)
    
  

    
    
    
    if not os.path.exists(outdir):           
        os.makedirs(outdir)
    os.chdir(outdir)

    
    
    
