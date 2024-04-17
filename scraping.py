import requests
from bs4 import BeautifulSoup
import json

def get_dom(url):
    headers = {
        'User-Agent': ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/123.0.0.0 Safari/537.36")
    }

    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.content, 'html.parser')


# Gets all <a> tags
def get_links(dom):
    links = []
    for link in dom.find_all('a'):
        href = link.get('href')
        if (href.startswith("http://") or href.startswith("https://")):
            links.append(href)
    return links


def write_to_file(links):
    links_json = json.dumps(links)
    with open('links.json', 'w') as f:
        f.write(links_json)

    print("JSON sauvegardé dans le fichier 'links.json'")