__all__ = ['Node', 'MasterNode']


class MasterNode:

    __instance = None

    def __init__(self):
        if MasterNode.__instance:
            raise BaseException("You need just one MasterNode")
        MasterNode.__instance = self

    @staticmethod
    def get_master_node():
        return MasterNode.__instance

    def create(self, name):
        return self.__node_control(name)

    def __node_control(self, name):
        """
        Every node have to be unique. So this function control exists
        :param name: Node Name
        :return: If this name
        """
        if name in [n.name for n in MasterNode.all()]:
            return MasterNode.get(name)
        node = Node(name)
        return node

    @staticmethod
    def all():
        """
        Return All Nodes
        """
        for node in Node.nodes:
            yield node

    @staticmethod
    def key_nodes():
        """
        Return just node is a key
        """
        for node in Node.nodes:
            if node.is_key:
                yield node

    @staticmethod
    def get(name):
        """
        Return node which have a this name
        @WIP
        """
        for node in Node.nodes:
            if node.name == name:
                return node

    @staticmethod
    def get_keys(name):
        node = MasterNode.get(name)
        for value in node.keys:
            yield value

    @staticmethod
    def delete(name):
        node = MasterNode.get(name)
        if not node.is_key and not node.keys:
            Node.nodes.remove(node)
            return True
        return False

    @staticmethod
    def get_or_create(name):
        if MasterNode.get(name):
            return MasterNode.get(name)
        master_node = MasterNode.get_master_node()
        return master_node.create(name)


class Node:
    nodes = []

    def __init__(self, name):
        self._name = name
        self.is_key = False
        self.__keys = []
        Node.nodes.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not self.is_key:
            raise BaseException('This node is a key. You can not change name')
        if self._name:
            print('Node Name Change')
        self._name = value

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def values(self, node):
        if isinstance(node, Node):
            self.keys.append(node)
        else:
            raise ('Parameter should be node instance')


if __name__ == "__main__":
    print("direct method")
