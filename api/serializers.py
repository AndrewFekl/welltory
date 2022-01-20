from rest_framework import serializers

class RowDataSerializer(serializers.Serializer):
    x = serializers.JSONField()
    y = serializers.JSONField()

class UserDataSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    data = RowDataSerializer()