import sys
import operator

def get_file_content():
    # Read command args to get filename to read
    filename = sys.argv[1]

    f = open(filename, "r")
    text = f.read()
    f.close()

    return text

# ---------------- Count symbols occurences -----------------

def count_and_sort_occurences(text):
    occurences = dict()
    for symbol in text:
        if symbol in occurences.keys():
            occurences[symbol] += 1
        else:
            occurences[symbol] = 1

    return sorted(occurences.items(), key=operator.itemgetter(1))

# ---------------- Huffman tree node class -----------------
class Node:
    def __init__(self, weight, left, right):
        self.weight = weight
        self.left = left
        self.right = right
    def __str__(self):
        return "w:" + str(self.weight) + " - 0:\n<< " + str(self.left) + " >>\n- 1:\n<<" + str(self.right) + " >>"

# ---------------- Combine two elements into a node -----------------
def create_node(left_child, right_child):
    if type(left_child) != tuple and type(right_child) != tuple:
        return Node(left_child.weight + right_child.weight, left_child, right_child)
    elif type(left_child) == tuple and type(right_child) == tuple:
        return Node(left_child[1] + right_child[1], left_child, right_child)
    elif type(left_child) == tuple and type(right_child) != tuple:
        return Node(left_child[1] + right_child.weight, left_child, right_child)
    else:
        return Node(left_child.weight + right_child[1], left_child, right_child)

# ---------------- Insert node in list depending on its weight -----------------
 
def insert_node(node, occurences):
    i = 0
    while i < len(occurences):
        if type(occurences[i]) != tuple and node.weight < occurences[i].weight:
            occurences.insert(i, node)
            break
        elif type(occurences[i]) == tuple and node.weight < occurences[i][1]:
            occurences.insert(i, node)
            break
        i += 1
    # In case node hasn't been add to the list, append it.
    occurences.append(node)

# ---------------- Huffman tree builder -----------------
def create_huffman_tree():
    text = get_file_content()
    occurences = count_and_sort_occurences(text)
    node = None

    # As we combine all elements into 1 tree, length will decrease
    while len(occurences) > 1:
        # Pop and combine first two elements into a node
        left_child = occurences.pop(0)
        right_child = occurences.pop(0)

        node = create_node(left_child, right_child)

        # Append node to the occurences list at the right position
        insert_node(node, occurences)
    return node

# ---------------- Main -----------------
if __name__ == "__main__":
    tree = create_huffman_tree()
    print(tree)
