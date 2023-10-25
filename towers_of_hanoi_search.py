import copy


def get_future_states_peg(state, peg_index):
    """Try to take topmost disc from peg at peg_index and put it on other pegs"""
    future_states_peg = []
    current_peg = state[peg_index]
    if current_peg == []:
        return []
    topmost_disc = current_peg[-1]
    for other_peg_index in range(len(state)):
        if other_peg_index == peg_index:
            continue
        other_peg = state[other_peg_index]
        if other_peg == [] or topmost_disc < other_peg[-1]:
            print(peg_index, '->', other_peg_index)
            future_state = copy.deepcopy(state)
            future_state[peg_index].pop()
            future_state[other_peg_index].append(topmost_disc)
            future_states_peg.append(future_state)
    return future_states_peg


def get_future_states(state):
    """
    state is a tower of hanoi state expressed as [[...], [...], [...], ...].
    Each subarray is a peg. Each number in the subarray is disk size (unique).
    Valid tower of hanoi state: In each subarray, large numbers first. First means on the bottom.
    """

    future_states = []
    for peg_index in range(len(state)):
        future_states_peg = get_future_states_peg(state, peg_index)
        future_states.extend(future_states_peg)
    return future_states


def hanoi_move_count():
    initial_state = [[3, 2, 1], [], []]
    queue = [initial_state]
    visited = []
    while queue != []:
        current_state = queue.pop(0)
        visited.append(current_state)
        print(current_state)
        if current_state == [[], [], [3, 2, 1]]:
            return
        future_states = get_future_states(current_state)
        for future_state in future_states:
            if future_state not in visited:
                queue.append(future_state)


hanoi_move_count()