const fs = require('fs');
const moment = require('moment');
const chalk = require('chalk');
const inquirer = require('inquirer');



//input validation//

function initialData () {

    const months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    const years = ["2014", "2015", "2016", "2017"]
    const endOfMonth = {
        January : 31,
        February: 28,
        March: 31,
        April: 30,
        May: 31,
        June: 30,
        July: 31,
        August: 31,
        September: 30,
        October: 31,
        November: 30,
        December: 30
    }

    const endOfMonthLeap = {
        January : 31,
        February: 29,
        March: 31,
        April: 30,
        May: 31,
        June: 30,
        July: 31,
        August: 31,
        September: 30,
        October: 31,
        November: 30,
        December: 30
    }

    inquirer.prompt([

        {
            name: "firmName",
            type: "input",
            message: chalk.magenta("Please enter the firm name:")
        }, {

            name: "endMonth",
            type: "list",
            message: chalk.greenBright("Please select the period-end month:"),
            choices: months
        },{

            name: "endYear",
            type: "list",
            message: chalk.cyanBright("Please select the period-end year:"),
            choices: years
        }  
    ])
    
    .then(function(answers){

        let firmName = answers.firmName;
        let fullMonthName = answers.endMonth;
        let year = parseInt(answers.endYear);
        let monthNum = months.indexOf(fullMonthName)+1;
        let endDay = endOfMonth[fullMonthName];

        let endDate = moment(`'${year}-${monthNum}-${endDay}'`, 'YYYY-MM-DD').format('YYYY-MM-DD');

        const initialDataObj = {

            firmName: firmName,
            endYear: year,
            endMonth: monthNum,
            endDay: endDay,
            endDate: endDate
        }
     
        console.log(initialDataObj)
        return initialDataObj
        

    })

    }

    function relevantDatesCalc (Year,YTDMonth,FYEMonth = 12) { 
    
        Year = parseInt(Year);
        YTDMonth = parseInt(YTDMonth);

        const endOfMonth = [31,28,31,30,31,30,31,31,30,31,30,31];
        const leapYearEndOfMonth = [31,29,31,30,31,30,31,31,30,31,30,31];

        //end dates of YTD accounting for leap years
        if (Year % 4 == 0) {
                endDate = moment(new Date(Year, YTDMonth-1, leapYearEndOfMonth[YTDMonth-1])).format('YYYY-MM-DD');
                endDatePrior = moment(new Date(Year-1, YTDMonth-1, endOfMonth[YTDMonth-1])).format('YYYY-MM-DD');
        } else if ((Year - 1) % 4 == 0) {
                endDate = moment(new Date(Year, YTDMonth-1, endOfMonth[YTDMonth-1])).format('YYYY-MM-DD');
                endDatePrior = moment(new Date(Year-1, YTDMonth-1, leapYearEndOfMonth[YTDMonth-1])).format('YYYY-MM-DD');
        } else {
                endDate = moment(new Date(Year, YTDMonth-1, endOfMonth[YTDMonth-1])).format('YYYY-MM-DD');
                endDatePrior = moment(new Date(Year-1, YTDMonth-1, endOfMonth[YTDMonth-1])).format('YYYY-MM-DD');          
        }

        // ytd period start dates
        if (FYEMonth === 12) {
                startMonth = 0;
                startYear = Year;
        } else if (YTDMonth < FYEMonth) {
                startMonth = FYEMonth;
                startYear = Year-1;
        } else {
                startMonth = FYEMonth;
                startYear = Year;
        }


        startDate = moment(new Date(startYear, startMonth, 1)).format('YYYY-MM-DD');
        startDatePrior = moment(new Date(startYear-1, startMonth, 1)).format('YYYY-MM-DD');
        

        // fiscal year ends
        if (YTDMonth == FYEMonth ){
            fiscalYE = endDate;
            fiscalYEm1 = endDatePrior;
            fiscalYEm2 = moment(endDatePrior).subtract(1, 'y').format('YYYY-MM-DD');
            displayYTD = false;
            ytdPeriod = 0;

        } else if (YTDMonth < FYEMonth){

            fiscalYE = moment(new Date(Year-1, FYEMonth-1, endOfMonth[FYEMonth-1])).format('YYYY-MM-DD');
            fiscalYEm1 = moment(fiscalYE).subtract(1, 'y').format('YYYY-MM-DD');
            fiscalYEm2 = moment(fiscalYE).subtract(2, 'y').format('YYYY-MM-DD');
            displayYTD = true;
            ytdPeriod = (12 - FYEMonth) + YTDMonth;


        } else {
            fiscalYE = moment (new Date(Year, FYEMonth-1, endOfMonth[FYEMonth-1])).format('YYYY-MM-DD');
            fiscalYEm1 = moment(fiscalYE).subtract(1, 'y').format('YYYY-MM-DD');
            fiscalYEm2 = moment(fiscalYE).subtract(2, 'y').format('YYYY-MM-DD');
            displayYTD = true;
            ytdPeriod = YTDMonth-FYEMonth;


        }


    
    // else:



        const relevantDates =  {

            startDate: startDate,
            endDate: endDate,
            startDatePrior: startDatePrior,
            endDatePrior: endDatePrior,
            fiscalYE: fiscalYE,
            fiscalYEm1: fiscalYEm1,
            fiscalYEm2: fiscalYEm2,
            displayYTD: displayYTD,
            ytdPeriod: ytdPeriod
        }    

       

        console.log(relevantDates);
        return relevantDates;
    }

let Year = process.argv[2];
let YTDMonth = process.argv[3];
let FYEMonth = process.argv[4];

relevantDatesCalc (Year,YTDMonth,FYEMonth) 

    // initialData();