#Layer 1: Manga Genre Selection
print("Hello fellow manga enjoyer! What type of manga do you enjoy?")
print("1. Slice of Life")
print("2. Romance")
print("3. Drama")
genre_select = input("Please make your selection! (1/2/3) ---> ")

if genre_select == "1" :
    #Layer 1.2: Length
    print("You have selected Slife of Life!")
    print("What's your preferred Manga Length?")
    print("1. Long")
    print("2. Medium")
    print("3. Short")
    length = input("Make your choice! (1/2/3) --->")

    if length == "1" :
         #Layer 1.3: Decade
        print("You prefer a Longer Manga!")
        print("How long ago do you want your manga to be released on?")
        print("1. 2000s or Older")
        print("2. 2010s")
        print("3. 2020s")
        decade = input("Please make your choice! (1/2/3) ---> ")

        if decade == "1" :
            print("I recommend Yotsuba&! and Welcome to the NHK")
        elif decade == "2" :
            print("I recommend Kimi ni Todoke: From Me to You")
        elif decade == "3" :
            print("I recommend Bocchi the Rock!")
        else :
            print("Sorry! I cannot recommend a manga")
    
    elif length == "2" :
        print("You prefer a Medium-Lengthed Manga!")
        print("How long ago do you want your manga to be released on?")
        print("1. 2000s or Older")
        print("2. 2010s")
        print("3. 2020s")
        decade = input("Please make your choice! (1/2/3) ---> ")

        if decade == "1" :
            print("I recommend Hidamari Sketch")
        elif decade == "2" :
            print("I recommend March Comes in Like a Lion")
        elif decade == "3" :
            print("I recommend Skip and Loafer")
        else:
            print("Sorry! I cannot recommend a manga")
    
    elif length == "3" :
        print("You prefer a Shorter Manga!")
        print("How long ago do you want your manga to be released on?")
        print("1. 2000s or Older")
        print("2. 2010s")
        print("3. 2020s")
        decade = input("Please make your choice! (1/2/3) ---> ")

        if decade == "1" : 
            print("I recommend Solanin")
        elif decade == "2" :
            print("I recommend Anohana: The Flower We Saw That Day")
        elif decade == "3" :
            print("I recommend Boys Run the Riot")
        else :
            print("Sorry! I cannot recommend a manga")
    else :
        print("Sorry! I cannot recommend a manga")
elif genre_select == "2" :
    #Layer 2.2: Length
    print("You have selected Romance!")
    print("What's your preferred Manga Length?")
    print("1. Long")
    print("2. Medium")
    print("3. Short")
    length = input("Make your choice! (1/2/3) --->")

    if length == "1" :
         #Layer 2.3: Decade
        print("You prefer a Longer Manga!")
        print("How long ago do you want your manga to be released on?")
        print("1. 2000s or Older")
        print("2. 2010s")
        print("3. 2020s")
        decade = input("Please make your choice! (1/2/3) ---> ")

        if decade == "1" :
            print("I recommend Bokura ga Ita (We Were There)")
        elif decade == "2" :
            print("I recommend Horimiya")
        elif decade == "3" :
            print("I recommend Shikimoris Not Just a Cutie")
        else :
            print("Sorry! I cannot recommend a manga")
    
    elif length == "2" :
        print("You prefer a Medium-Lengthed Manga!")
        print("How long ago do you want your manga to be released on?")
        print("1. 2000s or Older")
        print("2. 2010s")
        print("3. 2020s")
        decade = input("Please make your choice! (1/2/3) ---> ")

        if decade == "1" :
            print("I recommend High School Debut")
        elif decade == "2" :
            print("I recommend My Little Monster")
        elif decade == "3" :
            print("I recommend Skip and Loafer")
        else:
            print("Sorry! I cannot recommend a manga")
    
    elif length == "3" :
        print("You prefer a Shorter Manga!")
        print("How long ago do you want your manga to be released on?")
        print("1. 2000s or Older")
        print("2. 2010s")
        print("3. 2020s")
        decade = input("Please make your choice! (1/2/3) ---> ")

        if decade == "1" : 
            print("I recommend Venus in Love")
        elif decade == "2" :
            print("I recommend Orange")
        elif decade == "3" :
            print("I recommend Were Just Friends")
        else :
            print("Sorry! I cannot recommend a manga")
    else :
        print("Sorry! I cannot recommend a manga")
elif genre_select == "3" :
    #Layer 3.2: Length
    print("You have selected Drama!")
    print("What's your preferred Manga Length?")
    print("1. Long")
    print("2. Medium")
    print("3. Short")
    length = input("Make your choice! (1/2/3) --->")

    if length == "1" :
         #Layer 3.3: Decade
        print("You prefer a Longer Manga!")
        print("How long ago do you want your manga to be released on?")
        print("1. 2000s or Older")
        print("2. 2010s")
        print("3. 2020s")
        decade = input("Please make your choice! (1/2/3) ---> ")

        if decade == "1" :
            print("I recommend Nana")
        elif decade == "2" :
            print("I recommend Tokyo Ghoul")
        elif decade == "3" :
            print("I recommend Frieren: Beyond Journeys End")
        else :
            print("Sorry! I cannot recommend a manga")
    
    elif length == "2" :
        print("You prefer a Medium-Lengthed Manga!")
        print("How long ago do you want your manga to be released on?")
        print("1. 2000s or Older")
        print("2. 2010s")
        print("3. 2020s")
        decade = input("Please make your choice! (1/2/3) ---> ")

        if decade == "1" :
            print("I recommend Alive: The Final Evolution")
        elif decade == "2" :
            print("I recommend A Silent Voice")
        elif decade == "3" :
            print("I recommend Insomniacs After School")
        else:
            print("Sorry! I cannot recommend a manga")
    
    elif length == "3" :
        print("You prefer a Shorter Manga!")
        print("How long ago do you want your manga to be released on?")
        print("1. 2000s or Older")
        print("2. 2010s")
        print("3. 2020s")
        decade = input("Please make your choice! (1/2/3) ---> ")

        if decade == "1" : 
            print("I recommend Our Happy Time")
        elif decade == "2" :
            print("I recommend A Girl on the Shore")
        elif decade == "3" :
            print("I recommend Goodbye, Eri")
        else :
            print("Sorry! I cannot recommend a manga")
    else :
        print("Sorry! I cannot recommend a manga")
else :
    print("Sorry! But I cannot recommend a manga")