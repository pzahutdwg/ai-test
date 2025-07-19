import wikipedia as wiki
from wikipedia.exceptions import DisambiguationError, PageError
import requests
from bs4 import BeautifulSoup as bs
import main as m
import data as d
import justWords as words
import time
data = d.subjects

def printContent(url):
    response = requests.get(url)
    soup = bs(response.content, features='html.parser')
    paragraphs = soup.find_all('p')
    print(f"Number of paragraphs found: {len(paragraphs)}")
    print('\n=====================================================================\n')

def train(url, title):
    title = title.lower()
    title = words.justSubject(title)
    if not title in data:
        m.trainUrl(url, title)
        print(f"Added {title} to subjects ({url}).")

def main():
    
    amount = int(input("How many random pages do you want to train? "))
    antiStub = int(input('Minimum page length: '))
    print("Training random pages...")
    iterations = 0
    
    start = time.time()
    
    for _ in range(amount):
        iterations += 1
        print(f"Iteration {iterations}/{amount}.\n")
        bad = True

        while bad:
            try:
                title = wiki.random(1)
                url = wiki.page(title).url
                if len(wiki.page(title).content) < antiStub:
                    print(f"Skipping {title} due to insufficient content length.")
                    continue
                print(f"URL for '{title}': {url}")
                # printContent(url)
                train(url, title)
                bad = False
            except (DisambiguationError, PageError):
                continue
        
        print('\n=====================================================================\n')
    end = time.time()
    print(f"Training completed in {end - start:.2f} seconds (About {round((end - start) / amount, 2)} seconds per page).")
main()