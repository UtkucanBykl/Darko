from node import MasterNode, Node

__all__ = ['Edge']


class Edge:

    edges = {'key': []}
    KEY = 'key'
    VALUE = 'value'

    @staticmethod
    def create(name, from_node, to_node):
        if not isinstance(to_node, Node) or not isinstance(from_node, Node):
            raise BaseException(
                'to_node and from_node is have to Node instance')
        if from_node.is_key and name == Edge.KEY:
            raise BaseException('This Node assinged key before')
        if name == Edge.KEY:
            edge = Edge.edges.get(name)
            edge.append({'to': to_node.name, 'from': from_node.name})
            from_node.is_key = True
        elif name == Edge.VALUE:
            from_node.keys = to_node
        return True

    @staticmethod
    def get(from_node_name):
        if Edge.edges.get(Edge.KEY, None):
            edge = Edge.edges.get(Edge.KEY)
            for e in edge:
                if from_node_name == e['from']:
                    return MasterNode.get(e['to'])
        return False

    @staticmethod
    def delete(from_node_name, to_node_name):
        if Edge.edges.get(Edge.KEY, None):
            edge = Edge.edges.get(Edge.KEY)
            for e in edge:
                if from_node_name == e['from'] and to_node_name == e['to']:
                    edge.remove(e)
                    from_node = MasterNode.get(from_node_name)
                    to_node = MasterNode.get(to_node_name)
                    if from_node in to_node.keys:
                        to_node.keys.remove(from_node)
                    from_node.is_key = False
                    MasterNode.delete(from_node_name)
                    MasterNode.delete(to_node_name)
                    return True
        return False

    @staticmethod
    def update(from_node_name, to_node_name):
        old_to_node = Edge.get(from_node_name)
        if old_to_node:
            Edge.delete(from_node_name, old_to_node.name)    
            Edge.create(
                Edge.KEY,
                MasterNode.get_or_create(from_node_name),
                MasterNode.get_or_create(to_node_name),
            )
            return True
        return False
