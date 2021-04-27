class ShortestPath:
    visited_table = {}
    visited = []
    unvisited = []
    short_paths = []
    next_p = [-1, -1]
    total_cost = 0

    def __init__(self, node, len_of_node, start, end):
        self.node = node
        self.len_of_node = len_of_node
        self.start = start
        self.end = end
        self.short_paths = [end]
        self.__assign_values()

    def __assign_values(self):
        for i in range(1, self.len_of_node + 1):
            if i != self.end:
                self.unvisited.append(i)
            self.visited_table[i] = [-1, -1]
        self.unvisited.append(self.end)

    def __check(self, p1, p2, s):
        if p1 != s and p2 != s:
            return True
        elif p1 in self.visited or p2 in self.visited:
            return True
        else:
            return False

    def __find_path(self):
        while True:
            if self.visited_table[self.short_paths[-1]][1] == -1:
                break
            self.short_paths.append(self.visited_table[self.short_paths[-1]][1])

    def __search(self, p):
        for i, j in self.node:
            if self.__check(i, j, p):
                continue

            if p != self.start:
                cost = self.node[(i, j)] + self.visited_table[p][0]
            else:
                cost = self.node[(i, j)]

            if i == p:
                if cost < self.visited_table[j][0] or self.visited_table[j][0] == -1:
                    self.visited_table[j] = [cost, i]
                    # check the next point
                if self.next_p[0] == -1 or self.next_p[1] > cost:
                    self.next_p[0] = j
                    self.next_p[1] = cost
            elif j == p:
                if cost < self.visited_table[i][0] or self.visited_table[i][0] == -1:
                    self.visited_table[i] = [cost, j]
                if self.next_p[0] == -1 or self.next_p[1] > cost:
                    self.next_p[0] = i
                    self.next_p[1] = cost
        self.visited.append(p)
        self.unvisited.remove(p)

    def find(self):
        p = self.start
        while len(self.unvisited) != 0:
            self.__search(p)
            if self.next_p[0] == self.end and len(self.unvisited) != 0:
                p = self.unvisited[0]
            else:
                p = self.next_p[0]
            if len(self.unvisited) != 0 and p == -1:
                p = self.unvisited[0]
            self.next_p = [-1, -1]
        self.total_cost = self.visited_table[self.end][0]
        self.__find_path()

    def get_visited_table(self):
        # return Dictionary
        return self.visited_table

    def get_short_paths(self):
        # return List
        return self.short_paths[::-1]

    def get_cost(self):
        # return integer
        return self.total_cost
