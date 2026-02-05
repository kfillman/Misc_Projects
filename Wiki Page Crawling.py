# Wiki Page Speedrun

import requests
from bs4 import BeautifulSoup
import random

def get_links(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/wiki/')]
    title = soup.find(id="firstHeading")
    print(title.text)
    return ['https://en.wikipedia.org' + link for link in links]

def find_path(start_url, end_url):
    queue_visited = [(start_url, [start_url])]
    
    while queue_visited:
        current_url, path = queue_visited.pop(0)
        if current_url == end_url:
            return path

        print(len(queue_visited))
        links = get_links(current_url)
        for link in links:
            if link not in [i[0] for i in queue_visited]:
                new_path = path + [link]
                queue_visited.append((link, new_path))

    return None

# Example usage
start_article = "https://en.wikipedia.org/wiki/Web_scraping"
end_article = "https://en.wikipedia.org/wiki/Poitou"

path = find_path(start_article, end_article)
if path:
    print("Path found:")
    for step in path:
        print(step)
else:
    print("No path found between the articles.")