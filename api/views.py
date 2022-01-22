from .models import UserCorrelation
from .serializers import UserCorrelationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
def calculate_view(request):
    """ Метод принимает в теле запроса данные пользователя в json формате,
    вычисляет статистики (ковариация и корреляция по Пирсону) и записывает их в базу"""

    # Преобразование данных в формат модели и вычисление статистик
    output_dict = UserCorrelation.data_preparation(request.data)

    # Запись данных в базу
    data_set = UserCorrelationSerializer(data=output_dict)

    if data_set.is_valid():
        data_set.save()

    return Response(status=201)


@api_view(['GET'])
def correlation_view(request):
    """ Метод принимает GET запрос с параметрами и возвращает соответствующие статистики """

    user_id = int(request.GET['user_id'])
    x_data_type = request.GET['x_data_type']
    y_data_type = request.GET['y_data_type']

    try:
        statistical_data = UserCorrelation.objects.get(user_id=user_id, x_data_type=x_data_type, y_data_type=y_data_type)
    except ObjectDoesNotExist:
        return Response(status=404)

    serializer = UserCorrelationSerializer(statistical_data)

    return Response(serializer.data)


