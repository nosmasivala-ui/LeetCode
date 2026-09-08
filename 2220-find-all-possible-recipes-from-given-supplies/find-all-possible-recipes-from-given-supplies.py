class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        cooked = set()
        changed = True

        while changed:
            changed = False
            for r, ing_list in zip(recipes, ingredients):
                if r not in cooked and all(ing in supplies for ing in ing_list):
                    cooked.add(r)
                    supplies.add(r)
                    changed = True

        return list(cooked)