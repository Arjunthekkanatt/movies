import random

movies={
    "excited":[
        "The Avengers",
        "interstellar",
        "Justice league",
        "Death race",
        "The expendebles"
    ],
    "romantic":[
        "Name is adeline",
        "meet joe black",
        "titanic",
        "The NoteBook",
        "Crazy Rich asians"
    ],
    "bored":[
        "Hangover",
        "jurney 2",
        "Mummy returns",
        "Lion king mufasa",
        "Bullet train"
    ],
    "happy":[
        "The pursuit of happiness",
        "Rocky III",
        "La La Land",
        "The pursuit of happiness",
        "Sing"
    ],
    "sad":[
        "the fault in our stars",
        "Marley and me",
        "blue valentine",
        "Schindlers list",
        "manchester by the sea"
    ]
}

def recommended(mood):
    mood = mood.lower()
    if mood in movies:
        movie = random.choice(movies[mood])
        print(f"\n Based on your mode({mood},you should watch : \n{movie}")
    else:
        print("sorry we dont have recommendation for your mode. Please try one of these:")
        print("-"+"\n - ".join(movies.keys()))

user_mood = input("what's your current moood? (excited,Romantic,bored,Sad,happy):")
recommended(user_mood)


