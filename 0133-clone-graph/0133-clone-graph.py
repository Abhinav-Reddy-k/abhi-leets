"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = set()
        mapping = {}

        def dfs(node):
            if node.val in visited:
                return mapping[node]
            visited.add(node.val)
            copyNode = Node(node.val)
            mapping[node] = copyNode
            for nei in node.neighbors:
                copyNode.neighbors.append(dfs(nei))
            return copyNode
        
        return dfs(node) if node else None

                
                


        