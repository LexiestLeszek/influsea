import requests

def calculate_engagement_rate(likes, comments, shares, followers):
    engagement_rate = ((likes + comments + shares) / followers) * 100
    return engagement_rate

def get_top_users_by_hashtag(hashtag):
    access_token = 'YOUR_ACCESS_TOKEN'
    api_url = f'https://api.instagram.com/v1/tags/{hashtag}/media/recent?access_token={access_token}'

    try:
        response = requests.get(api_url)
        data = response.json()

        users = {}
        for post in data['data']:
            username = post['user']['username']
            likes = post['likes']['count']
            comments = post['comments']['count']
            shares = post['shares']['count']
            followers = post['user']['followers']['count']

            engagement_rate = calculate_engagement_rate(likes, comments, shares, followers)

            if username in users:
                users[username] += engagement_rate
            else:
                users[username] = engagement_rate

        top_users = sorted(users.items(), key=lambda x: x[1], reverse=True)[:10]

        return top_users

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage
hashtag = 'your_hashtag'
top_users = get_top_users_by_hashtag(hashtag)
for user, engagement_rate in top_users:
    print(f"User: {user}, Engagement Rate: {engagement_rate}")