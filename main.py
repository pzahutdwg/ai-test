import data
d = data.subjects
import justWords as words
import requests
from bs4 import BeautifulSoup as bs
# import random

# url = "https://en.wikipedia.org/wiki/Mathematics"
# response = requests.get(url)
# soup = bs(response.content, 'html.parser')
# paragraphs = soup.find_all('p')
# print(f"Number of paragraphs found: {len(paragraphs)}")
# for para in paragraphs:
#     print(para.get_text(), end='\n=====================================================================\n\n')

# Most of the paragraphs (if not all) are taken from Wikipedia

def backup():
    try:
        with open("justInCase.py", "w", encoding="utf-8") as file:
            file.write("subjects = " + str(data.subjects) + "\n")
    except Exception as e:
        print(f"Error during backup: {e}")

def rewrite():
    with open("data.py", "w") as file:
        file.write("subjects = " + str(data.subjects) + "\n")
    backup()


def trainUrl(url, subject):
    response = requests.get(url)
    soup = bs(response.content, "html.parser")
    paragraphs = soup.find_all("p")
    subject = subject.lower()
    subject = words.justSubject(subject)  # This returns a list

    for paragraph in paragraphs:
        paragraph = paragraph.get_text().lower()
        paragraph = paragraph.split()
        paragraph = words.justWords2(paragraph)


        for thing in data.subjects:
            for extraName in data.subjects[thing]["names"]:
                if subject == extraName:
                    subject = thing
                    newNick = thing
                    break

        if subject not in data.subjects:

            data.subjects[subject] = {"names": [subject], "paragraphs": [paragraph]}

        elif newNick not in data.subjects[subject]["names"]:

            data.subjects[subject]["names"].append(newNick)

        data.subjects[subject]["paragraphs"].append(paragraph)

        words.justWords()
        rewrite()


def train(paragraph, subject):
    d = data.subjects
    subject = subject.lower()
    paragraph = paragraph.lower()
    paragraph = paragraph.split()
    paragraph = words.justWords2(paragraph)

    newNick = subject  # Initialize newNick
    for thing in d:
        for extraName in d[thing]["names"]:
            if subject == extraName:
                subject = thing
                newNick = thing
                break

    if subject not in d:
        d[subject] = {"names": [subject], "paragraphs": [paragraph]}
        rewrite()

    elif newNick not in d[subject]["names"]:
        d[subject]["names"].append(newNick)
        rewrite()

    d[subject]["paragraphs"].append(paragraph)
    rewrite()

    words.justWords()
    words.justWords()
    rewrite()

def test(paragraph):
    paragraph = paragraph.lower()
    paragraph = paragraph.split()
    paragraph = words.justWords2(paragraph)
    paragraph = words.justWords2(paragraph)

    probabilities = {}

    for subject in data.subjects:
        probabilities[subject] = 0

    total = len(paragraph)
    probToReturn = []

    for subject in data.subjects:
        for word in paragraph:
            found = False  # Track if word was found in this subject
            
            for para in data.subjects[subject]["paragraphs"]:
                if word in para and not found:  # Only count once per subject
                    probabilities[subject] += 1
                    print(f'"{word}" was found in "{subject}". ({probabilities[subject]}/{total})')
                    found = True  # Mark as found to prevent double counting
                    break  # Exit paragraph loop once found
        print()

        

    for subject in probabilities:
        probToReturn.append(round((probabilities[subject] / total) * 100, 2))
        probabilities[subject] = round((probabilities[subject] / total) * 100, 2)

    if not probToReturn:
        return None, 0
    return sorted(probabilities, key=probabilities.get, reverse=True)[:5], sorted(probToReturn, reverse=True)[:5]

def newNicks(subject):
    commons = {}
    print(subject)
    for paragraph in data.subjects[subject]["paragraphs"]:
        for word in paragraph:
            if word in commons:
                commons[word] += 1
            else:
                commons[word] = 1

    possibleNicks = sorted(commons, key=commons.get, reverse=True)
    print(f'Some common words in the {subject} subject are "{possibleNicks[0]}", "{possibleNicks[1]}", and "{possibleNicks[2]}".')
    possibleNicks = [possibleNicks[0], possibleNicks[1], possibleNicks[2]]


def select():
    mode = input(">> ").lower()
    if mode == "train":

        print("Please enter a wikipedia webpage URL.")
        url = input(">> ")
        print("What is the subject of this webpage?")
        subject = input(">> ")
        trainUrl(url, subject)

    elif mode == "test":

        print("Please enter the paragraph you would like to test the AI with.")
        paragraph = input(">> ")
        print("\n=================================================================\n")
        guesses, percents = test(paragraph)

        print("\nGuessing from the following subjects:")
        for subject in data.subjects:
            print(subject, end=', ')

        print("\n=================================================================\n")

        print(f'The AI predicts that the subject of this paragraph is "{guesses[0]}", ({round(percents[0], 2)}% match).')
        newNicks(guesses[0])

        print(f'Some other close guesses were "{guesses[1]}" ({round(percents[1], 2)}% match), "{guesses[2]}" ({round(percents[2], 2)}% match), "{guesses[3]}" ({round(percents[3], 2)}% match), and "{guesses[4]}" ({round(percents[4], 2)}% match).\n')

        print("Was", guesses[0], "correct?")
        correct = input(">> ").lower()
        if correct == "no":
            print("What is the subject of this paragraph?")
            subject = input(">> ")
            print("Should I train the AI with this paragraph?")
            toTrain = input(">> ").lower()
            if toTrain == "yes":
                train(paragraph, subject)  # Remove extra 'data' parameter
        else:
            train(paragraph, guesses[0])  # Remove extra 'data' parameter

    elif mode == "exit":
        rewrite()
        exit()

    elif mode == "nicknames":
        print("What subject would you like to see nicknames for?")
        subject = input(">> ")
        newNicks(subject)

    else:
        print(
            'Invalid input. Please try again. (Enter "train", "nicknames", "exit", or "test")'
        )
        select()


def main():

    print("===============================================================\n")
    print("Would you like to train, add nicknames (nicknames), exit or test?")
    select()
    main()

if __name__ == "__main__":
    backup()
    words.justWords()
    rewrite()

    print("\nWelcome to my first attempt at an AI!")
    print("The goal of this is to take a paragraph and guess it's subject.\n")

    main()
