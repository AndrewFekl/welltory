from rest_framework import serializers
from .models import UserCorrelation


class UserCorrelationSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCorrelation
        fields = ('user_id', 'x_data_type', 'y_data_type', 'correlation')


