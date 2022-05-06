const csv = require('csv-parse');
const fs = require('fs');

var _cityData = [];
var _rawData = [];
var _stateName = [];
var _finalData = [];

function start(){
    parseStateFile();
}

// Load 500 cities data from 500Cities.csv
function parseStateFile(){
    fs.createReadStream('./Data/500Cities.csv')
    .pipe(csv.parse({ delimiter: ',' }))
    .on('data', (r) => {
        // console.log(r);
        _cityData.push(r);
    })
    .on('end', () => {
        console.log("500 Cities load.");
        parseDataFile();
    })
}

// Load data from CHDB_data_city_all_v13.1.csv and select park access
function parseDataFile(){
    fs.createReadStream('./Data/CHDB_data_city_all_v13.1.csv')
    .pipe(csv.parse({ delimiter: ',' }))
    .on('data', (r) => {
        if(r[5] == 'Park access'){
            // console.log(r);
            _rawData.push(r);
        }
    })
    .on('end', () => {
        console.log("Data file load.");
        mergeData();
    })
}

// merge park access data into 500 cities 
function mergeData(){
    var header = _cityData[0];
    header.push('Park access');
    _finalData.push(header);

    for(var index = 1; index < _cityData.length; index++){
        var data = _cityData[index];
        var matched = false;
        for(var index2 = 0; index2 < _rawData.length; index2++){
            if(data[1] == cityName(_rawData[index2][4]) && data[3] == _rawData[index2][0]){
                matched = true;
                data.push(_rawData[index2][11]);
                break;
            }
        }
        if(!matched){
            data.push('N/A');
        }
        _finalData.push(data);
    }
    
    // console.log(_finalData);
    writeCSV();
}

// write data into 500Cities_Park.csv
function writeCSV(){
    var str = '';
    _finalData.forEach(data => {
        str += data + '\n';
    });
    // console.log(str);
    fs.writeFile('./Data/500Cities_Park.csv', str, 'utf-8', (err) => {
        if (err) {
            console.log("Error");
        } else {
            console.log("Write CSV finish.");
        }
    })
}

function cityName(name){
    if(name == 'Boise City'){
        return 'Boise';
    } else if(name == 'San Buenaventura (Ventura)'){
        return 'San Buenaventura';
    } else{
        return name;
    }
}

start();