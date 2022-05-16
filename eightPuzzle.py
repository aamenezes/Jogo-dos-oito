import os
import random

class Screen:
    def __init__(self, screen, action):
        self.screen = screen
        self.action = action #Move up, down, right, left
        self.digits = []
        self.generateRandomPuzzle()

    def generateRandomPuzzle(self):
        del self.digits[:]
        while len(self.digits) != 9:
            num = random.randint(1,9)
            if num not in self.digits:
                self.digits.append(num)
        print (self.digits)
        return self.digits

class Node:
    def __init__(self, state, previous_node, step_cost, path_cost, heuristic_cost):
        self.state = state
        self.previous_node = previous_node 
        self.step_cost = step_cost #cost to take the step
        self.path_cost = path_cost #cost to reach the current node
        self.heuristic_cost = heuristic_cost #cost to reach the goal state

if __name__ == '__main__':
    screen = Screen(1,1)