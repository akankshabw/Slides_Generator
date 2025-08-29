import cohere
from dotenv import load_dotenv
import os

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def summarize_content(text, topic):
    prompt = f"You are given the following text which is information gathered from internet. Use this and your own knowledge and create 20-25 bullet points for a presentation on '{topic}':\n\n{text}"
    response = co.chat(model="command-r-plus", message=prompt)
    return response.text

def generate_slide_deck(topic, summarized_points):
    prompt = f"""
    You are a professional presentation assistant. Use the following context to create a 7-slide presentation on "{topic}".

    --- CONTEXT START ---
    {summarized_points}
    --- CONTEXT END ---

    Slide Structure:
    1. Title Slide (only the topic)
    2. Overview
    3–6: Key ideas / trends / arguments  (each slide = title + 6-8 bullet points)
    7. Conclusion

    Guidelines:
    - Use concise, impactful titles.
    - Do not include slide numbers or any extra text or ###.
    - Output titles and bullet points clearly.
    - The ttle slide should contain the topic in the middle of the slide.
    - Give 6-8 bullet points for slides 3-6.
    """
    response = co.chat(model="command-r-plus", message=prompt)
    print("------------\nGenerated Slide Deck Content:\n", response.text)
    return response.text
