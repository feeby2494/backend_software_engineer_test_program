import os

class ActionLog:
    def __init__(self):
        self.action_list = []
        self.fight_number = 1

    def add_action_list(self, line):
        self.action_list.append(line)

    def write_action_log_to_file(self):
        with open(os.path.join(os.getcwd(),"log", "action_log"), "w") as f:
            for line in self.action_list:
                f.write(line + "\n")