import pandas as pd
from fetch import (
fetch_headlines,
get_available_countries,
resolve_query
)

def main():
    print("=== Testing get_available_countries ===")
    countries = get_available_countries()
    print(countries)

    test_country = "Australia"
    test_topic = "economy"

    print("\n=== Testing resolve_query ===")
    query = resolve_query(test_topic, test_country)
    print(f"Resolved query: {query}")

    print("\n=== Testing fetch_headlines ===")
    try:
        df = fetch_headlines(query, days_back=3, page_size=10)

        if df.empty:
            print("No articles found.")
        else:
            print(f"Fetched {len(df)} articles")
            print(df.head())

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()