import json
from unittest import TestCase, main, skip

from Darko.Darko import Darko, MasterNode, Node, Edge


class DarkoTest(TestCase):
    def setUp(self):
        self.darko = Darko.get_darko()
        self.master_node = MasterNode.get_master_node()
        self.config = Config.get_config()
        self.config.test = True

    def test_get(self):
        self.darko.create('utkuu:1')
        self.assertEqual(self.darko.get('utkuu').name, '1')

    def test_get_false(self):
        self.assertFalse(self.darko.get('1'))

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
