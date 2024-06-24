import threading
from geopy.geocoders import Nominatim
import json

#for git

from django.http import JsonResponse
import openrouteservice as ors
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView


from map.consumer import get_coord_from_kafka, coord_queue
from map.models import Map
from orders.models import Order


def index(request):
    # Возвращение шаблона с данными карты
    return render(request, 'main/index.html')


class MapView(CreateAPIView):
    def get(self, request, order_id):
        #получаем адрес пользователя
        order = Order.objects.filter(id=order_id)[0]
        orders_coords = Map.objects.all()
        current_coords = None
        for coords in orders_coords:
            if coords.order.id == order.id:
                current_coords = coords
        if current_coords is None:
            address_finish = order.user.address
            address_start = "Россия, Воронеж, Университетская площадь, 1"
            #переделываем адрес в коордиинаты (api)
            geolocator = Nominatim(user_agent="geoapiExercises")
            loc_finish = geolocator.geocode(address_finish)
            loc_start = geolocator.geocode(address_start)
            if (loc_finish is None) or (loc_start is None):
                return Response({'answer': 'ошибка получения координат адресов '}, status=status.HTTP_400_BAD_REQUEST, headers={"charset": "utf-8"})
            current_coords = Map.objects.create(order=order, start_longitude=loc_start.longtitude, start_latitude=loc_start.latitude,
                                                end_longitude=loc_finish.longitude, end_latitude=loc_finish.latitude)
        start_coord = [current_coords.start_latitude, current_coords.start_longitude]  # стартовая точка пути - хранится в бд
        end_coord = [current_coords.end_latitude, current_coords.end_longitude]  # финишная точка пути - хранится в бд

        coords = [start_coord[::-1], end_coord[::-1]]
        client = ors.Client(key='5b3ce3597851110001cf624860bbe2ce295c433185dd45a4f3e1ae18')
        route = client.directions(coordinates=coords,
                                  profile='driving-car',
                                  format='geojson')

        courier_coord = get_courier_coordinates(order.courier.id)

        route = route['features'][0]['geometry']['coordinates']
        route = [[sublist[1], sublist[0]] for sublist in route]
        data = [
            {'start_coord': start_coord},
            {'end_coord': end_coord},
            {'route_coord': route}
        ]
        if courier_coord is not None:
            data.append({'courier_coord': courier_coord})

        return JsonResponse(data, safe=False)

def get_courier_coordinates(courier_id):
    # Запуск потока для получения координат из Kafka
    kafka_thread = threading.Thread(target=get_coord_from_kafka)
    kafka_thread.start()
    for data in coord_queue.queue:
        print('data =', data)
        user_id = int(data[0])
        print('user_id =', user_id)
        if user_id == courier_id:
            delivery_coord = [float(coord) for coord in data[1].split(' ', maxsplit=1)]
            print('new_coord =', delivery_coord)
            return delivery_coord

#забрать getpoint из index.html