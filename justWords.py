import data

exclude = ['(', ')', '!','.',',','?',';',':','"','\'','[',']','{','}','<','>','/','\\','|','@','#','$','%','^',"&",'*','+','-','_','=','~','`','1','2','3','4','5','6','7','8','9','0', '�']

excludedWords = ['of', 'as', 'to', 'and', 'the', 'a', 'to', 'of', 'as', 'is', 'in', 'that', 'there', 'are', 'eg', 'or', 'because', 'they', 'was', 'for', 'by', 's', 'at', 'an', 'this', 'it', 'its', 'on', 'has', 'have', 'than' ,'', 'with', 'but', 'not']

def justWords():

    new = data.subjects
    for subject in new:
        for p, paragraph in enumerate(new[subject]["paragraphs"]):
            for i, word in enumerate(paragraph):
                if word in excludedWords:
                    print(word, "was excluded")
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

def justWords2(paragraph):

    for i, word in enumerate(paragraph):
        for char in word:
            if char in exclude:
                print(paragraph[i], "before")
                paragraph[i] = paragraph[i].replace(char, "")
                print(paragraph[i], "after")
                

    return paragraph
