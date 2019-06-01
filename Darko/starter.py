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
                        data = line[6:-1] if '\n' in line else line[6:]
                        if line[0:5] == '-del-':
                            darko.delete(data)
                        elif line[0:5] == '-upt-':
                            darko.update(data)
                        else:
                            data = line[:-1] if '\n' in line else line
                            darko.create(data)
                        print(data)
                config.wal = True
            except:
                print('Wal file not found')
