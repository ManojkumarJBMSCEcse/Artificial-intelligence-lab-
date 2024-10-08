from collections import deque

class PuzzleState:
    def _init_(self, state, moves=0, previous=None):
        self.state = state
        self.moves = moves
        self.previous = previous

    def _str_(self):
        return str(self.state[:3]) + "\n" + str(self.state[3:6]) + "\n" + str(self.state[6:]) + "\n"

def get_neighbors(state):
    neighbors = []
    index_blank = state.index(0)
    x, y = divmod(index_blank, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = list(state)
            new_state[index_blank], new_state[new_index] = new_state[new_index], new_state[index_blank]
            neighbors.append(tuple(new_state))

    return neighbors

def bfs(start, goal):
    queue = deque()
    visited = set()
    
    start_state = PuzzleState(start)
    queue.append(start_state)
    visited.add(start)

    while queue:
        current_state = queue.popleft()

        if current_state.state == goal:
            return current_state
        
        for neighbor in get_neighbors(current_state.state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(PuzzleState(neighbor, current_state.moves + 1, current_state))

    return None

def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.previous
    for step in reversed(path):
        print(step)

start_state = (1, 2, 3, 4, 0, 5, 6, 7, 8)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution = bfs(start_state, goal_state)

if solution:
    print("Solution found in", solution.moves, "moves:")
    print_solution(solution)
else:
    print("No solution found.")
