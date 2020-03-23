# -*- coding: utf-8 -*-

"""Documentation file database.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from dataclasses import dataclass, field
from typing import NoReturn, Text, Callable, Dict
from redis import ConnectionPool, Redis, ConnectionError

# =============================================================================
# CLASS - SINGLETON 
# =============================================================================

class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs) -> Callable:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# =============================================================================
# CLASS - BASE REDIS
# =============================================================================

@dataclass(init=True, repr=True, eq=False, order=False, unsafe_hash=False, frozen=False)
class BaseRedis(metaclass=Singleton):
    _host: str = field(repr=True, default="cache")
    _port: int = field(repr=True, default=6379)
    _database: str = field(repr=True, default="")
    _password: str = field(repr=False, default="Redis2019!")
    charset: str = field(repr=True, default="utf-8")

    @property
    def host(self) -> Text:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @property
    def database(self) -> Text:
        return self._database

    @property
    def password(self) -> Text:
        return self._password

    @property
    def pool(self) -> ConnectionPool:
        if self.database:
            return ConnectionPool(host=self.host, port=self.port, password=self.password, database=self.database, charset=self.charset)
        else:
            return ConnectionPool(host=self.host, port=self.port, password=self.password, charset=self.charset)  

# =============================================================================
# CLASS - REDIS CONTROLLER
# =============================================================================

class RedisController(BaseRedis):

    def get_redis_connection(self) -> Redis:
        try:
            self._conn = Redis(connection_pool=self.pool, socket_connect_timeout=1000)
        except ConnectionError:
            raise ConnectionError()

    def info(self) -> Dict:
        return self.conn.info()

    def instance_size(self) -> int:
        return self.info()["used_memory"]

    def set(self, key, value) -> NoReturn:
        self.conn.set(key, value)

    def get(self, key):
        return self.conn.get(key)

    def mset(self, mapping: Dict) -> NoReturn:
        self.conn.mset(mapping)

    def lpush(self, name, values) -> NoReturn:
        self.conn.lpush(name, values)
        
    def lrange(self, name, start, end):
        return self.conn.lrange(name, start, end)

    @property
    def conn(self) -> Redis:
        """
        Se esse objeto não tiver um atributo de conexão, então retornamos uma conexão.

        O método hasattr() retornará true se um objeto tiver o atributo nomeado especificado e false se não tiver.
        """
        if not hasattr(self, "_conn"):
            self.get_redis_connection()
        return self._conn
