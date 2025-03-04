import data
import justWords as words
# Most of the paragraphs are taken from Wikipedia

def rewrite():
    with open("data.py", "w") as file:
        file.write("subjects = " + str(data.subjects) + "\n")

def train(paragraph, subject):
    subject = subject.lower()
    paragraph = paragraph.lower()
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
        rewrite()

    elif newNick not in data.subjects[subject]["names"]:

        data.subjects[subject]["names"].append(newNick)
        rewrite()
    
    data.subjects[subject]["paragraphs"].append(paragraph)
    rewrite()

    words.justWords()
    rewrite()

def test(paragraph):
    paragraph = paragraph.lower()
    paragraph = paragraph.split()
    paragraph = words.justWords2(paragraph)

    probabilities = {}

    for subject in data.subjects:
        probabilities[subject] = 0

    for subject in data.subjects:
        total = 0
        for paragraph2 in data.subjects[subject]["paragraphs"]:
            for word in paragraph:

                total += 1

                if word in paragraph2:
                    probabilities[subject] += 1
                    print(subject, word, str(probabilities[subject]) + "/" + str(total))

        probabilities[subject] = round((probabilities[subject] / total) * 100, 2)
    
    print(probabilities)
    return max(probabilities, key = probabilities.get)

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
        guess = test(paragraph)

        print('Guessing from the following subjects:')
        for subject in data.subjects:
            print(subject)
            
        print("The AI predicts that the subject of this paragraph is " + str(guess))
        print("Was that correct?")
        correct = input(">> ").lower()
        if correct == "no":
            print("What is the subject of this paragraph?")
            subject = input(">> ")
            print("Should I train the AI with this paragraph?")
            toTrain = input(">> ").lower()
            if toTrain == "yes":
                train(paragraph, subject)
        else:
            train(paragraph, guess)

    elif mode == "exit":
        exit()
        
    else:
        print("Invalid input. Please try again. (Enter \"train\", \"exit\", or \"test\")")
        select()
        
def main():
    
    print("---------------------------------------------------------------\n")
    print("Would you like to train or would you like to test?")
    select()
        
words.justWords()
rewrite()

print("\nWelcome to my first attempt at an AI!")
print("The goal of this is to take a paragraph and guess it's subject.\n")

main()
