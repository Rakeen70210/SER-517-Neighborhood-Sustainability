import time
import requests
import json
import csv
string = open("json_data.json", "r").read()

dic = json.loads(string)
datausa_map = {}
id_exceptions = {'indianapolis, in': 'indianapolis city (balance), in', 'nashville, tn': 'nashville-davidson metropolitan government (balance), tn', 'louisville, ky': 'louisville/jefferson county metro government (balance), ky', 'honolulu, hi': 'urban honolulu, hi', 'winston salem, nc': 'winston-salem, nc', 'augusta, ga': 'augusta-richmond county consolidated government (balance), ga', 'boise, id': 'boise city, id', 'lexington, ky': 'lexington-fayette, ky', 'macon, ga': 'macon-bibb county, ga', 'athens, ga': 'athens-clarke county unified government (balance), ga', 'san buenaventura, ca': 'san buenaventura (ventura), ca'}
to_check = []

def update_datausa_id_map():
    for row in dic["results"]:
        datausa_map[row["name"].lower()] = row


def update_row(key):
    details = datausa_map[key] if key in datausa_map else datausa_map[id_exceptions[key]]
    location_id = details['id']
    base = f'https://datausa.io/api/data?Origin State={location_id}&measure=Millions%20Of%20Dollars,Thousands%20Of%20Tons&drilldowns=Destination State'
    data = requests.get(base).text
    time.sleep(1)
    try:
        past_trade_dollars, past_trade_tons,\
        future_trade_dollars, future_trade_tons = getData(data, "2020", "2030")
        return [past_trade_dollars, past_trade_tons,\
        future_trade_dollars, future_trade_tons]
    except json.decoder.JSONDecodeError:
        print(data)
        to_check.append([key, "json.decoder.JSONDecodeError " + data, base])
        return ["N" * 4]



def update_500_cities():
    passed = 0
    # name of csv output file
    output_file = open("output/output.csv", 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(output_file)

    # new columns
    new_cols = ["past_trade_dollars_2020", "past_trade_tons_2020", "future_trade_dollars_2030", "future_trade_tons_2030"]

    with open("C:/Users/ssuryaw1/PycharmProjects/SER517/final500Cities.csv", "r") as readObj:
        csvReader = csv.reader(readObj)
        headers = next(csvReader)


        # write headers
        headers.extend(new_cols)
        csv_writer.writerow(headers)

        for row in csvReader:
            cityName = row[1].lower().replace("-", " ")
            stateID = row[3].lower()
            key = cityName + ", " + stateID

            if key in datausa_map or key in id_exceptions:
                row.extend(update_row(key))
                passed += 1
            else:
                # default values
                row.extend(["N" * len(new_cols)])
                to_check.append([key, "Key(city) not found"])
            print(f'Writing details for: {key}')
            csv_writer.writerow(row)
            # break

    print("Found cities: ", passed - len(to_check), " \n Errors: ", to_check)

def getData(data, past_year, future_year):
    data = json.loads(data)["data"]
    past_trade_dollars = 0
    past_trade_tons = 0
    future_trade_dollars = 0
    future_trade_tons = 0

    for row in data:
        year = row["Year"]
        dollars = row["Millions Of Dollars"]
        tons = row["Thousands Of Tons"]

        if year == past_year:
            past_trade_dollars += dollars
            past_trade_tons += tons

        elif year == future_year:
            future_trade_dollars += dollars
            future_trade_tons += tons
    print("returning... ", [past_trade_dollars, past_trade_tons,
            future_trade_dollars, future_trade_tons])
    return [past_trade_dollars, past_trade_tons,
            future_trade_dollars, future_trade_tons]


update_datausa_id_map()
update_500_cities()
