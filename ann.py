import math
import random
import time
from decimal import *


class input_node:
    def __init__(self, weight):
        self.input_value = 0
        self.weight = weight


class output_node:
    def __init__(self):
        self.input_value = 0


def classification_function(output):
    #print('Output: '+str(output.input_value))

    #time.sleep(.2)
    if Decimal(output.input_value) >= Decimal(.9):
        return 1
    else:
        return 0


def change_weight(input_nodes, inputs, dimensionality, obtained):
    #print('Updating weights')
    lr = .01
    for idx, node_w in enumerate(input_nodes):
        if idx == 0:
            error = float(inputs[dimensionality]) - node_w.weight
        else:
            error = (float(inputs[dimensionality]) - (1 if node_w.input_value*node_w.weight > .9 else 0)) * float(inputs[idx-1])

        #print(error)
        #time.sleep(.5)
        node_w.weight += lr * error


def train(dimensionality, test_set):
    input_nodes = []
    for idx in range(dimensionality+1):
        input_nodes.append(input_node((random.random())))
    asserts = 0
    restart = True
    laps = 0
    while restart:
        for x in range(len(test_set)):
            exit_node = output_node()
            for idx, node in enumerate(input_nodes):
                if idx == 0:
                    node.input_value = 1.0
                else:
                    node.input_value = float(test_set[x][idx-1])
                exit_node.input_value += (node.input_value * node.weight)
            class_value = classification_function(exit_node)
            if class_value == int(test_set[x][dimensionality]):
                asserts += 1
            else:
                asserts = 0
                change_weight(input_nodes, test_set[x], dimensionality, exit_node.input_value)
            if asserts >= len(test_set):
                restart = False
        #print("Lap")
        if laps > 1000:
            print("no solution found")
            exit(0)
        laps += 1
    return input_nodes


def print_network(net):
    for idx, node in enumerate(net):
        print('Node '+str(idx)+' Weight: '+str(node.weight))


def evaluate(network, input):
    exit_node = output_node()
    for idx, node in enumerate(network):
        if idx == 0:
            exit_node.input_value += node.weight
        else:
            exit_node.input_value += node.weight * float(input[idx-1])
    print(classification_function(exit_node))

if __name__ == '__main__':

    d = int(input())
    m = int(input())
    n = int(input())
    examples = []
    tests = []
    for idx in range(m):
        line = input()
        line = line.replace('\n', '')
        line = line.replace(' ', '')
        line = line.split(',')
        examples.append(line)
    for idx in range(n):
        line = input()
        line = line.replace('\n', '')
        line = line.replace(' ', '')
        line = line.split(',')
        tests.append(line)

    network = train(d, examples)
    #print_network(network)
    for test in tests:
        evaluate(network, test)

    exit(0)