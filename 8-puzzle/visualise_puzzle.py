import numpy as np
import matplotlib.pyplot as plt
import heuristics

def visualize_puzzle(path, goal):
    """Function to visualize the path of the 8-puzzle solution."""
    # Number of states to visualize
    num_states = len(path)
    
    # Calculate number of rows needed
    num_rows = (num_states + 2) // 3  # Round up to ensure we cover all states
    
    # Create subplots
    fig, axes = plt.subplots(nrows=num_rows, ncols=3, figsize=(9, 3 * num_rows))
    
    # Flatten axes for easy iteration
    axes = axes.flatten()
    
    for i, (ax, state) in enumerate(zip(axes, path)):
        state_array = np.array(state).reshape(3, 3)
        cost = heuristics.manhattan_distance(state_array, goal)
        ax.imshow(state_array, cmap='tab20', vmin=0, vmax=9)
        ax.set_title(f"Manhattan Distance: {cost:.2f}")
        ax.set_xticks(np.arange(3))
        ax.set_yticks(np.arange(3))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        for x in range(3):
            for y in range(3):
                ax.text(y, x, state_array[x, y] if state_array[x, y] != 0 else '',
                        ha='center', va='center', color='white', fontsize=20)
        ax.grid(color='black')
    
    # Hide unused subplots
    for j in range(i + 1, len(axes)):
        axes[j].axis('off')
    
    plt.tight_layout()
    plt.show()