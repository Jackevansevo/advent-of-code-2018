from typing import List, Set, Deque
from dataclasses import dataclass, field
from graphviz import Digraph
from operator import attrgetter


@dataclass
class Node:
    name: str
    children: List["Node"] = field(default_factory=list)

    def __hash__(self):
        return hash(self.name)

    def __iter__(self):
        yield self
        for child in sorted(self.children, key=attrgetter("name")):
            yield from child


def draw_graph(root):
    dot = Digraph(comment="Graph")
    dot = build_graph(dot, root)
    dot.render("graph/ast.gv", view=True)


def traverse(node):
    def find_next_step(node, available, visited):
        visited.append(node)
        if node.children is not None:
            available.extend(node.children)
            available = Deque(sorted(list(available), key=attrgetter("name")))
        if len(available) > 0:
            next_node = available.popleft()
            return next_node, available, visited

    next_node = node
    available = Deque(sorted(node.children, key=attrgetter("name")))
    visited = [next_node]
    while True:
        result = find_next_step(next_node, available, visited)
        if result is not None:
            next_node, available, visited = result
            print(next_node)
        if next_node is None:
            return


def build_graph(dot, nodes):
    try:
        node, *rest = nodes
        for child in node.children:
            dot.edge(node.name, child.name)
    except ValueError:
        return dot
    return build_graph(dot, rest)


if __name__ == "__main__":
    root = None
    # Keeps track of created nodes
    pool = dict()
    with open("input/day7.txt") as f:
        for line in f:
            instruction = line.strip()
            step, dependency = line[5], line[36]
            if root is None:
                root, before = Node(step), Node(dependency)
                root.children.append(before)
                pool[step] = root
                pool[dependency] = before
            else:
                child = pool.get(step)
                if child is not None:
                    before = Node(dependency)
                    child.children.append(before)
                    pool[dependency] = before
    # draw_graph(root)
    traverse(root)
