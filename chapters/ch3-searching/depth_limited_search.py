from utils.Tree import letterTree


def depth_limited_search_r(problem, goal, limit):
    if problem.value == goal:
        return True

    elif problem.depth == limit:
        return 'cutoff'
    elif problem.children is not None:
        cutoff_occurred = False
        for child in problem.children:
            result = depth_limited_search_r(child, goal, limit)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result is not None:
                return result

        return 'cutoff' if cutoff_occurred else None


def depth_limited_search(head, goal, limit):
    return depth_limited_search_r(head, goal, limit)


tree = letterTree()

print('{}'.format(depth_limited_search(tree, '4', 4)))
