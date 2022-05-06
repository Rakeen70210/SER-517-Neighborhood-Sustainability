const csv = require('csv-parse');
const fs = require('fs');

var _cityData = [];
var _rawData = [];
var _stateCode = [];
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
        parseStateCode();
    })
}

// Load state code from State_Code.csv
function parseStateCode(){
    fs.createReadStream('./Data/State_Code.csv')
    .pipe(csv.parse({ delimiter: ',' }))
    .on('data', (r) => {
        // console.log(r);
        _stateCode.push(r);
    })
    .on('end', () => {
        console.log("State code load.");
        parseDataFiles();
    })
}

// Load all transit data
function parseDataFiles(){
    var resultsObj = {};
    var promises = [];
    var path = './Data/Transit data/alltransit_data_places_{filepath}.csv';
    for(var i = 0; i < _stateCode.length; i++){
        var stateCode = _stateCode[i][0];
        var stateInit = _stateCode[i][1];
        var filepath = path.replace("{filepath}", stateCode);
        var promise = parseDataFile(filepath, stateInit, resultsObj);
        promises.push(promise);
    }

    var finalPromise = promises.reduce((previousPromise, nextPromiseElement) => {
        return previousPromise.then(() => {
          return nextPromiseElement;
        });
      }, Promise.resolve());

    finalPromise.then(() => {
        // console.log("resultsObj: "+JSON.stringify(resultsObj, null, 2));
        mergeData(resultsObj);
    })

}

function parseDataFile(path, stateInit, resultsObj){
    var dataSoFar = [];
    return new Promise(function(resolve, reject){
        fs.createReadStream(path)
        .pipe(csv.parse({ delimiter: ',' }))
        .on('data', (r) => {
            dataSoFar.push(r);
            //console.log(r);
        })
        .on('end', () => {
            console.log("resolved : "+stateInit);
            resultsObj[stateInit] = dataSoFar;
            // console.log(dataSoFar);
            resolve();
        })
        .on('error', () => {
            console.log("rejected : "+stateInit)
            reject();
        })
    })
}

// merge transit data into 500 cities
function mergeData(resultsObj){
    for(var state in resultsObj){
        var pointer = 1;
        for(var index = pointer; index < _cityData.length; index++){
            var data = _cityData[index];
            if(data[3] == state){
                var matched = false;
                for(var index2 = 1; index2 < resultsObj[state].length; index2++){
                    // console.log(resultsObj[state][index2][1]);
                    if(data[1] == cityName(resultsObj[state][index2][1])){
                        matched = true;
                        data.push(resultsObj[state][index2][5]);
                        break;
                    }
                }
                if(!matched){
                    // data.push('N/A');
                }
                _cityData[index] = data;
                pointer = index;
            }
        }
        pointer = 1;
    }
    
    _cityData[0].push('alltransit_performance_score');
    // console.log(_cityData);
    writeCSV();
}

// write data into 500Cities_Transit.csv
function writeCSV(){
    var str = '';
    _cityData.forEach(data => {
        str += data + '\n';
    });
    // console.log(str);
    fs.writeFile('./Data/500Cities_Transit.csv', str, 'utf-8', (err) => {
        if (err) {
            console.log("Error");
        } else {
            console.log("Write CSV finish.");
        }
    })
}

function cityName(name){
    if(name == '"Boise City"'){
        return 'Boise';
    } else if(name == '"San Buenaventura (Ventura)"'){
        return 'San Buenaventura';
    } else if(name == '"Athens-Clarke County unified government (balance)"'){
        return 'Athens';
    } else if(name == '"Macon-Bibb County"'){
        return 'Macon';
    } else if(name == '"Augusta-Richmond County consolidated government (balance)"'){
        return 'Augusta';
    } else if(name == '"Lexington-Fayette"'){
        return 'Lexington';
    } else if(name == '"Urban Honolulu"'){
        return 'Honolulu';
    } else if(name == '"Nashville-Davidson metropolitan government (balance)"'){
        return 'Nashville';
    } else if(name == '"Indianapolis city (balance)"'){
        return 'Indianapolis';
    } else{
        return name.replaceAll('"','');
    }
}

start();