from utils.Node import infinity
from utils.Tree import tree_for_adv_search


def alpha_beta_pruning(tree):
    v = max_value(tree, -infinity, infinity)

    return v


def max_value(node, alpha, beta):
    if node.is_leaf():
        return node.value

    v = - infinity

    for child in node.children:
        v = max(v, min_value(child, alpha, beta))

        if v >= beta:
            return v
        alpha = max(alpha, v)


    node.value = v
    return v


def min_value(node, alpha, beta):
    if node.is_leaf():
        return node.value

    v = infinity

    for child in node.children:
        v = min(v, max_value(child, alpha, beta))

        if v <= alpha:
            return v

        beta = min(beta, v)

    node.value = v

    return v


tree = tree_for_adv_search()
output = alpha_beta_pruning(tree)

print('the output of this alpha beta pruning is {}'.format(output))
