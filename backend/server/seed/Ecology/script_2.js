const csv = require('csv-parse');
const fs = require('fs');

var _stateData = [];
var _rawData = [];
var _stateName = [];
var _finalData = [];

function start(){
    parseStateFile();
}

// Load current State level data
function parseStateFile(){
    fs.createReadStream('./Data/State_level_data_final.csv')
    .pipe(csv.parse({ delimiter: ',' }))
    .on('data', (r) => {
        // console.log(r);
        _stateData.push(r);
    })
    .on('end', () => {
        console.log("State data load.");
        parseDataFile();
    })
}

// Load farm production selected data
function parseDataFile(){
    fs.createReadStream('./Data/Farm_production_data_Selected.csv')
    .pipe(csv.parse({ delimiter: ',' }))
    .on('data', (r) => {
        // console.log(r);
        _rawData.push(r);
    })
    .on('end', () => {
        console.log("Data file load.");
        parseStateName();
    })
}

// Load state name/initials
function parseStateName(){
    fs.createReadStream('./Data/State_Name.csv')
    .pipe(csv.parse({ delimiter: ',' }))
    .on('data', (r) => {
        // console.log(r);
        _stateName.push(r);
    })
    .on('end', () => {
        console.log("State name load.");
        replaceStateName();
    })
}

function replaceStateName(){
    _rawData.forEach(data => {
        for(var i = 0; i < _stateName.length; i++){
            if(data[0] == _stateName[i][0]){
                data[0] = _stateName[i][1];
                break;
            }
        }
    });
    // console.log(_rawData);
    mergeData();
}

// merge data into state
function mergeData(){
    _stateData.forEach(state => {
        var data = state;
        var matched = false;
        for(var index = 0; index < _rawData.length; index++){
            if(data[0] == _rawData[index][0]){
                matched = true;
                data.push(_rawData[index][1],_rawData[index][2])
                break;
            }
        }
        if(!matched){
            data.push('0','0');
        }
        _finalData.push(data);
    });
    
    // console.log(_finalData);
    writeCSV();
}

// write data back into State_level_data_final.csv
function writeCSV(){
    var str = '';
    _finalData.forEach(data => {
        str += data + '\n';
    });
    // console.log(str);
    fs.writeFile('./Data/State_level_data_final.csv', str, 'utf-8', (err) => {
        if (err) {
            console.log("Error");
        } else {
            console.log("Write CSV finish.");
        }
    })
}

start();