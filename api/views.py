from .models import UserCorrelation
from .serializers import UserCorrelationSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from.schemas import VALIDATION_SCHEMA


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def calculate_view(request):
    """ Метод принимает в теле запроса данные пользователя в json формате,
    вычисляет статистики (ковариация и корреляция по Пирсону) и записывает их в базу"""

    # Проверяем валидность данных, вычисляем статистики и переводим в формат модели БД
    try:
        validate(instance=request.data, schema=VALIDATION_SCHEMA)
        output_dict = UserCorrelation.data_preparation(request.data)

    except json.JSONDecodeError as exc:
        return Response(f"Bad JSON, {exc.message}", status=400)

    except ValidationError as exc:
        return Response(f"Validation Error, {exc.message}", status=400)


    # Запись данных в базу
    data_set = UserCorrelationSerializer(data=output_dict)

    if data_set.is_valid():
        data_set.save()

    return Response(status=201)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
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


