import psycopg

from finopsai.config import settings


def database_is_ready() -> bool:
    try:
        with psycopg.connect(settings.database_url, connect_timeout=3) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")
                return cursor.fetchone() == (1,)
    except psycopg.OperationalError:
        return False