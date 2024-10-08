class Node:
    def _init_(self, state, parent=None):
        self.state = state
        self.parent = parent

def depth_limited_dfs(node, goal, depth):
    if depth == 0 and node.state == goal:
        return node
    elif depth > 0:
        for child in get_children(node):
            result = depth_limited_dfs(child, goal, depth - 1)
            if result is not None:
                return result
    return None

def iterative_deepening_dfs(start, goal):
    depth = 0
    while True:
        result = depth_limited_dfs(start, goal, depth)
        if result is not None:
            return result
        depth += 1

def get_children(node):
    # Example of generating children for a simple binary tree
    return [Node(node.state * 2, node), Node(node.state * 2 + 1, node)]

def print_solution(solution):
    path = []
    while solution is not None:
        path.append(solution.state)
        solution = solution.parent
    print(" -> ".join(map(str, path[::-1])))

if _name_ == "_main_":
    start_node = Node(1)  # Starting state
    goal_state = 10       # Goal state

    solution = iterative_deepening_dfs(start_node, goal_state)

    if solution:
        print("Goal found!")
        print_solution(solution)
    else:
        print("Goal not found.")
