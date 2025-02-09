from newsapi import NewsApiClient

async def get_headlines(user_category: str, key: str) -> dict:
    news_api = NewsApiClient(api_key=key)

    try:
        top_headlines = news_api.get_top_headlines(category=user_category)
        return top_headlines["articles"][:5]
    except:
        print('Something went wrong with the API call.')