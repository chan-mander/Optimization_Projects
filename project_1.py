import scipy as sp
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

def monte_carlo_sim(n, ngs, goal_row, goal_col, repeat):

    list_of_moves = [(1, 0, "Move Right"), (-1, 0, "Move Left"), (0, 1, "Move Down"), (0, -1, "Move Up")]

    state_value = []
    goal_state = (goal_row, goal_col)

    for i in range(n):
        for j in range(n):

            costs = []
            
            for k in range(repeat):
                
                cost = 0
                state = (i, j)

                if(((i*n)+j) not in ngs):

                    while state != goal_state:  
                        move = random.choice(list_of_moves)
                        maybe_state = (state[0] + move[0], state[1] + move[1])

                        if(maybe_state[0] < 0 or maybe_state[0] > n-1 or maybe_state[1] < 0 or maybe_state[1] > n-1 or ((maybe_state[0]*n)+maybe_state[1]) in ngs):
                            state = state
                        else:
                            state = maybe_state

                        cost = cost + 1

                costs.append(cost)
        
            state_value.append(np.sum(costs)/repeat)

    return state_value


def get_element(matrix, ngs, row, col):
    if (0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and (((row*len(matrix))+col) not in ngs)):
        return matrix[row][col]
    else:
        raise IndexError("Index out of bounds")


def cal_A(n, ngs, gr, gc):

    A = np.zeros((n*n, n*n))
    list_of_moves = [(1, 0, "Move Right"), (-1, 0, "Move Left"), (0, 1, "Move Down"), (0, -1, "Move Up")]
    board = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if((i, j) != (gr, gc) and (((i*n)+j) not in ngs)):
                A[(i*n)+j][(i*n)+j] = -4
                for move in list_of_moves:
                    try:
                        get_element(board, ngs, i + move[0], j + move[1])
                        A[(i*n)+j][((i + move[0])*n)+(j+ move[1])] =  A[(i*n)+j][((i + move[0])*n)+(j+ move[1])] + 1
                    except IndexError as e:
                        A[(i*n)+j][(i*n)+j] =  A[(i*n)+j][(i*n)+j] + 1
    
    return A


def generate_heat_map(n_1, n_2, ngs, state_values_cal_part1, state_values_mcs_part1, state_values_cal_part2, state_values_mcs_part2):

    fig, ax = plt.subplots(2,2)

    value_set = []
    value_set.append(state_values_cal_part1)
    value_set.append(state_values_mcs_part1)
    value_set.append(state_values_cal_part2)
    value_set.append(state_values_mcs_part2)

    ax[0][0].set_title("Calculated State Values Question 1")
    ax[0][1].set_title("Monte Carlo Simulated State Values Question 1")
    ax[1][0].set_title("Calculated State Values Question 2")
    ax[1][1].set_title("Monte Carlo Simulated State Values Question 2")
    cmap = plt.get_cmap('coolwarm')

    for i in range(2):
        label_counter = n_1 * n_1 - 1

        norm = Normalize(vmin=min(value_set[i]), vmax=max(value_set[i]))

        for y in reversed(range(n_1)):
            for x in reversed(range(n_1)):

                color = cmap(norm(value_set[i][label_counter]))
                rect = plt.Rectangle((x, y), 1, 1, linewidth=1, edgecolor='black', facecolor=color)
                ax[0][i].add_patch(rect)
                label = ax[0][i].text(x + 0.5, y + 0.5, "S_{s}:\n{V}".format(s=label_counter, V=round(value_set[i][label_counter],2)), ha='center', va='center', fontsize=6)
                label_counter -= 1

        ax[0][i].set_xticks([])
        ax[0][i].set_yticks([])
        ax[0][i].set_xlim(0, n_1)
        ax[0][i].set_ylim(n_1,0)
        ax[0][i].grid(linewidth=0)
        ax[0][i].set_aspect('equal')

    for i in range(2):
        label_counter = n_2 * n_2 - 1

        norm = Normalize(vmin=min(value_set[i+2]), vmax=max(value_set[i+2]))

        for y in reversed(range(n_2)):
            for x in reversed(range(n_2)):
                
                if(label_counter not in ngs):
                    color = cmap(norm(value_set[i+2][label_counter]))
                    rect = plt.Rectangle((x, y), 1, 1, linewidth=1, edgecolor='black', facecolor=color)
                    ax[1][i].add_patch(rect)
                    label = ax[1][i].text(x + 0.5, y + 0.5, "S_{s}:\n{V}".format(s=label_counter, V=round(value_set[i+2][label_counter],2)), ha='center', va='center', fontsize=6)
                    label_counter -= 1
                else:
                    color = cmap(norm(value_set[i+2][label_counter]))
                    rect = plt.Rectangle((x, y), 1, 1, linewidth=1, edgecolor='black', facecolor='black')
                    ax[1][i].add_patch(rect)
                    label = ax[1][i].text(x + 0.5, y + 0.5, "Obs", ha='center', va='center', fontsize=6)
                    label_counter -= 1


        ax[1][i].set_xticks([])
        ax[1][i].set_yticks([])
        ax[1][i].set_xlim(0, n_2)
        ax[1][i].set_ylim(n_2,0)
        ax[1][i].grid(linewidth=0)
        ax[1][i].set_aspect('equal')

    plt.show()

