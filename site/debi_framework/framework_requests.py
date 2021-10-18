class GetRequests:
    @staticmethod
    def parse_input_data(data: str):
        result = dict()
        if data:
            # Разделяем параметры парама через &
            params = data.split('&')
            for item in params:
                # Парсим ключ и значение словаря через =
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(env_dict):
        # Получаем параметры запроса
        query_string = env_dict['QUERY STRING']
        # переводим полученные параметры в словарь
        request_params = GetRequests.parse_input_data(query_string)
        return request_params


class PostRequests:
    @staticmethod
    def parse_input_data(data: str):
        result = dict()
        if data:
            # Разделяем параметры парама через &
            params = data.split('&')
            for item in params:
                # Парсим ключ и значение словаря через =
                k, v = item.split('=')
                result[k] = v
        return result

    def parse_input_data(self):
        pass

    @staticmethod
    def get_wsgi_input_data(env_dict)->bytes:
        # Длина тела данных
        content_length_str = env_dict['CONTENT_LENGTH']
        # переводим в целое int
        content_length = int(content_length_str) if content_length_str else 0
        # считываем данные если они имеются
        data = env_dict['wsgi.input'].read(content_length) if content_length else b''
        return data

    def parse_wsgi_input_data(self, data:bytes)->dict:
        result=dict()
        if data:
            # Декодируем данные
            data_str = data.decode(encoding='utf-8')
            # Собираем их в словарь
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, env_dict):
        # получаем данные
        data = self.get_wsgi_input_data(env_dict)
        # превращаем байтовые данные в словарь
        data = self.parse_wsgi_input_data(data)
        return data

    @staticmethod
    def get_request_params(env_dict):
        pass
