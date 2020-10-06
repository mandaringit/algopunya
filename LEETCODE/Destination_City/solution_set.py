class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        all_cities = set()
        not_dest_cities = set()

        for path in paths:
            all_cities.update(path)
            not_dest_cities.add(path[0])

        return list(all_cities - not_dest_cities)[0]
