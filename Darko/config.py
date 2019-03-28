__all__ = ['Config']


class Config:

    __config = None

    def __init__(self, wal=True, wal_path='./wal.txt', test=False):
        if Config.__config:
            raise BaseException(
                'You have already Config instance. Please use get_config() method for use Darko instance'
            )
        Config.__config = self
        self.wal = wal
        self.wal_path = wal_path
        self.test = test

    @staticmethod
    def get_config():
        return Config.__config
