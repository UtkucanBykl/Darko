import json

__all__ = ['NodeSerializer']


class NodeSerializer():

    def __init__(self, node, fields='__all__', many=True):
        self.__node = node
        self.__fields = fields
        self.__many = many

    def serialize(self):
        serialize_data = list()
        if self.__many:
            for node in self.__node:
                data = dict(
                    name=node.name,
                    is_key=node.is_key,
                )
                serialize_data.append(data)
        return serialize_data

    def data(self):
        data = self.serialize()
        print(data)
        return json.dumps(data)
