from utils.Node import infinity, tree_for_adv_search


def mini_max(tree):
    out = max_value(tree)
    return out


def min_value(node):
    if node.is_leaf():
        return node.value

    v = infinity

    for child in node.children:
        v = min(v, max_value(child))

    node.value = v

    return v


def max_value(node):
    if node.is_leaf():
        return node.value

    v = -infinity

    for child in node.children:
        v = max(v, min_value(child))

    node.value = v

    return v

tree = tree_for_adv_search()
output = mini_max(tree)

print(output)