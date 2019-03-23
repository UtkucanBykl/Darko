from node import MasterNode
from edge import Edge
from serializers import NodeSerializer
from decorators import wal
__all__ = ['Darko']


class Darko:
    """
    This Class is a master. Every database method have to in here.
    Class pattern Singleton because we need only one master instance
    """

    __darko = None

    def __init__(self, db_name='default'):
        if Darko.__darko:
            raise BaseException(
                'You have already Darko instance. Please use get_darko() method for use Darko instance'
            )
        Darko.__darko = self
        self._db_name = db_name
        self.__master_node = MasterNode()

    @staticmethod
    def get_darko():
        if not Darko.__darko:
            Darko()
        return Darko.__darko

    @wal()
    def create(self, sentence):
        qs = sentence.split(":")
        to_node = self.__master_node.create(qs[1])
        from_node = self.__master_node.create(qs[0])
        Edge.create(name=Edge.KEY, to_node=to_node, from_node=from_node)
        Edge.create(name=Edge.VALUE, to_node=from_node, from_node=to_node)
        return True

    def get(self, name):
        return Edge.get(name)

    def get_all_nodes(self):
        return NodeSerializer(MasterNode.all(), many=True).data()
