from newspaper import Article
from slide_generator.config import MAX_ARTICLE_LENGTH

def scrape_and_extract_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text
        print(f"\n=== Extracted from {url} ===")
        print(text[:1000])
        print("===================================\n")
        return text[:MAX_ARTICLE_LENGTH]  
    except Exception as e:
        print(f" Failed to extract from {url}: {e}")
        return ""