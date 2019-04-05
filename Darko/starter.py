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
            try:
                with open(f'{config.wal_path}', 'r') as f:
                    for line in f.readlines():
                        line.replace('\n', '')
                        if line[0:5] == '-del-':
                            darko.delete(line[6:])
                        else:
                            darko.create(line)
                config.wal = True
            except:
                print('Wal file not found')
