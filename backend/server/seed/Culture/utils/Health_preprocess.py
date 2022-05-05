import os

import pandas as pd

state_abbr = ["NY", "CA", "IL", "FL", "TX", "PA", "TX", "GA", "DC", "MA", "AZ", "WA", "CA", "MI", "CA", "MN", "FL",
              "CO", "CA", "MD", "NV", "OR", "TX", "MO", "CA", "FL", "CA", "OH", "PA", "TX", "OH", "MO", "IN", "OH",
              "NC", "VA", "WI", "RI", "FL", "UT", "TN", "VA", "TN", "NC", "LA", "KY", "OK", "CT", "NY", "TX", "CT",
              "AZ", "NE", "TX", "HI", "TX", "NM", "AL", "OH", "NY", "CA", "PA", "OK", "FL", "CA", "CO", "SC", "MA",
              "MI", "CA", "NY", "TN", "CA", "UT", "LA", "OH", "CT", "SC", "AZ", "FL", "UT", "MA", "CA", "KS", "OH",
              "IA", "CA", "FL", "TX", "WI", "NV", "AR", "CA", "NC", "NC", "CA", "FL", "TN", "WA", "NY", "TX", "CA",
              "GA", "ID", "CA", "PA", "CA", "CO", "OH", "AR", "CA", "CA", "CA", "NC", "TX", "IN", "CA", "MI", "NC",
              "MS", "CA", "MI", "KY", "MI", "NV", "AL", "AL", "CO", "NC", "CA", "MN", "CA", "FL", "NJ", "NE", "MO",
              "AK", "TX", "CA", "IA", "IL", "NJ", "IN", "LA", "GA", "CA", "OR", "OH", "TX", "PA", "OR", "FL", "LA",
              "TX", "NJ", "NC", "GA", "AZ", "TX", "AZ", "TX", "FL", "IL", "NC", "AL", "AZ", "AZ", "NV", "VA", "VA",
              "CA", "WA", "TX", "TX", "CA", "NH", "FL", "IN", "AZ", "TX", "MS", "WI", "WA", "CA", "TX", "MI", "CA",
              "VA", "CA", "CA", "ND", "WI", "TX", "ME", "CA", "FL", "TX", "NY", "CA", "CA", "FL", "IL", "AZ", "KS",
              "TX", "TX", "CA", "CT", "TN", "IA", "SD", "CA", "PA", "WA", "ID", "NC", "FL", "TN", "NC", "VA", "CA",
              "CA", "CT", "AZ", "CA", "CA", "FL", "CA", "CA", "OR", "NC", "CA", "NH", "IL", "VA", "CA", "IL", "CO",
              "IN", "LA", "TX", "AL", "GA", "CA", "FL", "TX", "GA", "KS", "CA", "CA", "CA", "TX", "MA", "CA", "IL",
              "WA", "KS", "IL", "TX", "NJ", "CA", "CO", "TX", "CA", "AZ", "AZ", "MO", "GA", "CA", "CO", "FL", "CA",
              "TX", "CA", "KS", "TX", "WV", "CA", "CA", "CO", "NM", "UT", "VA", "MI", "IL", "FL", "TX", "WA", "MI",
              "WA", "WA", "CA", "WI", "NC", "CT", "NJ", "VA", "CA", "AR", "WI", "OK", "CO", "TX", "TX", "CA", "TX",
              "CA", "CO", "UT", "MT", "MN", "MN", "SC", "MA", "TX", "IA", "CA", "FL", "MO", "UT", "IN", "CA", "CA",
              "SC", "CA", "CA", "ID", "CO", "CA", "FL", "FL", "IA", "WA", "NM", "CA", "MA", "CO", "IL", "CA", "OK",
              "FL", "OR", "VT", "GA", "OR", "TX", "OR", "CA", "NC", "CA", "TX", "CA", "IA", "FL", "CA", "TX", "CA",
              "NV", "TX", "CA", "CA", "CA", "CA", "CA", "CA", "CO", "WA", "CA", "CA", "TX", "IN", "WA", "TX", "TX",
              "CA", "FL", "MO", "NM", "OR", "KS", "UT", "CA", "UT", "WA", "CA", "MA", "CA", "IN", "FL", "GA", "CA",
              "FL", "MA", "VA", "CA", "MA", "OK", "MI", "MI", "CA", "OK", "MT", "SD", "VA", "SC", "CA", "CA", "CA",
              "CA", "MA", "GA", "FL", "CT", "CA", "MO", "MA", "IN", "CA", "IL", "TX", "IL", "CA", "CA", "AL", "CA",
              "CA", "CA", "NJ", "FL", "MN", "GA", "CA", "TX", "CA", "MI", "CA", "CA", "FL", "CA", "CA", "CA", "MI",
              "WA", "RI", "MA", "CA", "AR", "FL", "RI", "IL", "MI", "MN", "MA", "MN", "WY", "CA", "CA", "CA", "MO",
              "TX", "CO", "FL", "NY", "AR", "OH", "UT", "CA", "TX", "CA", "CA", "CA", "PA", "MI", "IN", "TX", "CA",
              "IN", "IL", "IL", "MI", "CA", "NJ", "IL", "CA", "IL", "MI", "CT", "WI", "RI", "FL", "CA", "DE", "CA",
              "NJ", "NJ", "IL", "NY", "CA", "LA", "NY"]

