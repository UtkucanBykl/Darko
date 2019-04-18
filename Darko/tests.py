import json
from unittest import TestCase, main, skip

from darko import Darko
from node import MasterNode
from config import Config
from serializers import NodeSerializer
__all__ = ['DarkoTest']
class DarkoTest(TestCase):
    def setUp(self):
        self.darko = Darko.get_darko()
        self.master_node = MasterNode.get_master_node()
        self.config = Config.get_config()
        self.config.test = True

    def test_get(self):
        self.darko.create('utkuu:1')
        data = json.loads(self.darko.get('utkuu'))
        self.assertEqual(data[0]['name'], '1')

    def test_get_false(self):
        self.assertEqual('We found anything', self.darko.get('1'))

    @skip
    def test_get_all_nodes(self):
        data = json.loads(self.darko.get_all_nodes())
        self.assertEqual(len(data), 2)

    def test_delete(self):
        self.darko.create('ahmet:2')
        self.assertTrue(self.darko.delete('ahmet:2'))

    def test_delete_false(self):
        self.assertFalse(self.darko.delete('dede:baba'))


if __name__ == '__main__':
    main()
