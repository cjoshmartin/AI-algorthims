import sys

from depth_limited_search import depth_limited_search

from utils.Tree import letterTree


def iterative_deepening_search(tree, goal):

    for depth in range(sys.maxsize):
        result =  depth_limited_search(tree, goal, depth)
        if result is not 'cutoff':
            return result


tree = letterTree()
print('{}'.format(iterative_deepening_search(tree, 'Q')))