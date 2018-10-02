def recursive_backtracking(goal, node, eval):
    has_visted = set()

    if goal == node.value:
        return True

    colors  = eval(node)

    has_visted.add(node.value)

    for child in node.children:

        print(child.value)


    return False

def backtracking_search(goal, csp, eval):
    return recursive_backtracking(goal, csp)


def unused_colors(node):
    is_not_used_color = {
        'red': True,
        'blue': True,
        'green': True
    }

    for child in node.children:

        child_color = child['color']

        if child_color not None:
            is_not_used_color[child_color] = False

    if all(color == False for color in is_not_used_color.values()):
        return False

    return is_not_used_color