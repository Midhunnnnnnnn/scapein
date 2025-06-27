

# ScrapeRIn: Your Smart Web Scraper

ScrapeRIn is a FastAPI service designed for reliable web scraping. It intelligently extracts images and page content from a list of URLs, adapting its approach to ensure you get the data you need.

## How it Works (Tiered Scraping)

ScrapeRIn uses a "best-of-breed" approach to get page content:

1.  **First Try: Splash (for JavaScript)**: It first tries to get the page using Splash, which is great for websites that rely heavily on JavaScript.
2.  **Fallback 1: Aiohttp (Simple & Fast)**: If Splash doesn't work, or if it's not needed, ScrapeRIn uses a faster, simpler `aiohttp` scraper.
3.  **Fallback 2: Playwright (Guaranteed Content)**: If both the above methods return empty content, ScrapeRIn automatically switches to Playwright (a headless Chrome browser). This ensures you get the fully rendered page, even with complex JavaScript.

## Key Features

  * **Smart Scraping**: Automatically chooses the best method (Splash, aiohttp, or Playwright) to get page content.
  * **Image Extraction**: Can optionally find and list all image URLs on a page.
  * **Content Details**: Extracts the page title, a short text summary, the full page content, and even a "similarity score" if you provide a search query.
  * **Performance Boost**: Uses caching to make repeated scrapes faster and reduce unnecessary requests.
  * **Handles Tough Sites**: Built to handle modern, dynamic, and even protected websites.

## Get Started

### What You Need

  * Python 3.11 or newer
  * Docker (to run Splash)

### Installation Steps

1.  **Get the Code:**

    ```bash
    git clone https://github.com/Midhunnnnnnnn/ScapeRIN.git
    cd ScrapeRIN
    ```

2.  **(Optional) Set Up a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate # Use `venv\Scripts\activate` on Windows
    ```

3.  **Install Python Libraries:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Start Splash (with Docker):**

    ```bash
    docker run -p 8050:8050 scrapinghub/splash
    ```

    This makes Splash available at `http://localhost:8050`.

5.  **Install Playwright:**

    ```bash
    pip install playwright
    playwright install
    ```

6.  **Run ScrapeRIn:**

    ```bash
    uvicorn app.main:app --reload
    ```

    Your ScrapeRIn service will now be running at `http://localhost:8000`.

## How to Use the API

Send a POST request to the `/scrape` endpoint. Here's an example:

```json
{
  "urls": [
    "https://example.com"
  ],
  "query": "web scraping",
  "include_images": true,
  "browser_enabled": false
}
```

**Understanding `browser_enabled`:**

  * **`"browser_enabled": false` (Default)**: ScrapeRIn will try Splash/aiohttp first. If the content is empty, it *automatically* falls back to Playwright to ensure you get the full page. This is the recommended setting for most cases.
  * **`"browser_enabled": true`**: ScrapeRIn will *always* use Playwright directly for scraping. Use this if you know the pages require full browser rendering from the start.

### What You Get Back

The service will respond with a JSON object like this:

```json
{
  "results": [
    {
      "query": "web scraping",
      "images": [
        "https://example.com/image1.jpg",
        "https://example.com/image2.png"
      ],
      "result": {
        "title": "Example Domain",
        "url": "https://example.com",
        "content": "This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.",
        "score": 0.85,
        "raw_content": "Full text of the page goes here..."
      },
      "response_time": 5.12
    }
  ]
}
```

**Important**: If you don't provide any URLs, the API will return a `400 Bad Request` error.

Happy scraping\!
