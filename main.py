class Recipe:
    def __init__(self, name, ingredients, difficulty, time, rating, URL):
        self.name:         str     =  name 
        self.ingredients:  set     =  ingredients
        self.difficulty:   int     =  difficulty 
        self.time:         int     =  time 
        self.rating:       float   =  rating 
        self.URL:          str     =  URL

    def __str__(self):
        return f"\nName: {self.name} \nIngredients: {self.ingredients} \nDifficulty: {self.difficulty} \n Time: {self.time} \nRating: {self.rating} \nURL: {self.URL}\n"

#Wrapped object declaration
if True:
    recipeList = []
    bread_bun = Recipe("Bread bun", ["Milk", "Yeast", "Flour", "Salt", "Oil"], 2, 60, 4.3, "https://www.ica.se/recept/kallarfranska-729217/")
    recipeList.append(bread_bun)
    chicken = Recipe("Chicken", ["Chicken", "Oil", "Dijon mustard", "Soy", "Honey", "Thyme", "Salt", "Pepper", "Water"], 1, 60, 4.6, "https://www.ica.se/recept/helstekt-kyckling-i-ugn-729067/")
    recipeList.append(chicken)
    mango_sorbet = Recipe("Mango sorbet", ["Mango", "Milk", "Coconut flakes"], 1, 15, 4.7, "https://www.ica.se/recept/mangosorbet-med-kokos-725888/")
    recipeList.append(mango_sorbet)
    mayonnaise = Recipe("Mayonnaise", ["Mayonnaise", "Misopasta", "Salt"], 1, 15, 4.5, "https://www.ica.se/recept/misomajonnas-725204/")
    recipeList.append(mayonnaise)
    popcorn = Recipe("Popcorn", ["Popcorn", "Butter", "Sriracha sauce", "Lime"], 1, 15, 4.7, "https://www.ica.se/recept/popcorn-med-chili-och-lime-724046/")
    recipeList.append(popcorn)
    padron_peppers = Recipe("padron_peppers", ["Creme fraiche", "Parmesan", "Pepper", "Oil"], 1, 15, 4.5, "https://www.ica.se/recept/padrones-med-parmesandipp-724049/")
    recipeList.append(padron_peppers)
    waffles = Recipe("Waffles", ["Butter", "Flour", "Baking soda", "Salt", "Egg", "Milk"], 1, 45, 3.6, "https://www.ica.se/recept/grundrecept-vaffelsmet-292887/")
    recipeList.append(waffles)
    feta_cheese = Recipe("Feta cheese", ["Feta cheese", "Thyme", "Oregano", "Garlic", "Oil"], 1, 60, 4.0, "https://www.ica.se/recept/marinerad-fetaost-727845/")
    recipeList.append(feta_cheese)
    sriracha_hollandaise = Recipe("Sriracha hollandaise", ["Hollandaise sauce", "Pepper sauce"], 1, 15, 4.0, "https://www.ica.se/recept/srirachahollandaise-728214/")
    recipeList.append(sriracha_hollandaise)
    sugar = Recipe("Sugar", ["Sugar"], 1, 0, 5, "-")
    recipeList.append(sugar)

#Ingredient input
def ingredientInput():
    loop1 = True
    while loop1 == True:
        try:
            numOfIngredients = int(input("How many ingredients do you want to enter?: "))
            loop1 = False
        except ValueError: 
            print("Please enter a valid integer!")

    ingredientsList = []
    while numOfIngredients > 0:
            element = str(input("Enter an ingredient: "))

            if filterMethods.validIngredients(element) == False:
                print("Please enter a valid string!")
            else:
                ingredientsList.append(element)
                numOfIngredients -= 1

    #Applies correct capitalization
    for i in range(len(ingredientsList)):
        ingredientsList[i] = ingredientsList[i].capitalize()
    return ingredientsList

#Class containing methods for filtering
class filterMethods:
    @staticmethod
    def validIngredients(ingredients):
        for i in ingredients:
            if i.isdigit():
                return False
    
    suitableRecipesList = []
    @staticmethod
    def findRecipe(recipeList, ingredients):
        suitableRecipes = []
        for i in recipeList:
            if set(i.ingredients).issubset(set(ingredients)):
                suitableRecipes.append(i.name)
                filterMethods.suitableRecipesList.append(i)
        return suitableRecipes

    @staticmethod
    def findDifficulty(recipeList, difficulty):
        list = []
        for i in recipeList:
            if i.difficulty == difficulty:
                list.append(i)
        return list

    @staticmethod
    def findTime(recipeList, time1, time2):
        list = []
        for i in recipeList:
            if time1 <= i.time <= time2:
                list.append(i)
        return list

    @staticmethod
    def findRating(recipeList, grade1, grade2):
        list = []
        for i in recipeList:
            if float(grade1) <= i.rating <= float(grade2):
                list.append(i)
        return list

    @staticmethod
    def isValidSelection(input):
        if str(input) in ["Difficulty", "difficulty", "Time", "time", "Rating", "rating", "Exit", "exit"]:
            return True
        return False

#Loop for filter-application
previousFilters = []
def filterLoop(filteredList):
    selectionLoop = True
    while selectionLoop == True:
        selection1 = input("\nTo filter based on difficulty, type \"Difficulty\".\nTo filter based on time, type \"Time\".\nTo filter based on rating, type \"Rating\".\nTo exit, type \"Exit\".\n")
        
        if filterMethods.isValidSelection(selection1) == True:
            selectionLoop = False
        else:
            print("\nPlease enter a valid input!")

    if selection1 in ["Exit", "exit"]:
        return -1

    if selection1 in ["Difficulty", "difficulty"]:
        difficultySelection = int(input("Choose the wanted difficulty: "))
        filteredList = (filterMethods.findDifficulty(filteredList, difficultySelection))
        filteredListStr = ", ".join([i.name for i in filteredList])
        print(f"\nThe following recipes match your filters: {filteredListStr}!")
        return (filterLoop(filteredList))

    elif selection1 in ["Time", "time"]:
        timeLimit1 = int(input("Choose the first time-limit: "))
        timeLimit2 = int(input("Choose the first time-limit: "))
        filteredList = (filterMethods.findTime(filteredList, timeLimit1, timeLimit2))
        filteredListStr = ", ".join([i.name for i in filteredList])
        print(f"\nThe following recipes match your filters: {filteredListStr}!")
        return (filterLoop(filteredList))

    elif selection1 in ["Rating", "rating"]:
        ratingLimit1 = float(input("Choose the first rating-limit: "))
        ratingLimit2 = float(input("Choose the first rating-limit: "))
        filteredList = (filterMethods.findRating(filteredList, ratingLimit1, ratingLimit2))
        filteredListStr = ", ".join([i.name for i in filteredList])
        print(f"\nThe following recipes match your filters: {filteredListStr}!")
        return (filterLoop(filteredList))

def main():
    #Outputs suitable recipes
    suitableRecipesStr = ", ".join(filterMethods.findRecipe(recipeList, ingredientInput()))
    print(f"\nYou can cook these recipes: {suitableRecipesStr}")

    #Starts filtering recursion-loop
    print(filterLoop(filterMethods.suitableRecipesList))

if __name__ == "__main__":
    main()
