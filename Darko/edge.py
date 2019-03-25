from node import MasterNode, Node

__all__ = ['Edge']


class Edge:

    edges = {'key': [], 'value': []}
    KEY = 'key'
    VALUE = 'value'

    @staticmethod
    def create(name, to_node, from_node):
        if not isinstance(to_node, Node) or not isinstance(from_node, Node):
            raise BaseException('to_node and from_node is have to Node instance')
        if from_node.is_key and name == Edge.KEY:
            raise BaseException('This Node assinged key before')
        edge = Edge.edges.get(name)
        edge.append({'to': to_node.name, 'from': from_node.name})
        if name == Edge.KEY:
            from_node.is_key = True
        elif name == Edge.VALUE:
            from_node.values = to_node
        return True

    @staticmethod
    def get(value):
        if Edge.edges.get(Edge.KEY, None):
            edge = Edge.edges.get(Edge.KEY)
            for e in edge:
                if value == e['from']:
                    return MasterNode.get(e['to'])
        return False

    @staticmethod
    def delete(from_node, to_node):
        if Edge.edges.get(Edge.KEY, None):
            edge = Edge.edges.get(Edge.KEY)
            for e in edge:
                if from_node == e['from'] and to_node == e['to']:
                    edge.remove(e)
                    return True
        return False


if __name__ == "__main__":
    print("direct method")
