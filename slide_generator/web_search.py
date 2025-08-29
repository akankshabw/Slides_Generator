import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, unquote
from slide_generator.config import DEFAULT_NUM_RESULTS

HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.141 Safari/537.36"
    }

def search_duckduckgo(query, num_results=DEFAULT_NUM_RESULTS):
    url = f"https://duckduckgo.com/html/?q={query}"
    
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")
    raw_links = [a['href'] for a in soup.select('.result__a')][:num_results]

    cleaned_links = []
    for raw in raw_links:
        parsed = urlparse(raw)
        query = parse_qs(parsed.query)
        if 'uddg' in query:
            real_url = unquote(query['uddg'][0])
            cleaned_links.append(real_url)

    return cleaned_links