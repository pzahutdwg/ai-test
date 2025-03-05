import data

exclude = ['(', ')', '!','.',',','?',';',':','"','\'','[',']','{','}','<','>','/','\\','|','@','#','$','%','^',"&",'*','+','-','_','=','~','`','1','2','3','4','5','6','7','8','9','0', '�']

excludedWords = ['of', 'as', 'to', 'and', 'the', 'a', 'to', 'of', 'as', 'is', 'in', 'that', 'there', 'are', 'eg', 'or', 'because', 'they', 'was', 'for', 'by', 'at', 'an', 'this', 'it', 'its', 'on', 'has', 'have', 'than' ,'', 'with', 'but', 'not', 'also', 'such', 'be', 'which', 'were', 'from', ' ', 'had', 'been', 'their', 'when', 'them']

def justWords():

    new = data.subjects
    for subject in new:
        for p, paragraph in enumerate(new[subject]["paragraphs"]):
            for i, word in enumerate(paragraph):
                if word in excludedWords:
                    if word == '' or word == ' ':
                        print("<blank> was excluded")
                    else:
                        print("\"" + word + "\"", "was excluded")
                    new[subject]["paragraphs"][p].remove(word)
                    data.subjects = new
                    continue
                
                for char in word:
                    if char in exclude:
                        print(p)
                        print(i, word)
                        new[subject]["paragraphs"][p][i] = new[subject]["paragraphs"][p][i].replace(char, "")
                        print(new[subject]["paragraphs"][p][i])
                        data.subjects = new
    print()

def justWords2(paragraph):

    for i, word in enumerate(paragraph):

        if word in excludedWords:
                    if word == '' or word == ' ':
                        print("<blank> was excluded")
                    else:
                        print("\"" + word + "\"", "was excluded")
                    paragraph.remove(word)
                    continue
        
        for char in word:
            if char in exclude:
                print(word, "<< before")
                paragraph[i] = paragraph[i].replace(char, "")
                print(paragraph[i], "<< after")
                
    print()
    return paragraph