def main():
    n_1 = 8
    g_row = 7
    g_column = 7
    no_go_spaces = []

    A = 1/4 * cal_A(n_1, no_go_spaces, g_row, g_column)
    b = -np.ones((n_1*n_1,1))
    b[((g_row*n_1)+g_column)]=0
    c = np.ones((n_1*n_1,1))

    res = sp.optimize.linprog(c, A_ub=A, b_ub=b)

    value_CAL_1 = res.x

    print()
    print("-- Question 1 Calculated State Values --")
    print(np.round(value_CAL_1,2))
    print()
    print("-- Question 1 Calculated Summation of Expected Values --")
    print(np.round(res.fun,2))
    print()
    value_MCS_1 =  monte_carlo_sim(n_1, no_go_spaces, g_row, g_column, 500)
    print("-- Question 1 Monte Carlo Simmulated State Values --")
    print(np.round(value_MCS_1,2))
    print()
    print("-- Question 1 Calculated Summation of Simmulated State Values --")
    print(np.sum(np.round(value_MCS_1,2)))

    n_2 = 5
    g_row = 4
    g_column = 4

    no_go_spaces = [3, 12, 17, 20, 21]

    A = 1/4 * cal_A(n_2, no_go_spaces, g_row, g_column)
    b = -np.ones((n_2*n_2,1))
    c = np.ones((n_2*n_2,1))

    b[((g_row*n_2)+g_column)]=0
    for space in no_go_spaces:
        b[space]=0

    for space in no_go_spaces:
        c[space]=0

    res = sp.optimize.linprog(c, A_ub=A, b_ub=b)

    value_CAL_2 = res.x
    print()
    print("-- Question 2 Calculated State Values --")
    print(np.round(value_CAL_2, 2))
    print()
    print("-- Question 2 Calculated Summation of Expected Values --")
    print(np.round(res.fun, 2))
    print()
    value_MCS_2 =  monte_carlo_sim(n_2, no_go_spaces, g_row, g_column, 500)
    print("-- Question 2 Monte Carlo Simmulated State Values --")
    print(np.round(value_MCS_2,2))
    print()
    print("-- Question 2 Calculated Summation of Simmulated State Values --")
    print(np.sum(np.round(value_MCS_2,2)))


    generate_heat_map(n_1, n_2, no_go_spaces, value_CAL_1, value_MCS_1, value_CAL_2, value_MCS_2)




if __name__ == '__main__':
    main()