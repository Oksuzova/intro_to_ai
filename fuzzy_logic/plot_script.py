import matplotlib.pyplot as plt


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