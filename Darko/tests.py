from unittest import TestCase, main
from darko import Darko
from edge import Edge
from node import Node, MasterNode
from config import Config
from serializers import NodeSerializer
import json


class DarkoTest(TestCase):

    def setUp(self):
        self.darko = Darko.get_darko()
        self.master_node = MasterNode.get_master_node()
        self.config = Config.get_config()
        self.config.test = True

    def test_get(self):
        self.darko.create('utku:1')
        self.assertEqual(self.darko.get('utku').name, '1')

    def test_get_false(self):
        self.assertFalse(self.darko.get('1'))

    def test_get_all_Nodes(self):
        data = json.loads(self.darko.get_all_nodes())
        self.assertEqual(len(data), 2)


if __name__ == '__main__':
    main()
