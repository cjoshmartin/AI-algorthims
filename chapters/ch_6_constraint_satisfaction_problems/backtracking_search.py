from chapters.ch_6_constraint_satisfaction_problems.general import austria_graph


def recursive_backtracking(node, eval_, has_visited, output_set):  # Generic algorithm
    curr_node = node['node']
    node_children = curr_node.children
    node_name = curr_node.value

    value = eval_(node)  # passed in function that makes the decision for our backtracking algorithm

    if value is False:
        return

    has_visited.add(node_name)
    output_set.append(tuple((node_name, value)))

    if len(has_visited) == 6:
        return output_set

    for child in node_children:
        if child['node'].value not in has_visited:
            return recursive_backtracking(child, eval_, has_visited, output_set)

    has_visited.remove(node_name)
    return False


def backtracking_search(csp, eval_):
    has_visited = set()
    output_set = []
    return recursive_backtracking(csp, eval_, has_visited, output_set)


def unused_colors(node):  # evaluate function
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

    node['color'] = next(iter(is_unused))

    return node['color']


head_node = austria_graph()  # map
output = backtracking_search(
    head_node,
    unused_colors,
)

print(output)
