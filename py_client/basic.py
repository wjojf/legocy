import requests
import pprint 
import os


printer = pprint.PrettyPrinter()


HEADERS = {
    'Authorization': f'Bearer TOKEN_HERE'
}
print(HEADERS)

endpoint = 'http://localhost:8000/api/'

endpoint_series = endpoint + 'series/'
endpoint_create_series = endpoint_series + 'create/'


endpoint_sets = endpoint + 'sets/'
endpoint_set_detail = endpoint_sets + '1'
endpoint_create_set = endpoint_sets + 'create/'
endpoint_update_set = endpoint_sets + 'update/{pk}'

endpoint_images = endpoint + 'images/'
endpoint_marketitems = endpoint + 'marketitems/'
endpoint_marketitems_create = endpoint_marketitems + 'create/'



series_response = requests.get(
    endpoint_series,
    headers=HEADERS
)
print(series_response.json())


# home_response = requests.get(
#     endpoint,
#     headers=HEADERS,
#     json={'test': True}
# )
# printer.pprint(home_response.json())


sets_response = requests.get(
    endpoint_sets,
    headers=HEADERS,
    json={"filter_": {"n_details__gte": 2000}}
)
printer.pprint(sets_response.json())


# images_response = requests.get(
#     endpoint_images,
#     json={'message': 'Hello, World!'}
# )
# printer.pprint(images_response.json())


# marketitems_response = requests.get(
#     endpoint_marketitems,
#     json={"filter_": {
#         "active": True,
#         "lego_set__set_number": 76240
#     }},
#     headers=HEADERS
# )
# printer.pprint(marketitems_response.json())



# set_response = requests.get(
#     endpoint_set_detail,
#     headers=HEADERS
# )
# printer.pprint(set_response.json())


TEST_DATA = {
    'name': 'Creator'
}

# create_series_response = requests.post(
#     endpoint_create_series,
#     headers=HEADERS,
#     data = TEST_DATA
# )
# print(create_series_response.json())


# TEST_SET_DATA = {
#     'series': 1,
#     'set_number': 76139,
#     'title': 'Batmobile 1989',
#     'n_details': 3308
# }

# create_set_response = requests.post(
#     endpoint_create_set,
#     headers=HEADERS,
#     data=TEST_SET_DATA
# )
# print(create_set_response.json())

TEST_UPDATE_DATA = {
    'series': 4
}
pk = 1

# update_response = requests.put(
#     endpoint_update_set.format(pk=pk),
#     headers=HEADERS,
#     data=TEST_UPDATE_DATA
# )
# print(update_response.json())


# TEST_MARKETITEM_DATA = {
#     'seller': 1,
#     'lego_set': 4,
#     'price': 500,
#     'currency': 'USD'
# }
# create_item_response = requests.post(
#     endpoint_marketitems_create,
#     headers=HEADERS,
#     data=TEST_MARKETITEM_DATA
# )
# print(create_item_response.json())