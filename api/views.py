from django.shortcuts import render
from .models import TestModel
from .serializers import UserDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def test_view(request):
    data = {
        'x_data_type': 'temperature',
        'y_data_type': 'humidity',
        'x': [
            {
                'date': '2022-01-07',
                'value': 5,
            }
        ],
        'y': [
            {
                'date': '2022-01-07',
                'value': 30,
            },
            {
                'date': '2022-01-08',
                'value': 28,
            }
        ]
    }

    test_model = TestModel(user_id=1, data=data)
    serializer = UserDataSerializer(test_model)

    return Response(serializer.data)