cities = ["New York", "Los Angeles", "Chicago", "Miami", "Dallas", "Philadelphia", "Houston", "Atlanta", "Washington",
          "Boston", "Phoenix", "Seattle", "San Francisco", "Detroit", "San Diego", "Minneapolis", "Tampa", "Denver",
          "Riverside", "Baltimore", "Las Vegas", "Portland", "San Antonio", "St. Louis", "Sacramento", "Orlando",
          "San Jose", "Cleveland", "Pittsburgh", "Austin", "Cincinnati", "Kansas City", "Indianapolis", "Columbus",
          "Charlotte", "Virginia Beach", "Milwaukee", "Providence", "Jacksonville", "Salt Lake City", "Nashville",
          "Richmond", "Memphis", "Raleigh", "New Orleans", "Louisville", "Oklahoma City", "Bridgeport", "Buffalo",
          "Fort Worth", "Hartford", "Tucson", "Omaha", "El Paso", "Honolulu", "McAllen", "Albuquerque", "Birmingham",
          "Dayton", "Rochester", "Fresno", "Allentown", "Tulsa", "Cape Coral", "Concord", "Colorado Springs",
          "Charleston", "Springfield", "Grand Rapids", "Mission Viejo", "Albany", "Knoxville", "Bakersfield", "Ogden",
          "Baton Rouge", "Akron", "New Haven", "Columbia", "Mesa", "Palm Bay", "Provo", "Worcester", "Murrieta",
          "Wichita", "Toledo", "Des Moines", "Long Beach", "Port St. Lucie", "Denton", "Madison", "Reno", "Little Rock",
          "Oakland", "Durham", "Winston-Salem", "Indio", "Palm Coast", "Chattanooga", "Spokane", "Syracuse",
          "Arlington", "Stockton", "Augusta", "Boise", "Oxnard", "Scranton", "Modesto", "Aurora", "Youngstown",
          "Fayetteville", "Anaheim", "Victorville", "Lancaster", "Greensboro", "Corpus Christi", "Fort Wayne",
          "Santa Ana", "Flint", "Fayetteville", "Jackson", "Santa Rosa", "Lansing", "Lexington", "Ann Arbor",
          "Henderson", "Huntsville", "Mobile", "Fort Collins", "Asheville", "Santa Clarita", "St. Paul", "Antioch",
          "Lakeland", "Trenton", "Lincoln", "Springfield", "Anchorage", "Plano", "Irvine", "Davenport", "Rockford",
          "Newark", "South Bend", "Shreveport", "Savannah", "Chula Vista", "Eugene", "Canton", "Lubbock", "Reading",
          "Salem", "St. Petersburg", "Lafayette", "Laredo", "Jersey City", "Concord", "Columbus", "Chandler",
          "McKinney", "Scottsdale", "Killeen", "Tallahassee", "Peoria", "Wilmington", "Montgomery", "Gilbert",
          "Glendale", "North Las Vegas", "Chesapeake", "Norfolk", "Fremont", "Kennewick", "Garland", "Irving",
          "Visalia", "Nashua", "Hialeah", "Evansville", "Avondale", "Brownsville", "Gulfport", "Appleton", "Tacoma",
          "San Bernardino", "College Station", "Kalamazoo", "Thousand Oaks", "Roanoke", "Fontana", "Moreno Valley",
          "Fargo", "Green Bay", "Amarillo", "Portland", "Santa Barbara", "Gainesville", "Frisco", "Yonkers", "Glendale",
          "Huntington Beach", "Deltona", "Aurora", "Tempe", "Overland Park", "Grand Prairie", "Waco", "Salinas",
          "Waterbury", "Clarksville", "Cedar Rapids", "Sioux Falls", "Ontario", "Erie", "Vancouver", "Nampa",
          "Gastonia", "Fort Lauderdale", "Murfreesboro", "High Point", "Newport News", "Rancho Cucamonga", "Hemet",
          "Danbury", "Peoria", "Oceanside", "Elk Grove", "Pembroke Pines", "Vallejo", "Garden Grove", "Medford", "Cary",
          "Corona", "Manchester", "Champaign", "Alexandria", "Hayward", "Springfield", "Lakewood", "Lafayette",
          "Lake Charles", "Odessa", "Tuscaloosa", "Warner Robins", "Palmdale", "Hollywood", "Midland", "Macon",
          "Kansas City", "Sunnyvale", "Pomona", "Escondido", "Pasadena", "New Bedford", "Fairfield", "Naperville",
          "Bellevue", "Topeka", "Joliet", "Beaumont", "Paterson", "Merced", "Pueblo", "Tyler", "Torrance", "Yuma",
          "Surprise", "Columbia", "Athens", "Roseville", "Thornton", "Miramar", "Pasadena", "Mesquite", "Santa Maria",
          "Olathe", "Carrollton", "Charleston", "Orange", "Fullerton", "Greeley", "Las Cruces", "West Valley City",
          "Hampton", "Warren", "Bloomington", "Coral Springs", "Round Rock", "Yakima", "Sterling Heights", "Kent",
          "Bellingham", "Santa Clara", "Racine", "Greenville", "Stamford", "Elizabeth", "Lynchburg", "Simi Valley",
          "Fort Smith", "Kenosha", "Norman", "Boulder", "Abilene", "Pearland", "Berkeley", "Richardson", "Redding",
          "Arvada", "St. George", "Billings", "Rochester", "Duluth", "Rock Hill", "Cambridge", "Sugar Land",
          "Iowa City", "Chico", "Clearwater", "Independence", "West Jordan", "Bloomington", "El Monte", "Carlsbad",
          "North Charleston", "Temecula", "Clovis", "Meridian", "Westminster", "Costa Mesa", "Pompano Beach",
          "West Palm Beach", "Waterloo", "Everett", "Santa Fe", "Downey", "Lowell", "Centennial", "Elgin", "Richmond",
          "Broken Arrow", "Miami Gardens", "Bend", "Burlington", "Sandy Springs", "Gresham", "Lewisville", "Hillsboro",
          "San Buenaventura", "Jacksonville", "Inglewood", "League City", "Turlock", "Sioux City", "Davie", "Daly City",
          "Allen", "West Covina", "Sparks", "Wichita Falls", "San Mateo", "Norwalk", "Rialto", "Manteca", "El Cajon",
          "Burbank", "Longmont", "Renton", "Vista", "Vacaville", "Edinburg", "Carmel", "Spokane Valley", "San Angelo",
          "Longview", "Tracy", "Boca Raton", "Lee's Summit", "Rio Rancho", "Beaverton", "Lawrence", "Orem",
          "San Marcos", "Sandy", "Federal Way", "Hesperia", "Brockton", "Compton", "Fishers", "Sunrise", "Roswell",
          "Menifee", "Plantation", "Quincy", "Portsmouth", "Chino", "Lynn", "Edmond", "Dearborn", "Livonia",
          "South Gate", "Lawton", "Missoula", "Rapid City", "Suffolk", "Mount Pleasant", "Carson", "Livermore",
          "Westminster", "Santa Monica", "Fall River", "Albany", "Miami Beach", "Norwalk", "San Leandro", "O'Fallon",
          "Newton", "Muncie", "Citrus Heights", "Decatur", "Bryan", "Waukegan", "Hawthorne", "Redwood City", "Hoover",
          "Lake Forest", "Napa", "Whittier", "Clifton", "Largo", "Bloomington", "Johns Creek", "Newport Beach",
          "Mission", "Milpitas", "Troy", "Chino Hills", "Alhambra", "Melbourne", "Mountain View", "Buena Park",
          "Pleasanton", "Westland", "Auburn", "Cranston", "Somerville", "Folsom", "Springdale", "Deerfield Beach",
          "Warwick", "Cicero", "Farmington Hills", "Brooklyn Park", "Lawrence", "Plymouth", "Cheyenne", "Tustin",
          "Lakewood", "Perris", "St. Joseph", "Pharr", "Loveland", "Boynton Beach", "New Rochelle", "Jonesboro",
          "Parma", "Layton", "Alameda", "Baytown", "Upland", "Bellflower", "San Ramon", "Bethlehem", "Wyoming",
          "Hammond", "Missouri City", "Baldwin Park", "Gary", "Arlington Heights", "Bolingbrook", "Rochester Hills",
          "Union City", "Camden", "Evanston", "Apple Valley", "Schaumburg", "Southfield", "New Britain", "Waukesha",
          "Pawtucket", "Lauderhill", "Redlands", "Wilmington", "Lynwood", "Passaic", "Union City", "Palatine",
          "Mount Vernon", "Redondo Beach", "Kenner", "Schenectady"]


