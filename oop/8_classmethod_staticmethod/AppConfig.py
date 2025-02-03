import json


class AppConfig:
    data = {}

    def __init__(self, file='app_config.json'):
        if not AppConfig.data:
            self.load_config(file)

    @classmethod
    def load_config(cls, file='app_config.json'):
        with open(file) as json_data:
            cls.data = json.load(json_data)

    @classmethod
    def get_config(cls, value: str):
        key_parts = value.split('.')
        result = cls.data

        for key in key_parts:
            if key in result:
                result = result[key]
            else:
                return None

        return result
# Загрузка конфигурации при запуске приложения
AppConfig.load_config('app_config.json')

# Получение значения конфигурации
assert AppConfig.get_config('database') == {
    'host': '127.0.0.1', 'port': 5432,
    'database_name': 'postgres_db',
    'user': 'owner',
    'password': 'ya_vorona_ya_vorona'}
assert AppConfig.get_config('database.user') == 'owner'
assert AppConfig.get_config('database.password') == 'ya_vorona_ya_vorona'
assert AppConfig.get_config('database.pass') is None
assert AppConfig.get_config('password.database') is None

config = AppConfig()
assert config.get_config('max_connections') == 10
assert config.get_config('min_connections') is None

conf = AppConfig()
assert conf.get_config('max_connections') == 10
assert conf.get_config('database.user') == 'owner'
print(conf.get_config('database.host'))
assert conf.get_config('database.host') == '127.0.0.1'
assert conf.get_config('host') is None

print('Good')
