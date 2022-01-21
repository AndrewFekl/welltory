from django.db import models


# Тестовая модель данных
class TestModel:

    def __init__(self, user_id, data):
        self.user_id = user_id
        self.data = data


class UserData(models.Model):

    user_id = models.IntegerField(null=False)
    data_type = models.CharField(max_length=100)
    data = models.JSONField()


class UserCorrelation(models.Model):

    user_id = models.JSONField(null=False)
    x_data_type = models.CharField(max_length=100)
    y_data_type = models.CharField(max_length=100)
    correlation = models.JSONField()

