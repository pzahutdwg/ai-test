exclude = ['(', ')', '!','.',',','?',';',':','"','\'','[',']','{','}','<','>','/','\\','|','@','#','$','%','^',"&",'*','+','-','_','=','~','`','1','2','3','4','5','6','7','8','9','0', '�']

excludedWords = ['of', 'as', 'to', 'and', 'the', 'a', 'to', 'of', 'as', 'in', 'that', 'there', 'are', 'eg', 'or', 'because', 'they', 'was', 'for', 'by', 'at', 'an', 'this', 'it', 'its', 'on', 'has', 'have', 'than' ,'', 'with', 'but', 'not', 'also', 'such', 'be', 'which', 'were', 'from', ' ', 'had', 'been', 'their', 'when', 'them', 'usually', 'other', 'many', 'may', 'these', 'due', 'who', 'each', 'can', 'he', 'she', 'is', 'like', 'often', 'then', 'while', 'whether']

def justWords(new):

    for subject in new:
        for p, paragraph in enumerate(new[subject]["paragraphs"]):
            for i, word in enumerate(paragraph):
                if word in excludedWords:
                    if word == '' or word == ' ':
                        print("<blank> was excluded from", subject)
                    else:
                        print("\"" + word + "\"", "was excluded from", subject)
                    new[subject]["paragraphs"][p].remove(word)
                    continue
                
                for char in word:
                    if char in exclude:
                        print(p)
                        print(word, '<< before')
                        new[subject]["paragraphs"][p][i] = new[subject]["paragraphs"][p][i].replace(char, "")
                        print(new[subject]["paragraphs"][p][i], '<< after')
    print()
    return new

def justWords2(paragraph):

    for i, word in enumerate(paragraph):

        if word in excludedWords:
                    if word == '' or word == ' ':
                        print("<blank> was excluded from anonymous paragraph")
                    else:
                        print("\"" + word + "\"", "was excluded from anonymous paragraph")
                    paragraph.remove(word)
                    continue
        
        for char in word:
            if char in exclude:
                print(word, "<< before")
                paragraph[i] = paragraph[i].replace(char, "")
                print(paragraph[i], "<< after")
                
    print()
    return paragraph
