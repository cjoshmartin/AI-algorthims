from utils.Node import Node


def austria_graph():
    def create_child(node):
        return {'node': node, 'color': None}

    wa = create_child(Node("WA"))
    nt = create_child(Node("NT"))
    sa = create_child(Node("SA"))
    q = create_child(Node('Q'))
    nsw = create_child(Node('NSW'))
    v = create_child(Node('V'))

    wa['node'].add_children([
        nt,
        sa
    ])

    sa['node'].add_children([
        wa,
        nt,
        q,
        nsw,
        v
    ])

    nt['node'].add_children([
        wa,
        sa,
        q
    ])

    q['node'].add_children([
        nt,
        sa,
        nsw
    ])
    nsw['node'].add_children([
        q,
        sa,
        v
    ])

    v['node'].add_children([
        nsw,
        sa
    ])

    return wa
