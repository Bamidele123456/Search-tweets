import requests

bearer_token = "AAAAAAAAAAAAAAAAAAAAAIUXmgEAAAAAKkT4C5AGl6dy3xpN0Xu8qniIpBM%3DrLZTCakRyejwirFyIcuOOP9BjUk29Z7rGz7TJFd1ofwDccwPvO"

params = {
    "query": "suicide",
    "tweet.fields": "created_at",
    "max_results": 100
}

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json",
}

# Get recent tweets based on the specified query
response = requests.get("https://api.twitter.com/2/tweets/search/recent", headers=headers, params=params)

if response.status_code == 200:
    data = response.json().get('data', [])

    # Extract and print the text from each tweet
    for tweet in data:
        tweet_text = tweet.get('text')
        print(tweet_text)

        # Save the text to a .txt file
        with open('suicide.txt', 'a', encoding='utf-8') as file:
            file.write(tweet_text + '\n')

    print("Tweets saved to 'tweets.txt'")
else:
    print(f"Error: {response.status_code} - {response.text}")
