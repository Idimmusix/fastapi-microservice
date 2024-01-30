from redis_om import get_redis_connection
from decouple import config

redis = get_redis_connection(
        host = config("REDIS_HOST"),
        port=config("REDIS_PORT"),
        decode_responses=True
        )
