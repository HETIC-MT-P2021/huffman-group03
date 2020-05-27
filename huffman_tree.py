import sys
import operator

# Read command args to get filename to read
filename = sys.argv[1]

f = open(filename, "r")
text = f.read()
f.close()

# ---------------- Count symbols occurences -----------------

occurences = dict()
for symbol in text:
    if symbol in occurences.keys():
        occurences[symbol] += 1
    else:
        occurences[symbol] = 1

sorted_occurences = sorted(occurences.items(), key=operator.itemgetter(1))

# ---------------- Create Huffman tree -----------------
class Node:
    def __init__(self, weight, left, right):
        self.weight = weight
        self.left = left
        self.right = right
    def __str__(self):
        return "w:" + str(self.weight) + " - 0:\n\t<< " + str(self.left) + " >>\n- 1:\n\t<<" + str(self.right) + " >>"


node = None
while len(sorted_occurences) > 1:

    # Pop and combine first two elements into a node
    next_sorted_l = sorted_occurences.pop(0)
    next_sorted_r = sorted_occurences.pop(0)

    if type(next_sorted_l) != tuple and type(next_sorted_r) != tuple:
        node = Node(next_sorted_l.weight + next_sorted_r.weight, next_sorted_l, next_sorted_r)
    elif type(next_sorted_l) == tuple and type(next_sorted_r) == tuple:
        node = Node(next_sorted_l[1] + next_sorted_r[1], next_sorted_l, next_sorted_r)
    elif type(next_sorted_l) == tuple and type(next_sorted_r) != tuple:
        node = Node(next_sorted_l[1] + next_sorted_r.weight, next_sorted_l, next_sorted_r)
    elif type(next_sorted_l) != tuple and type(next_sorted_r) == tuple:
        node = Node(next_sorted_l.weight + next_sorted_r[1], next_sorted_l, next_sorted_r)


    # Append node to the occurences list at the right position

    i = 0
    while i < len(sorted_occurences):
        if type(sorted_occurences[i]) != tuple and node.weight < sorted_occurences[i].weight:
            sorted_occurences.insert(i, node)
            node = None
            break
        elif type(sorted_occurences[i]) == tuple and node.weight < sorted_occurences[i][1]:
            sorted_occurences.insert(i, node)
            node = None
            break
        i += 1
    # In case node hasn't been add to the list, append it.
    if node != None:
        sorted_occurences.append(node)


print("END: ")
print(node)
