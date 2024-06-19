import threading
import json

#66721f857e5fe423578274mpz03ab15 apikey geocode

from django.http import JsonResponse
import openrouteservice as ors
from django.shortcuts import render

from djangoProject.consumer import get_coord_from_kafka, coord_queue


def index(request):
    # Возвращение шаблона с данными карты
    return render(request, 'main/index.html')


def get_route_data(request):
    start_coord = [51.6564867, 39.2053785]  # стартовая точка пути - хранится в бд
    end_coord = [51.6675548, 39.1915629]  # финишная точка пути - хранится в бд

    coords = [start_coord[::-1], end_coord[::-1]]
    client = ors.Client(key='5b3ce3597851110001cf624860bbe2ce295c433185dd45a4f3e1ae18')
    route = client.directions(coordinates=coords,
                              profile='driving-car',
                              format='geojson')

    # Запуск потока для получения координат из Kafka
    kafka_thread = threading.Thread(target=get_coord_from_kafka)
    kafka_thread.start()
    data = coord_queue.get()
    print('data =', data)
    user_id = int(data[0])
    print('user_id =', user_id)
    delivery_coord = [float(coord) for coord in data[1].split(' ', maxsplit=1)]
    print('new_coord =', delivery_coord)

    route = route['features'][0]['geometry']['coordinates']
    route = [[sublist[1], sublist[0]] for sublist in route]
    data = [
        {'start_coord': start_coord},
        {'end_coord': end_coord},
        {'routeCoordinates': route}
    ]
    '''
    user_id здесь - id курьера, который взял заказ;
    он должен совпадать с полученными данными,
    чтобы клиенту показывались гео данные того курьера,
     который принял его заказ - id получать из бд
    '''
    if user_id == 1:
        data.append({'delivery_coord': delivery_coord})

    return JsonResponse(data, safe=False)
