import os
import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
 
load_dotenv()
 
API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"
 
COUNTRY_QUERIES = {
    "Australia": "Australia news",
    "USA": "United States news",
    "UK": "United Kingdom news",
    "China": "China news",
    "India": "India news",
    "Germany": "Germany news",
    "Japan": "Japan news",
    "Brazil": "Brazil news",
}

def fetch_headlines(query: str, days_back: int = 7, page_size: int = 100) -> pd.DataFrame:
    if not API_KEY:
        raise ValueError("NEWS_API_KEY not found, check .env file")
    
    from_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
 
    params = {
        "q": query,
        "from": from_date,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": page_size,
        "apiKey": API_KEY,
    }
 
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
 
    data = response.json()
    articles = data.get("articles", [])
 
    if not articles:
        return pd.DataFrame()
 
    rows = []
    for article in articles:
        rows.append({
            "title": article.get("title", ""),
            "description": article.get("description", ""),
            "published_at": article.get("publishedAt", ""),
            "source": article.get("source", {}).get("name", "Unknown"),
            "url": article.get("url", ""),
        })