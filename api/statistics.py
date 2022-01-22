import pandas as pd


class Statistics:

    def __init__(self, data_dict):
        self.data_dict = data_dict


    def get_data_types(self):

        x_data_type = self.data_dict['x_data_type']
        y_data_type = self.data_dict['y_data_type']

        return x_data_type, y_data_type


    def get_pirson_correlation(self, data_frame):
        """ Принимает на вход pandas dataframe, где первая колонка - даты,
        вторая и третья соответственно массивы данных для вычисления корреляции"""

        pirson_corr = data_frame.iloc[:, 1].corr(data_frame.iloc[:, 2])

        return pirson_corr


    def get_covariance(self, data_frame):
        """ Принимает на вход pandas dataframe, где первая колонка - даты,
        вторая и третья соответственно массивы данных для вычисления ковариации"""

        covariance = data_frame.iloc[:, 1].cov(data_frame.iloc[:, 2])

        return covariance


    def get_clean_dataframe(self):
        """ Функция берет инициированный при создании экземпляра класса словарь
        и возвращает pandas dataframe по совпадающим датам без пропуска данных"""

        # Формирование массивов данных для очищенного датафрейма
        x_data = {'date': [], 'value': []}
        y_data = {'date': [], 'value': []}

        for data in self.data_dict['x']:

            x_data['date'] = x_data['date'] + [data['date']]
            x_data['value'] = x_data['value'] + [data['value']]

        for data in self.data_dict['y']:
            y_data['date'] = y_data['date'] + [data['date']]
            y_data['value'] = y_data['value'] + [data['value']]

        # Создадим датафреймы данных x и y и сольем их в один по совпадающим датам
        x_df = pd.DataFrame(x_data)
        y_df = pd.DataFrame(y_data)
        data_frame = pd.merge(x_df, y_df, on='date', how='inner')
        # Возвращаем датафрейм без пропуска данных
        return data_frame.dropna()



