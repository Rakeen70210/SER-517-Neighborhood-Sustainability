from server.controllers import DomainController, SubdomainController
from server.models.City import City
from server.models.abstract_base_classes.Domain import Domain
from server.models.abstract_base_classes.Subdomain import Subdomain


def get_sustainability_index(city_name, state_id, db_session):
    node, info = db_session.write_transaction(find_city_by_name_and_state_id, city_name, state_id)
    city = City.get_city(node)
    print(city)
    return {
        "city": city,
        "index": 90
    }


def create_city_tx(tx, city):  # tx is passed when db_session.write_transaction(CityController.create_city_tx, city)
    statement = __get_create_statement(city)
    result = tx.run(statement)
    record = result.single()
    value = record.value()
    info = result.consume()
    return value, info


def merge_city_tx(tx, city):  # tx is passed when db_session.write_transaction(CityController.create_city_tx, city)
    # print(city.name)
    statement = __get_merge_statement(city)
    result = tx.run(statement)
    record = result.single()
    value = record.value()
    info = result.consume()
    return value, info


def index_city(tx):
    statement = __get_index_statement()
    result = tx.run(statement)
    record = result.single()
    value = record.value()
    info = result.consume()
    return value, info


def find_city_by_id(tx, city):
    statement = __get_find_by_city_id_statement(city.city_id)
    result = tx.run(statement)
    record = result.single()
    value = record.value()
    info = result.consume()
    return value, info


def find_city_by_name_and_state_id(tx, city_name, state_id):
    statement = __get_find_by_cityname_and_state_id_statement(city_name, state_id)
    print(f'executing {statement}')
    result = tx.run(statement)
    print(f'results {result}')
    record = result.single()
    value = record.value()
    info = result.consume()
    return value, info


def update_city(city, db_session):
    statement = __get__update_statement(city.city_id, city)
    print(f'executing {statement}')
    result = db_session.run(statement)
    print(f'results {result}')
    return result


def delete_city(city, db_session):
    statement = __get_delete_statement(city)
    print(f'executing {statement}')
    result = db_session.run(statement)
    print(f'results {result}')
    return result


# Calculates and updates scores for city
def update_city_score(city, db_session):
    city_update_statement = __get__update_statement(city.city_id, {'score': city.score})
    # print(f'executing {city_update_statement}')
    result = db_session.run(city_update_statement)
    # print(f'results {result}')

    for attribute in dir(city):
        if issubclass(getattr(city, attribute).__class__, Domain):
            domain_obj = getattr(city, attribute)
            info = db_session.write_transaction(DomainController.merge_domain_tx, city, domain_obj)
            # print(info)

            for domain_attr in dir(domain_obj):
                if issubclass(getattr(domain_obj, domain_attr).__class__, Subdomain):
                    subdomain_obj = getattr(domain_obj, domain_attr)
                    info2 = db_session.write_transaction(SubdomainController.merge_subdomain_tx, city, domain_obj,
                                                         subdomain_obj)
                    # print(info2)


def get_all_cities(db_session, page, limit):
    # json array
    cities_all = []

    # the count of all cities in the db
    city_count_result = db_session.run("MATCH (city:City) return COUNT(city)")
    city_count = 0

    for count in city_count_result:
        city_count = count[0]

    # if page passed in is higher than max_page set to max_page
    if page > city_count:
        page = city_count - 1

    # print(page)
    # print(limit)
    # print((
    #         "MATCH (city:City) RETURN city.city_id, city.name, city.state, city.state_id, city.latitude, city.longitude, city.score ORDER BY city.state SKIP " + str(page) + " LIMIT " + str(limit)))

    cities = db_session.run(
        "MATCH (city:City) RETURN city.city_id, city.name, city.state, city.state_id, city.latitude, city.longitude, city.score ORDER BY city.state SKIP " + str(
            page) + " LIMIT " + str(limit))

    for city in cities:
        json_obj = {'city_id': city[0], 'name': city[1], 'state': city[2], 'state_id': city[3], 'latitude': city[4],
                    'longitude': city[5], 'score': city[6]}
        cities_all.append(json_obj)

    return cities_all


# -------------- Helper functions ---------------------------------------------------------------------#
def __get_create_statement(city):
    return 'CREATE (a:City {city_id : "' + city.city_id + '", name : "' + city.name + '", state : "' + city.state + '", state_id : "' + city.state_id + '", county : "' + city.county + '", county_fips : "' + city.county_fips + '", latitude : ' + city.latitude + ', longitude : ' + city.longitude + ', population : ' + city.population + ', density : ' + city.density + ', zips : "' + city.zips + '" }) RETURN a'


def __get_merge_statement(city_dict):
    merge = 'MERGE (a:City {city_id : "' + city_dict['city_id'] + '"}) '

    on_create = "\nON CREATE SET"
    on_match = "\nON MATCH SET"

    for key in city_dict:
        on_create += ('\na.' + key + ' = "' + city_dict[key] + '",')
        on_match += ('\na.' + key + ' = "' + city_dict[key] + '",')

    merge += on_create[:-1]
    merge += on_match[:-1]

    merge += '\nRETURN a;'
    # print(merge)
    return merge


def __get_index_statement():
    return 'MATCH (a:City) RETURN a'


# def __get_create_bulk_statement(city):
#     return f"({city.name+city.city_id}:City {{city_id : {city.city_id}, name : '{city.name}', state : '{city.state}', state_id : '{city.state_id}', county : '{city.county}', county_fips : {city.county_fips}, latitude : {city.latitude}, longitude : {city.longitude}, population : {city.population}, density : {city.density}, zips : '{city.zips}' }})"


def __get_find_by_city_id_statement(city_id):
    return f"MATCH (a:City {{city_id: {city_id}}}) RETURN a"


def __get_find_by_cityname_and_state_id_statement(city_name, state_id):
    return 'MATCH (a:City {name: "' + city_name + '", state_id: "' + state_id + '"}) RETURN a'


def __get_delete_statement(city):
    return f"MATCH (a:City {{city_id: {city.city_id} }}) DELETE a"


def __get__update_statement(city_id, details):
    if len(details) == 0: raise ValueError("Details cannot be empty")

    retVal = f"MATCH (a:City {{city_id : '{int(city_id)}'}}) SET "
    for key, val in details.items():
        if key == "city_id":
            continue
        retVal += f"a.{key} = {val}"

    return retVal + " RETURN a"
