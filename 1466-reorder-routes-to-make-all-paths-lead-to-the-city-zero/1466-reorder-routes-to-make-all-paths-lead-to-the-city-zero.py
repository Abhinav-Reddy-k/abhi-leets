class Solution:
    def minReorder(self, n, connections):
        cns = {(a, b) for a, b in connections}
        gph = collections.defaultdict(list)

        for a, b in connections:
            gph[a].append(b)
            gph[b].append(a)

        visit = set()

        def dfs(city):
            if city in visit:
                return 0

            visit.add(city)
            count = 0
            for ngbr in gph[city]:
                if ngbr in visit:
                    continue
                if (ngbr, city) not in cns:
                    count += 1
                count += dfs(ngbr)
            return count

        return dfs(0)