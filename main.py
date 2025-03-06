import data as d
data = d.subjects

import justWords as words

# Most of the paragraphs (if not all) are taken from Wikipedia

def backup():
    with open("justInCase.py", "w") as file:
        print('backing up...')
        file.write("subjects = " + str(data))


def rewrite():
    backup()
    open('data.py', 'w').close()
    with open("data.py", "w") as file:
        print('rewriting...')
        file.write("subjects = " + str(data))
    backup()


def train(paragraph, subject, data):
    subject = subject.lower()
    paragraph = paragraph.lower()
    paragraph = paragraph.split()
    paragraph = words.justWords2(paragraph)
    print(data)

    for thing in data:
        for extraName in data[thing]["names"]:
            if subject == extraName:
                subject = thing
                newNick = thing
                break

    if subject not in data:

        data[subject] = {"names": [subject], "paragraphs": [paragraph]}
        rewrite()

    elif newNick not in data[subject]["names"]:

        data[subject]["names"].append(newNick)
        rewrite()

    data[subject]["paragraphs"].append(paragraph)
    rewrite()

    data = words.justWords(data)
    data = words.justWords(data)
    rewrite()


def test(paragraph):
    paragraph = paragraph.lower()
    paragraph = paragraph.split()
    paragraph = words.justWords2(paragraph)
    paragraph = words.justWords2(paragraph)

    probabilities = {}

    for subject in data:
        probabilities[subject] = 0

    total = len(paragraph)
    probToReturn = []

    for subject in data:

        for word in paragraph:

            for para in data[subject]["paragraphs"]:

                if word in para:
                    probabilities[subject] += 1
                    print(
                        '"' + word + '" was found in',
                        subject
                        + ". ("
                        + str(probabilities[subject])
                        + "/"
                        + str(total)
                        + ")",
                    )
                    continue

        print()

    for subject in probabilities:

        probToReturn.append(round((probabilities[subject] / total) * 100, 2))
        probabilities[subject] = round((probabilities[subject] / total) * 100, 2)

    print(probabilities)
    print(sorted(probToReturn, reverse = True))
    return sorted(probabilities, key=probabilities.get, reverse=True), sorted(probToReturn, reverse = True), 


def newNicks(subject):
    commons = {}
    print(subject)
    for paragraph in data[subject]["paragraphs"]:
        for word in paragraph:
            if word in commons:
                commons[word] += 1
            else:
                commons[word] = 1

    possibleNicks = sorted(commons, key=commons.get, reverse=True)
    print(
        "Some common words in the " + subject + " subject are " + str(possibleNicks[0]) + ",", str(possibleNicks[1]) + ", and", str(possibleNicks[2]) + ".",
    )
    possibleNicks = [possibleNicks[0], possibleNicks[1], possibleNicks[2]]


def select():
    mode = input(">> ").lower()
    if mode == "train":

        print("Please enter the paragraph you would like to train the AI with.")
        paragraph = input(">> ")
        print("What is the subject of this paragraph?")
        subject = input(">> ")
        train(paragraph, subject)

    elif mode == "test":

        print("Please enter the paragraph you would like to test the AI with.")
        paragraph = input(">> ")
        print("\n-----------------------------------------------------------------\n")
        guess, percent = test(paragraph)

        print("\nGuessing from the following subjects:")
        for subject in data:
            print(subject)
        print()

        print(
            "The AI predicts that the subject of this paragraph is " + str(guess[0]),
            "(" + str(round(percent[0], 2)) + "% match)",
        )
        print(newNicks(guess[0]))

        print('Some other subjects that were also close guesses were', guess[1] + ' (' + str(round(percent[1], 2)) + '% match),', guess[2] + ' (' + str(round(percent [2], 2)) + '% mach), and', guess[3] + ' (' + str(round(percent[3], 2)) + '% match).')

        print("Was", guess[0], "correct?")
        correct = input(">> ").lower()
        if correct == "no":
            print("What is the subject of this paragraph?")
            subject = input(">> ")
            print("Should I train the AI with this paragraph?")
            toTrain = input(">> ").lower()
            if toTrain == "yes":
                train(paragraph, subject, data)
        else:
            train(paragraph, guess[0], data)

    elif mode == "exit":
        rewrite()
        exit()

    elif mode == "nicknames":
        newNicks()

    else:
        print(
            'Invalid input. Please try again. (Enter "train", "nicknames", "exit", or "test")'
        )
        select()


def main():

    print("---------------------------------------------------------------\n")
    print("Would you like to train, add nicknames (nicknames), exit or test?")
    select()
    main()


backup()
data = words.justWords(data)
rewrite()

print("\nWelcome to my first attempt at an AI!")
print("The goal of this is to take a paragraph and guess it's subject.\n")

main()
