import os


class Config:
    def __init__(self):
        self.__API_PORT: int = int(os.getenv('API_PORT', '8000'))
        self.__POSTGRES_USER = os.getenv('POSTGRES_USER', 'user')
        self.__POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'password')
        self.__POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'postgres')
        self.__POSTGRES_PORT = int(os.getenv('POSTGRES_PORT', '5432'))
        self.__POSTGRES_DB = os.getenv('POSTGRES_DB', 'db')

    @property
    def api_port(self) -> int:
        return self.__API_PORT

    @property
    def postgres_user(self) -> str:
        return self.__POSTGRES_USER

    @property
    def postgres_password(self) -> str:
        return self.__POSTGRES_PASSWORD

    @property
    def postgres_host(self) -> str:
        return self.__POSTGRES_HOST

    @property
    def postgres_port(self) -> int:
        return self.__POSTGRES_PORT

    @property
    def postgres_db(self) -> str:
        return self.__POSTGRES_DB
