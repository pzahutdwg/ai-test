import wikipedia as wiki
from wikipedia.exceptions import DisambiguationError, PageError
import requests
from bs4 import BeautifulSoup as bs
import main as m
import data as d
import justWords as words
data = d.subjects

def printContent(url):
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    print(f"Number of paragraphs found: {len(paragraphs)}")
    print('\n=====================================================================\n')
    for para in paragraphs:
        if para != '':
            print(para.get_text(), end='\n=====================================================================\n\n')

def train(url, title):
    title = title.lower()
    print("Doing the thing")
    title = words.justSubject(title)
    if not title in data:
        m.trainUrl(url, title)
        print(f"Added {title} to subjects ({url}).")

def main():
    
    amount = int(input("How many random pages do you want to train? "))
    print("Training random pages...")
    
    for _ in range(amount):
        bad = True

        while bad:
            try:
                title = wiki.random(1)
                url = wiki.page(title).url
                print(f"URL for '{title}': {url}")
                # printContent(url)
                train(url, title)
                bad = False
            except (DisambiguationError, PageError):
                continue
            
main()