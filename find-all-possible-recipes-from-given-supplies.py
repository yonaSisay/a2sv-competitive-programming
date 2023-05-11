class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        supplies = set(supplies)
        indgree = defaultdict(int)
        que = deque()
        ans = []

        for i,recipe in enumerate(recipes):
            for ing in ingredients[i]:
                if ing not in supplies: 
                    graph[ing].append(recipe)
                    indgree[recipe] += 1
        
        for recipe in recipes:
            if not indgree[recipe]:
                que.append(recipe)
        
        while que:
            temp = que.popleft()
            ans.append(temp)

            for elm in graph[temp]:
                indgree[elm] -= 1

                if not indgree[elm]:
                    que.append(elm)
        
        return ans