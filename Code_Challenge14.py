#Goal: Create a code That Makes an Anime Watch List

anime_list = []

variable = True

while variable == True:
    anime = input("Anime Watch List Creator! Enter Anime Name Here! (Type Exit to Finish) ---> ")
    
    if anime.lower() == "exit":
        print("\nAlright! Here is Your Anime Watch List:")
        for anime in anime_list:
            print(f"- {anime}")
        break
    else:
        anime_list.append(anime)
        print("Anime Added to List!")
