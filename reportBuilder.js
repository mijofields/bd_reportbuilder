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


    initialData();