# process the csv and read the specified rows.
# each row is a 'metric' under the column 'metric_name' in the csv file
def process_csv():
    os.chdir("..")

    health = pd.read_csv("data/Culture/Health Data.csv")
    compare_cities_health(health, "Park access")
    compare_cities_health(health, "Walkability")

    # this column is actually being stored as 'Close Access to Healthy Foods'. see bottom last lines
    compare_cities_health(health, "Limited access to healthy foods")

# compare the provided metric and its total population with the 500 cities list
def compare_cities_health(df, metric_name):
    df = df.loc[df['metric_name'] == metric_name]

    # we are looking for the rows which contain 'total population' under column 'group_name'
    # this is because the file splits different groups such as black, white, asian etc.
    # total population includes all of the groups
    df = df.loc[df['group_name'] == "total population"]

    list_states = list(df["state_abbr"])
    list_cities = list(df["city_name"])

    # lists of cities and states that are not a direct match
    unmatched_cities = []
    unmatched_states = []

    # store the value when cities match
    city_values = []

    count = 0
    # compare cities by doing a direct match using ==
    for x in range(500):
        found = False
        for index, (city, state) in enumerate(zip(list_cities, list_states)):
            if city == cities[x]:
                if state == state_abbr[x]:
                    count = count + 1
                    found = True
                    if metric_name == "Limited access to healthy foods":
                        if df["est"].values[index] == df["est"].values[index]:
                            city_values.append(str(round(100 - df["est"].values[index])) + "%")
                        else:
                            city_values.append(str(df["est"].values[index]) + "%")
                    else:
                        city_values.append(str(df["est"].values[index]) + "%")
                    break
        if found is False:
            unmatched_cities.append(cities[x])
            unmatched_states.append(state_abbr[x])

    # match cities by checking if it exists as the first # of characters
    for x in range(500):
        for city, state in zip(unmatched_cities, unmatched_states):
            if cities[x].strip() == city[:len(cities[x])]:
                if state == state_abbr[x]:
                    count = count + 1
                    if metric_name == "Limited access to healthy foods":
                        if df["est"].values[index] == df["est"].values[index]:
                            city_values.append(str(round(100 - df["est"].values[index])) + "%")
                        else:
                            city_values.append(str(df["est"].values[index]) + "%")
                    else:
                        city_values.append(str(df["est"].values[index]) + "%")
                    break

    print("cities matched: " + str(count))

    df = pd.read_csv('data/final500Cities.csv')
    if metric_name == "Limited access to healthy foods":
        df["Close Access to Healthy Foods"] = city_values
    else:
        df[metric_name] = city_values
    print(df)
    df.to_csv('data/final500Cities.csv', mode='w', index=False)


process_csv()
