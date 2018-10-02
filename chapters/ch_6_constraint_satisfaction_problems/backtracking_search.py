from chapters.ch_6_constraint_satisfaction_problems.general import austria_graph


def recursive_backtracking(node, eval, has_visted):

    if len(has_visted) == 6:
        return True

    colors = eval(node)

    if colors is None:
        return
    else:
        node['color'] = next(iter(colors)) # cannot set color like this, will fix later

    has_visted.add(node['node'].value)

    for child in node['node'].children:
        if child['node'].value not in has_visted:
            return recursive_backtracking(child, eval, has_visted)

    has_visted.remove(node['node'].value)
    return False


def backtracking_search(csp, eval, has_visted):
    return recursive_backtracking(csp, eval, has_visted)


def unused_colors(node):
    is_unused = {'red', 'blue', 'green'}

    if node['color'] is not None:
        is_unused.remove(node['color'])

    for child in node['node'].children:

        child_color = child['color']

        if child_color is None:
            continue

        if is_unused is None or child_color not in is_unused:
            return False

        is_unused.remove(child_color)

    if is_unused is None:
        return False

    return is_unused


backtracking_search({'node': austria_graph(), 'color': None }, unused_colors, set())
