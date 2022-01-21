from django.shortcuts import render
from .models import TestModel
from .serializers import UserDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .statistics import Statistics

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


def corr_view(request):

    data = {
        "x_data_type": "sleep_hours",
        "y_data_type": "morning_pulse",
        "x": [
            {
                "date": "2022-01-14",
                "value": 9.7
            },
            {
                "date": "2022-01-08",
                "value": 9.0
            },
            {
                "date": "2022-02-01",
                "value": 6.5
            },
            {
                "date": "2022-01-11",
                "value": 8.6
            },
            {
                "date": "2022-01-25",
                "value": 6.0
            },
            {
                "date": "2022-01-04",
                "value": 9.9
            },
            {
                "date": "2022-01-27",
                "value": 5.2
            },
            {
                "date": "2022-01-03",
                "value": 5.3
            },
            {
                "date": "2022-01-02",
                "value": 7.7
            },
            {
                "date": "2022-01-19",
                "value": 6.0
            },
            {
                "date": "2022-01-12",
                "value": 6.4
            },
            {
                "date": "2022-01-26",
                "value": 5.2
            },
            {
                "date": "2022-01-18",
                "value": 5.6
            },
            {
                "date": "2022-01-16",
                "value": 9.0
            },
            {
                "date": "2022-01-23",
                "value": 5.4
            },
            {
                "date": "2022-01-09",
                "value": 5.6
            },
            {
                "date": "2022-01-06",
                "value": 6.9
            },
            {
                "date": "2022-01-17",
                "value": 9.3
            },
            {
                "date": "2022-01-15",
                "value": 9.1
            },
            {
                "date": "2022-01-13",
                "value": 7.3
            }
        ],
        "y": [
            {
                "date": "2022-01-16",
                "value": 96
            },
            {
                "date": "2022-01-31",
                "value": 77
            },
            {
                "date": "2022-01-01",
                "value": 45
            },
            {
                "date": "2022-01-05",
                "value": 60
            },
            {
                "date": "2022-01-08",
                "value": 47
            },
            {
                "date": "2022-02-01",
                "value": 97
            },
            {
                "date": "2022-01-26",
                "value": 93
            },
            {
                "date": "2022-01-23",
                "value": 68
            },
            {
                "date": "2022-01-13",
                "value": 49
            },
            {
                "date": "2022-01-06",
                "value": 44
            },
            {
                "date": "2022-01-29",
                "value": 75
            },
            {
                "date": "2022-01-10",
                "value": 88
            },
            {
                "date": "2022-01-20",
                "value": 54
            },
            {
                "date": "2022-01-11",
                "value": 82
            },
            {
                "date": "2022-01-27",
                "value": 62
            },
            {
                "date": "2022-01-19",
                "value": 57
            },
            {
                "date": "2022-01-18",
                "value": 82
            },
            {
                "date": "2022-01-17",
                "value": 65
            },
            {
                "date": "2022-01-03",
                "value": 64
            },
            {
                "date": "2022-01-28",
                "value": 50
            }
        ]
    }


    statistics = Statistics(data)
    df = statistics.get_clean_dataframe()
    p_correlation = statistics.get_pirson_correlation(df)
    covariance = statistics.get_covariance(df)

    return render(request, 'main.html', {'p_correlation': p_correlation, 'covariance': covariance})


