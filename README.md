# Slides Deck Generator using LLM + Web Search

This tool automatically generates a **7-slide PowerPoint presentation** from any given topic by combining:

- Real-time web search (DuckDuckGo)
- Article parsing (via `newspaper3k`)
- Summarization and slide planning (via Cohere LLM)
- Beautifully formatted `.pptx` output (via `python-pptx`)

---

## Project Structure

```
slide_generator_project/
├── slide_generator/
│   ├── __main__.py        # Entrypoint for running the app
│   ├── config.py          # Global constants and configuration
│   ├── ppt_builder.py     # Creates and styles PowerPoint slides using python-pptx
│   ├── scraper.py         # Extracts article text from URLs using newspaper3k
│   ├── summarizer.py      # Generates summaries and slide content
│   ├── web_search.py      # Performs DuckDuckGo search and extracts result URLs
│
├── .env                   # Environment file with COHERE_API_KEY
├── output.pptx            # Generated PowerPoint presentation
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

```

---

## How to Run

1. **Install dependencies**:

```bash
pip install -r requirements.txt
```

2. **Add your Cohere API key** in a `.env` file:

```env
COHERE_API_KEY=your_api_key_here
```

3. **Run the script**:

```bash
python -m slide_generator
```

You’ll be prompted:

```
Enter the topic for the presentation:
```

Example input: `AI in Healthcare`  
Output: `output.pptx` in the root directory