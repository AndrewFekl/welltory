from django.db import models
from .statistics import Statistics


class UserCorrelation(models.Model):

    user_id = models.JSONField(null=False)
    x_data_type = models.CharField(max_length=100)
    y_data_type = models.CharField(max_length=100)
    correlation = models.JSONField()

    @staticmethod
    def data_preparation(request_data):

        user_id = request_data['user_id']
        data = request_data['data']

        statistics = Statistics(data)
        x_data_type, y_data_type = statistics.get_data_types()
        df = statistics.get_clean_dataframe()
        p_correlation = statistics.get_pirson_correlation(df)
        covariance = statistics.get_covariance(df)

        output_dict = {
            'user_id': user_id,
            'x_data_type': x_data_type,
            'y_data_type': y_data_type,
            'correlation': {
                'value': covariance,
                'p_value': p_correlation
            }
        }

        return output_dict





