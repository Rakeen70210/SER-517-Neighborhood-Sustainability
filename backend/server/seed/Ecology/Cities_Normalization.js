const csv = require('csv-parse');
const fs = require('fs');

var _500Cities = [];
var dataPointer = 11;

function start(){
    parse500Cities();
}


// Load 500 cities data
function parse500Cities(){
    fs.createReadStream('./Data/500Cities_Collection.csv')
    .pipe(csv.parse({ delimiter: ',' }))
    .on('data', (r) => {
        _500Cities.push(r);        
    })
    .on('end', () => {
        console.log("500 Cities load.");
        normalization();
    })
}

// run each function for subdomains
function normalization(){
    var currentPointer = dataPointer;
    // emission
    general_normalization(currentPointer);
    currentPointer += 1;
    // energyGeneration
    generation_normalization(currentPointer);
    currentPointer += 1;
    // physicalHealth
    general_normalization(currentPointer);
    currentPointer += 1;
    // transit
    general_normalization(currentPointer);
    currentPointer += 1;
    // air
    general_normalization(currentPointer);
    currentPointer += 1;
    // console.log(_500Cities);
    writeCSV();
}

// 1 line normalization
function general_normalization(pointer){
    var max = new Number(-1);
    for(var i = 1; i < _500Cities.length; i++){
        var value = new Number(_500Cities[i][pointer]);
        if(max < value) max = value;
    }
    // console.log(max);
    for(var i = 1; i < _500Cities.length; i++){
        _500Cities[i][pointer] = new Number(_500Cities[i][pointer]) / max;
        // console.log(_500Cities[i][pointer]);
    }
}

// normalization for energy (renewable/(non-renewable+renewable))
function generation_normalization(pointer){
    var max = new Number(-1);
    for(var i = 1; i < _500Cities.length; i++){
        var value1 = new Number(_500Cities[i][pointer]);
        var value2 = new Number(_500Cities[i][pointer+1]);
        _500Cities[i][pointer+1] = value2 / (value1 + value2)
        // console.log(_500Cities[i][pointer+1]);
        _500Cities[i].splice(pointer,1);
        // console.log(_500Cities[i][pointer]);
    }
    _500Cities[0].splice(pointer,1);
    // console.log(_500Cities);
    general_normalization(pointer);
}

// write data into 500Cities_Final.csv
function writeCSV(){
    var str = '';
    _500Cities.forEach(city => {
        str += (Object.values(city).join(",") + "\n");
    });
    // console.log(str);
    fs.writeFile('./Data/500Cities_Final.csv', str, 'utf-8', (err) => {
        if (err) {
            console.log("Error");
        } else {
            console.log("Write CSV finish.");
        }
    })
}

start();