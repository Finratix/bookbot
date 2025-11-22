def WordsCounter(contentOfBook):
    content = contentOfBook.split()
    return f"Found {len(content)} total words"

def CharacterCounter(contentOfBook):
    charactersDictionary = {}
    for character in contentOfBook:
        character = character.lower()
        if character in charactersDictionary:
            charactersDictionary[character] += 1
        else:
            charactersDictionary[character] = 1
    return charactersDictionary

def SortCharacterCounter(charactersDictionary):
    def sort_on(items):
        return items["num"]

    characterList = []
    for character in charactersDictionary:
        characterList.append({"char": character, "num": charactersDictionary[character]})
    characterList.sort(reverse=True, key=sort_on)
    return characterList

def PrintTextForBookStatsReport(wordsCounterString, characterList, pathToBook):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {pathToBook}")
    print("----------- Word Count ----------")
    print(wordsCounterString)
    print("--------- Character Count -------")
    for characterDictionary in characterList:
        if characterDictionary['char'].isalpha():
            print(f"{characterDictionary['char']}: {characterDictionary['num']}")
    print("============= END ===============")

def BookStatsReport(contentOfBook, pathToBook):
    wordsCounterString = WordsCounter(contentOfBook)
    characterList = SortCharacterCounter(CharacterCounter(contentOfBook))
    PrintTextForBookStatsReport(wordsCounterString, characterList, pathToBook)







