from typing import *


class Node:
    def __init__(self, data: int = 0, left=None, right=None) -> None:
        self.data: int = data
        self.left: Node = left
        self.right: Node = right


class BinaryTree:
    def __init__(self):
        self.idx = -1

    def preOrderInsert(self, lists: [List]) -> Optional[Node]:
        self.idx += 1
        if None == lists[self.idx]:
            return None
        newNode: Node = Node(lists[self.idx])
        newNode.left = self.preOrderInsert(lists)
        newNode.right = self.preOrderInsert(lists)
        return newNode

    def preOrderPrint(self, root: Optional[Node]) -> None:
        if not root:
            return
        print(root.data, end=" -> ")
        self.preOrderPrint(root.left)
        self.preOrderPrint(root.right)

    @staticmethod
    def print():
        nodes: [List] = [1, 2, 4, None, None, 5, None, None, 3, None, 6, None, None]
        tree: BinaryTree = BinaryTree()

        root: Node = tree.preOrderInsert(nodes)
        tree.preOrderPrint(root)

