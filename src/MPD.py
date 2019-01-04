

class MPD:

    def __init__(self):
        self.actions_space = []
        self.states_space = []
        self.gamma = 0.9
        self.V_fun_tab = []

    def reward(self, state, action, n_state):
        pass

    def T_fun(self, state, action, n_state):
        # returns P(n_state | action, state)
        pass

    def V_fun(self, state):
        return max([self.Q_fun(state, action) for action in self.actions_space])

    def policy(self, state):
        values = [self.Q_fun(state, action) for action in self.actions_space]
        max_index = values.index(max(values))
        return self.actions_space[max_index]

    def Q_fun(self, state, action):
        result = 0
        for n_state in self.states_space:
            result += self.T_fun(state, action, n_state) * (self.reward(state, action, n_state) + self.gamma * \
                      self.V_fun_tab[n_state])
            """
            if state == (0,2) and n_state == (0, 3):
                if (n_state == (0, 3)):
                    print(self.T_fun(state, action, n_state) * (self.reward(state, action, n_state) + self.gamma * \
                                                                self.V_fun_tab[n_state]))
                    print(self.reward(state, action, n_state) , self.gamma , self.V_fun_tab[n_state])
                print (action, result, self.T_fun(state, action, n_state), self.V_fun_tab[n_state], n_state)
            """
        return result

    def update(self):
        for state in self.states_space[:-1]:
            values = [self.Q_fun(state, action) for action in self.actions_space]
            self.V_fun_tab[state] = max(values)

    def print(self):
        pass


