import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def plot_graphs(x, graphs, xlabel='x', ylabel='y'):
    # plt.figure(figsize=(10, 6))

    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)

    for graph in graphs:
        y = graph['y']
        label = graph["label"]
        color = graph["color"]
        linestyle = graph["linestyle"]

        plt.plot(x, y, label=label, color=color, linestyle=linestyle)
        plt.legend()
        plt.grid(True)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def subplot_graphs(x, graphs, xlabel='x', ylabel='y'):
    plt.figure(figsize=(10, 6))

    fig, axs = plt.subplots(len(graphs))

    for i, function in enumerate(graphs):
        y = function['y']
        label = function["label"]
        color = function["color"]
        linestyle = function["linestyle"]

        axs[i].plot(x, y, label=label, color=color, linestyle=linestyle)
        axs[i].set_title(label)
        axs[i].set(xlabel=xlabel, ylabel=ylabel)


def add_vertical_line(x_vert, color='Red', linestyle='--', label='x'):
    plt.axvline(x=x_vert, color=color, linestyle=linestyle, label=f'{label}={x_vert}')
    plt.legend()


def create_graph(x, function, label, xlabel, ylabel, color="SeaGreen", linestyle=None):
    plt.plot(x, function, label=label, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.show()


# Set colors for clusters
RED = '#96242c'
YELLOW = '#bfb02a'
GREEN = '#218f4b'
COLORS = [RED, YELLOW, GREEN]


# Map colors to clusters based on their centers
def get_cluster_colors(cluster_centers: np.ndarray, colors: list) -> list:
    sorted_indices = np.argsort(cluster_centers[:, 0])  # Sort by the first coordinate
    return [colors[i] for i in sorted_indices]


# Plot points with their corresponding clusters
def plot_points(data: np.ndarray, U: np.ndarray, cluster_colors: list, grades: np.ndarray = None, alpha: float = 0.7,
                s: int = 200):
    for i in range(data.shape[0]):
        cluster_index = np.argmax(U[i, :])  # Get the index of the cluster
        cluster_color = cluster_colors[cluster_index]  # Determine the cluster color

        plt.scatter(data[i, 0], data[i, 1], color=cluster_color, alpha=alpha, edgecolors='k', s=s)

        # Highlight student grades
        if grades is not None:
            if grades[i] == 0:  # Low
                plt.scatter(data[i, 0], data[i, 1], color=RED, alpha=0.9, s=60, edgecolors='k', label='_nolegend_')
            elif grades[i] == 1:  # Medium
                plt.scatter(data[i, 0], data[i, 1], color=YELLOW, alpha=0.9, s=60, edgecolors='k', label='_nolegend_')
            elif grades[i] == 2:  # High
                plt.scatter(data[i, 0], data[i, 1], color=GREEN, alpha=0.9, s=60, edgecolors='k', label='_nolegend_')


# Plot clustering results
def plot_results(data: np.ndarray, cluster_centers: np.ndarray, U: np.ndarray):
    plt.figure(figsize=(10, 6))
    cluster_colors = get_cluster_colors(cluster_centers, COLORS)  # Get fixed colors for clusters
    plot_points(data, U, cluster_colors)

    # Display cluster centers
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], color='black', marker='X', s=200, label='Cluster Centers')

    plt.title('Fuzzy C-Means Clustering')
    plt.xlabel('Number of raised hands in class')
    plt.ylabel('Number of visited resources')
    plt.legend()
    plt.grid()
    plt.show()


# Plot clustering results with student grades
def plot_with_grades(data: np.ndarray, cluster_centers: np.ndarray, U: np.ndarray, grades: np.ndarray):
    plt.figure(figsize=(12, 8))
    cluster_colors = get_cluster_colors(cluster_centers, COLORS)  # Get fixed colors for clusters
    plot_points(data, U, cluster_colors, grades)

    # Display cluster centers
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], color='black', marker='X', s=300, label='Cluster Centers')

    plt.title('Fuzzy C-Means Clustering with Student Grades')
    plt.xlabel('Number of raised hands in class')
    plt.ylabel('Number of visited resources')

    plt.xlim(min(data[:, 0]) - 5, max(data[:, 0]) + 5)  # Extend range on X-axis
    plt.ylim(min(data[:, 1]) - 5, max(data[:, 1]) + 5)  # Extend range on Y-axis

    # Create a custom legend
    custom_legend = [
        Line2D([0], [0], marker='o', color='w', label='Low', markerfacecolor=RED, markersize=10),
        Line2D([0], [0], marker='o', color='w', label='Medium', markerfacecolor=YELLOW, markersize=10),
        Line2D([0], [0], marker='o', color='w', label='High', markerfacecolor=GREEN, markersize=10)
    ]
    plt.legend(handles=custom_legend, title='Grades', loc='upper left')
    plt.grid()
    plt.show()


# Plot the changes in the objective function over iterations
def plot_objective_function(objective_values: list):
    plt.figure(figsize=(10, 6))
    plt.plot(objective_values, marker='o', color='b')
    plt.title('Objective Function Convergence')
    plt.xlabel('Iteration')
    plt.ylabel('Objective Function Value')
    plt.grid()
    plt.show()
