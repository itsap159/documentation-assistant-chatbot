from bs4 import BeautifulSoup
import os

def parse_html_files(directory):
    docs = {}
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')
                # Extract relevant information, e.g., titles and content
                title = soup.find('title').text
                content = soup.get_text()
                docs[title] = content
    return docs
if __name__ == '__main__':
    docs = parse_html_files('langchain-docs')
    print(docs)
