a = set()
def new_node(value):
    return {
        "value": value,
        "left": None,
        "right": None,
        "height": 0
    }


def height(node):
    if node:
        
        return node["height"]
    else:
        return 0


def rotate_right(node):
    left = node["left"]
    c = left["right"]
    node["left"] = c
    node["height"] = max(height(node["right"]), height(c)) + 1
    left["right"] = node
    left["height"] = max(height(left["left"]), height(node)) + 1
    a.add(node['height'])
    return left


def rotate_left(node):
    right = node["right"]
    c = right["left"]
    node["right"] = c
    node["height"] = max(height(node["left"]), height(c)) + 1
    right["left"] = node
    right["height"] = max(height(right["right"]), height(node)) + 1
    return right
    
def print_tree(node):
    if node is None:
        a.add(height(node))
        return
    a.add(height(node))
    print_tree(node["left"])
    
    a.add(height(node))
    print_tree(node["right"])

def add(node, value):
    if node is None:
        a.add(height(node))
        return new_node(value)
    if node["value"] == value:
        a.add(height(node))
        return node
    elif node["value"] < value:
        a.add(height(node))
        node["right"] = add(node["right"], value)
        node["height"] = max(height(node["left"]), height(node["right"])) + 1
        return node
    else:
        a.add(height(node))
        node["left"] = add(node["left"], value)
        node["height"] = max(height(node["left"]), height(node["right"])) + 1
        return node


if __name__ == "__main__":
    root = None
    c = list(map(int, input().split()))
    for i in c:
        root = add(root, i)
    print_tree(root)
    print(max(a) + 1)




