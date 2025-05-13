import random

from graph_utils import *

def graphEquals(g1, g2):
    return all(g1.get(v, set()) == g2.get(v, set()) for v in g1) and len(g1) == len(g2)


if __name__ == "__main__":
    s = [3, 3, 2, 2, 2, 1, 1]
    if canGraphBeCreated(s):
        g = createGraphFromSequence(s)
        print("Graph:")
        printGraph(g)

        count = 0
        for _ in range(100):
            g2 = randomizeNotDirectedGraphWithoutChangingDegrees(g)
            if not graphEquals(g, g2):
                count += 1
        print(f"Number of different graphs after randomization: {count}")
