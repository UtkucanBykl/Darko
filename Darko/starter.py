from config import Config
from darko import Darko
__all__ = ['Start']


class Start:

    @staticmethod
    def start():
        darko = Darko.get_darko()
        config = Config.get_config()
        if config.wal:
            config.wal = False
            with open(f'{config.wal_path}/wal.txt', 'r') as f:
                for line in f.readlines():
                    darko.create(line.replace('\n', ''))
            config.wal = True