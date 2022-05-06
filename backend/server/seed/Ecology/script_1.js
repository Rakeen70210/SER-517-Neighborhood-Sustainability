const csv = require('csv-parse');
const fs = require('fs');

var _500Cities = [];
var _rawData = [];
var _finalData = [];

function start(){
    parse500Cities();
}

// Load 500 cities data from 500Cities.csv
function parse500Cities(){
    fs.createReadStream('./Data/500Cities.csv')
    .pipe(csv.parse({ delimiter: ',' }))
    .on('data', (r) => {
        var city = {
            city_id: r[0],
            city_name: r[1],
            state_name: r[2],
            state_id: r[3],
            county_name: r[4],
            county_fips: r[5],
            zips: r[10]
        }
        // console.log(city);
        _500Cities.push(city);        
    })
    .on('end', () => {
        console.log("500 Cities load.");
        parseDataFile();
    })
}

// Load selected data from egrid2020_data
function parseDataFile(){
    fs.createReadStream('./Data/egrid2020_data_Selected.csv')
    .pipe(csv.parse({ delimiter: ',' }))
    .on('data', (r) => {
        var data = {
            state_id: r[0],
            emission_rate: r[1],
            nonrenewables_net_generation: r[2],
            renewables_net_generation: r[3]
        }
        console.log(data);
        _rawData.push(data);        
    })
    .on('end', () => {
        console.log("Data file load.");
        mergeData();
    })
}

// merge selected data with 500 cities
function mergeData(){
    var header = _500Cities[0];
    header.emission_rate = _rawData[0].emission_rate+' 2020';
    header.nonrenewables_net_generation = _rawData[0].nonrenewables_net_generation+' 2020';
    header.renewables_net_generation = _rawData[0].renewables_net_generation+' 2020';
    _finalData.push(header);

    for(var index = 1; index < _500Cities.length; index++){
        var city = _500Cities[index];
        _rawData.forEach(data => {
            if(city.state_id == data.state_id){
                city.emission_rate = data.emission_rate;
                city.nonrenewables_net_generation = data.nonrenewables_net_generation;
                city.renewables_net_generation = data.renewables_net_generation;
            }
        });
        // console.log(city);
        _finalData.push(city);
    }

    writeCSV();
}

// write data into 500Cities_energy_emission.csv
function writeCSV(){
    var str = '';
    _finalData.forEach(city => {
        str += (Object.values(city).join(",") + "\n");
    });
    // console.log(str);
    fs.writeFile('./Data/500Cities_energy_emission.csv', str, 'utf-8', (err) => {
        if (err) {
            console.log("Error");
        } else {
            console.log("Write CSV finish.");
        }
    })
}

start();