from decorators import wal
from edge import Edge
from node import MasterNode
from serializers import NodeSerializer

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

    @wal('CREATE')
    def create(self, sentence):
        qs = sentence.split(":")
        to_node = self.__master_node.create(qs[1])
        from_node = self.__master_node.create(qs[0])
        Edge.create(name=Edge.KEY, to_node=to_node, from_node=from_node)
        Edge.create(name=Edge.VALUE, to_node=from_node, from_node=to_node)
        return True

    def get(self, name):
        node = Edge.get(name)
        if node:
            return NodeSerializer(node).data()
        return 'We found anything'

    def get_all_nodes(self):
        return NodeSerializer(MasterNode.all(), many=True).data()

    @wal('DELETE')
    def delete(self, sentence):
        qs = sentence.split(":")
        return Edge.delete(qs[0], qs[1])

    @wal('UPDATE')
    def update(self, sentence):
        qs = sentence.split(':')
        return Edge.update(qs[0], qs[1])
