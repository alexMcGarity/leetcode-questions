'''
You are given an array of strings equations that represent relationships between variables where each string equations[i] 
is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".
Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.
'''


class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        # 1. Union-Find
        # Time: O(n)
        # Space: O(1)
        parent = [i for i in range(26)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)
        for eq in equations:
            if eq[1] == '=':
                union(ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a'))
        for eq in equations:
            if eq[1] == '!' and find(ord(eq[0]) - ord('a')) == find(ord(eq[3]) - ord('a')):
                return False
        return True
