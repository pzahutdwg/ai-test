import data
import unidecode

exclude = [
    "(",
    ")",
    "!",
    ".",
    ",",
    "?",
    ";",
    ":",
    '"',
    "'",
    "[",
    "]",
    "{",
    "}",
    "<",
    ">",
    "/",
    "\\",
    "|",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "+",
    "_",
    "=",
    "~",
    "`",
    "�",
]

excludeSubject = [
    "!",
    ".",
    "?",
    ";",
    "[",
    "]",
    "{",
    "}",
    "<",
    ">",
    "/",
    "\\",
    "|",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "+",
    "_",
    "=",
    "~",
    "`",
    "�",
]

excludedWords = [
    "of",
    "as",
    "to",
    "and",
    "the",
    "a",
    "to",
    "of",
    "as",
    "in",
    "that",
    "there",
    "are",
    "eg",
    "or",
    "because",
    "they",
    "was",
    "for",
    "by",
    "at",
    "an",
    "this",
    "it",
    "its",
    "on",
    "has",
    "have",
    "than",
    "",
    "with",
    "but",
    "not",
    "also",
    "such",
    "be",
    "which",
    "were",
    "from",
    " ",
    "had",
    "been",
    "their",
    "when",
    "them",
    "usually",
    "other",
    "many",
    "may",
    "these",
    "due",
    "who",
    "each",
    "can",
    "he",
    "she",
    "whereas",
    "if",
    "so",
    "more",
    "no",
    "all",
    "some",
    "what",
    "how",
    "why",
    "whoever",
    "whomever",
    "whichever",
    "whatever",
    "is",
    "are",
    "was",
    "were",
    "be",
    "being",
    "been",
    "am",
    "do",
    "does",
    "did",
    "doing",
    "done",
    "will",
    "shall",
    "should",
    "could",
    "would",
    "might",
    "must",
]


def justWords():
    new = data.subjects
    for subject in new:
        for p, paragraph in enumerate(new[subject]["paragraphs"]):
            # Create a new list to avoid modifying while iterating
            cleaned_words = []

            for word in paragraph:
                foo = word.split("[")[0]
                foo = unidecode.unidecode(foo)  # Normalize unicode characters

                # Clean characters first
                for char in exclude:
                    foo = foo.replace(char, "")

                # Check if word should be excluded after cleaning
                if (
                    foo not in excludedWords and foo.strip()
                ):  # Also exclude empty/whitespace-only words
                    cleaned_words.append(foo)
                else:
                    if foo == "" or foo == " " or not foo.strip():
                        print("<blank> was excluded")
                    else:
                        print('"' + foo + '"', "was excluded")

            # Replace the paragraph with cleaned words
            new[subject]["paragraphs"][p] = cleaned_words

    data.subjects = new
    print()


def justWords2(paragraph):
    cleaned_paragraph = []

    for word in paragraph:
        print(word, "<< before")
        word = word.split("[")[0]
        word = unidecode.unidecode(word)  # Normalize unicode characters
        print(word, "<< after")

        # Clean characters
        for char in exclude:
            word = word.replace(char, "")

        if word not in excludedWords and word.strip():
            cleaned_paragraph.append(word)
        else:
            if word == "" or word == " " or not word.strip():
                print("<blank> was excluded")
            else:
                print('"' + word + '"', "was excluded")

    print()
    return cleaned_paragraph

def justSubject(text):
    cleaned_text = ""
    for word in text.split():
        word = word.split("[")[0]
        word = unidecode.unidecode(word)
        for char in excludeSubject:
            word = word.replace(char, "")
        if word.strip():
            cleaned_text += " " + word
            
    print(cleaned_text.strip())
    return cleaned_text.strip()
