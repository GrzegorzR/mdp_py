import random
import numpy as np
from copy import deepcopy

from src.MPD import MPD


class LabMPD(MPD):

    def __init__(self, level, step_penelty=-0.1):
        self.level = level
        self.actions_space = [(-1, 0), (0, 1), (1, 0), (0,-1)]
        self.states_space = self.create_state_space(level)
        self.gamma = 0.9
        self.V_fun_tab = {j: 0 for j in self.states_space}
        self.step_penelty = step_penelty

    def create_state_space(self, level):
        result = []
        x = len(level)
        for i in range(x):
            for j in range(x):
                if lvl[i][j] != 'x':
                    result.append((i, j))

        result.append("exit")
        return result

    def T_fun(self, state, action, n_state):
        val = self.level[state[0]][state[1]]

        if n_state == "exit":
            if val != 0:
                return 1
            else:
                return 0

        if not self.next_to(state, n_state):
            return 0

        if state == n_state:
            if self.step_into_wall(state, action):
                return 0.8

        if self.step_into(state, n_state, action):
            return 0.8

        # any other case is field on the right or left of the action direction
        return 0.1

    def next_to(self, state, n_state):
        if state[0] == n_state[0] and state[1] == n_state[1] + 1:
            return True
        if state[0] == n_state[0] and state[1] == n_state[1] - 1:
            return True
        if state[1] == n_state[1] and state[0] == n_state[0] + 1:
            return True
        if state[1] == n_state[1] and state[0] == n_state[0] - 1:
            return True
        return False

    def step_into_wall(self, state, action):
        i, j = state[0] + action[0], state[1] + action[1]

        if i < 0 or j < 0 or i > len(self.level) or i > len(self.level):
            return True
        else:
            return False

    def step_into(self, state, n_state, action):
        i, j = state[0] + action[0], state[1] + action[1]

        if i == n_state[0] and j == n_state[1]:
            return True
        else:
            return False

    def reward(self, state, action, n_state):
        val = self.level[state[0]][state[1]]

        if n_state == "exit":
            if val != 0:
                return val
            else:
                return self.step_penelty
        else:
            return self.step_penelty

    def print(self):
        res = deepcopy(self.level)
        actions_dict = {
            (0, 1): '>',
            (0, -1): '<',
            (-1, 0): '^',
            (1, 0): 'v'}
        for i in range(len(self.level)):
            for j in range(len(self.level)):
                if res[i][j] == 0:
                    res[i][j] = actions_dict[self.policy((i,j))]
        print(np.matrix(res))


if __name__ == '__main__':
    x = 6
    lvl = [[0 for _ in range(x)] for _ in range(x)]
    for i in range(x):
        for j in range(x):
            if random.random() < 0.1:
                lvl[i][j] = 'x'
            elif random.random() < 0.2:
                lvl[i][j] = random.randint(-3,3)

    mpd = LabMPD(lvl)
    for _ in range(100):
        mpd.update()
    mpd.print()
    print(mpd.V_fun_tab)