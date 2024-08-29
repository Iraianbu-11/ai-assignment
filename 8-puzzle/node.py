import copy
import heuristics

class Node:
    def __init__(self, parent, mat, empty_tile_pos, cost, level):
        self.parent = parent
        self.mat = mat
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level
        
    def __lt__(self, other):
        return self.cost < other.cost

    @staticmethod
    def reconstruct_path(node):
        path = []
        while node:
            path.append(node.mat)
            node = node.parent
        return path[::-1]

    @staticmethod
    def new_node(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final):
        new_mat = copy.deepcopy(mat)
        x1, y1 = empty_tile_pos
        x2, y2 = new_empty_tile_pos
        new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
        cost = heuristics.manhattan_distance(new_mat, final)
        return Node(parent, new_mat, new_empty_tile_pos, cost, level)