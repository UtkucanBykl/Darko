from config import Config

__all__ = ['wal']
config = Config()


def wal():
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if config.wal:
                with open(f'{config.wal_path}/wal.txt', 'a') as f:
                    f.write(f'{kwargs.get("sentence")}\n')
            return result
        return wrapper
    return decorator
