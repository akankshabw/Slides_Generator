from slide_generator.web_search import search_duckduckgo
from slide_generator.scraper import scrape_and_extract_text
from slide_generator.summarizer import summarize_content, generate_slide_deck
from slide_generator.ppt_builder import create_ppt_from_text
from slide_generator.config import DEFAULT_OUTPUT_FILE, DEFAULT_NUM_RESULTS

def main():
    topic = input("Enter topic for the presentation: ")
    urls = search_duckduckgo(topic, num_results=DEFAULT_NUM_RESULTS)
    all_text = ""
    for url in urls:
        extracted = scrape_and_extract_text(url)
        all_text += extracted + "\n"

    if not all_text.strip():
        print(" No usable text extracted from web. Exiting.")
        return
    
    summary = summarize_content(all_text, topic)
    slides = generate_slide_deck(topic, summary)
    create_ppt_from_text(slides, filename=DEFAULT_OUTPUT_FILE)

if __name__ == "__main__":
    main()