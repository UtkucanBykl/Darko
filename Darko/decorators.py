from config import Config

__all__ = ['wal']
config = Config()
CREATE = 'CREATE'
DELETE = 'DELETE'


def wal(crud_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if config.wal and not config.test and result:
                with open(f'{config.wal_path}', "a") as f:
                    if crud_type == CREATE:
                        f.write(f'{kwargs.get("sentence")}\n')
                    elif crud_type == DELETE:
                        f.write(f'-del- {kwargs.get("sentence")}\n')
            return result

        return wrapper

    return decorator
