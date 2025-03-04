import data

def train(paragraph, subject):
    subject = subject.lower()
    paragraph = paragraph.lower()
    paragraph = paragraph.split()
    
    for thing in data.subjects:
        for extraName in thing["names"]:
            if subject == extraName:
                subject = thing
                break
            
    
    if subject not in data.subjects:
        with open("data.py", "w") as file:
            data.subjects[subject] = {"names": [subject], "paragraphs": [paragraph]}
            file.write("subjects = " + str(data.subjects))
    else:
                
        for word in paragraph:
            pass #! This is where I left off

def test(paragraph):
    paragraph = paragraph.lower()
    paragraph = paragraph.split()
    return paragraph

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
        print("The AI predicts that the subject of this paragraph is: " + str(test(paragraph)))
        
    else:
        print("Invalid input. Please try again. (Enter \"train\" or \"test\")")
        select()
        
def main():
    
    print("---------------------------------------------------------------\n")
    print("Would you like to train or would you like to test?")
    select()
        
print("Welcome to my first attempt at an AI!")
print("The goal of this is to take a paragraph and guess it's subject.\n")

main()
