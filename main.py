# This is a sample Python script.
import random
import webbrowser
import urllib.request
import re
import time


def openInBrowser(randomThing):
    url = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=how+to+draw+" + randomThing)
    # webbrowser.open('https://www.youtube.com/results?search_query=how+to+draw+' + randomPokemon)
    video_ids = re.findall(r"watch\?v=(\S{11})", url.read().decode())

    curVid = 0
    webbrowser.open('https://www.youtube.com/watch?v=' + video_ids[curVid])

    nextVid = input('Try next video? (y/n)')
    while nextVid == 'y':
        curVid += 1
        while video_ids[curVid] == video_ids[curVid - 1]:
            curVid += 1
        webbrowser.open('https://www.youtube.com/watch?v=' + video_ids[curVid])
        nextVid = input('Try next video? (y/n)')


def drawPokemon():
    # gen = input('Which generation would you like? (enter 0 for every generation)')
    pokeFile = open("pokemon.txt")

    pokeRay = []

    for pokemon in pokeFile:
        pokeRay.append(pokemon)

    loadDrawing(pokeRay, 'pokemon')


def drawAnimal():
    animalFile = open("animals.txt")
    animalRay = []

    for animal in animalFile:
        animalRay.append(animal)

    loadDrawing(animalRay, 'animal')


def drawSuperhero():
    superFile = open("superheroes.txt")
    superRay = []

    for hero in superFile:
        superRay.append(hero)

    loadDrawing(superRay, 'hero')


def drawVideoGameCharacter():
    print('Coming soon')


def drawAnimatedMovieCharacter():
    print('Coming soon')


def loadDrawing(ray, thingName):
    continueLoop = True
    while continueLoop:
        ready = input('Ready to get a random ' + thingName + '? (y/n)\n')

        if ready == 'y':
            randomThing = random.choice(ray)
            print('Your random ' + thingName + ' is ' + randomThing)

            openBrowser = input('Do you want to search for a drawing video in the browser? (y/n)\n')
            if openBrowser == 'y':
                # if randomAnimal.isspace():
                randomThing = randomThing.replace(' ', '+')
                openInBrowser(randomThing)

            else:
                print('Not opened in browser')

            again = input('Do you want to generate another random ' + thingName + '? (y/n)\n')
            if again == 'n':
                continueLoop = False
        else:
            continueLoop = False


def chooseOption():
    print('What would you like to draw today?')
    selectOption = input('You can type pokemon, animal, or superhero\n')  # , video game character, & animated movie character\n')

    if selectOption.lower() == 'pokemon':
        drawPokemon()

    elif selectOption.lower() == 'animal':
        drawAnimal()

    elif selectOption.lower() == 'superhero':
        drawSuperhero()

    elif selectOption.lower() == 'video game character':
        drawVideoGameCharacter()

    elif selectOption.lower() == 'animated movie character':
        drawAnimatedMovieCharacter()

    else:
        print('Option not found')


chooseOption()

while True:
    end = input('Try another option? (y/n)\n')
    if end == 'y':
        chooseOption()
    else:
        print('Ok bye')
        break


time.sleep(2)
