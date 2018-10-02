from utils.Node import Node


def austria_graph():
    def create_child(node, color = None):
        return {'node': node, 'color': color}

    wa = Node("WA")
    nt = Node("NT")
    sa = Node("SA")
    q = Node('Q')
    nsw = Node('NSW')
    v = Node('V')

    # t is not modeled because it can be any color

    wa.add_children([
        create_child(nt),
        create_child(sa)
    ])

    sa.add_children([
        create_child(wa),
        create_child(nt),
        create_child(q),
        create_child(nsw),
        create_child(v)
    ])

    nt.add_children([
        create_child(wa),
        create_child(sa),
        create_child(q)
    ])

    q.add_children([
        create_child(nt),
        create_child(sa),
        create_child(nsw)
    ])
    nsw.add_children([
        create_child(q),
        create_child(sa),
        create_child(v)
    ])

    return wa