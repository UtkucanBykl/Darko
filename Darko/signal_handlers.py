import signal
import sys
from config import Config

__all__ = ['SignalHandler']


class SignalHandler:
    def __init__(self):
        self.config = Config.get_config()

    def signal_handler(self, sig, frame):
        with open(f'{self.config.wal_path}', 'w') as f:
            f.write('')
        sys.exit(0)

    def save(self):
        signal.signal(signal.SIGINT, self.signal_handler)
