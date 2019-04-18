import json

from node import Node

__all__ = ['NodeSerializer']


class NodeSerializer():

    def __init__(self, node, fields='__all__', many=True):
        self.__node = node
        self.__fields = fields
        self.__many = many

    def __get_node(self):
        node_list = list()
        if isinstance(self.__node, Node):
            node_list.append(self.__node)
        else:
            node_list = self.__node
        return node_list

    def serialize(self):
        serialize_data = list()
        node_list = self.__get_node()
        if self.__many:
            for node in node_list:
                data = dict(
                    name=node.name,
                    is_key=node.is_key,
                )
                serialize_data.append(data)
        return serialize_data

    def data(self):
        data = self.serialize()
        return json.dumps(data)
