import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def manhattan_distance(state, goal_state):
    """Calculate the Manhattan Distance heuristic."""
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i, j]
            if value != 0:
                goal_pos = np.argwhere(goal_state == value)[0]
                distance += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return distance

def euclidean_distance(state, goal_state):
    """Calculate the Euclidean Distance heuristic."""
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i, j]
            if value != 0:
                goal_pos = np.argwhere(goal_state == value)[0]
                distance += np.sqrt((i - goal_pos[0]) ** 2 + (j - goal_pos[1]) ** 2)
    return distance

def chebyshev_distance(state, goal_state):
    """Calculate the Chebyshev Distance heuristic."""
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i, j]
            if value != 0:
                goal_pos = np.argwhere(goal_state == value)[0]
                distance = max(distance, abs(i - goal_pos[0]), abs(j - goal_pos[1]))
    return distance

def hamming_distance(state, goal_state):
    """Calculate the Hamming Distance heuristic."""
    return np.sum(state != goal_state) - 1  # Subtract 1 because zero is ignored

def visualize_heuristics(state, goal_state):
    """Visualize the state with various heuristics."""
    fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(15, 5))
    heuristics = [manhattan_distance, euclidean_distance, chebyshev_distance, hamming_distance]
    labels = ['Manhattan Distance', 'Euclidean Distance', 'Chebyshev Distance', 'Hamming Distance']
    
    for ax, heuristic, label in zip(axes, heuristics, labels):
        value = heuristic(state, goal_state)
        ax.imshow(state, cmap='tab20', vmin=0, vmax=9)
        ax.set_title(f"{label}: {value:.2f}")
        ax.set_xticks(np.arange(3))
        ax.set_yticks(np.arange(3))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        for i in range(3):
            for j in range(3):
                ax.text(j, i, state[i, j] if state[i, j] != 0 else '',
                        ha='center', va='center', color='white', fontsize=20)
        ax.grid(color='black')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Initial configuration and goal configuration
    initial_state = np.array([[1, 4, 3], [2, 5, 6], [8, 7, 0]])
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    
    # Visualize the state with various heuristics
    visualize_heuristics(initial_state, goal_state)