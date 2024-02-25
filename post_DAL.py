import pandas as pd
from datetime import datetime


posts = pd.read_csv('demo_csvs/demo_posts.csv')
likes = pd.read_csv('demo_csvs/demo_likes.csv')
follows = pd.read_csv('demo_csvs/demo_followers.csv')
reposts = pd.read_csv('demo_csvs/demo_reposts.csv')


class PostAPI:
    def get_creation_time(uri):
        return pd.to_datetime(posts.loc[posts['uri'] == uri]["created_at"].values[0])
    
    def get_poster(uri):
        return posts.loc[posts['uri'] == uri]["did"].values[0]

    def get_all_likes(uri):
        return len(likes.loc[likes['subject_uri'] == uri])

    def get_likes_since(uri, time):
        return len(likes.loc[(likes['subject_uri'] == uri) & (pd.to_datetime(likes['created_at']) > time)])

    def get_all_reposts(uri):
        return len(reposts.loc[reposts['subject_uri'] == uri])

    def get_reposts_since(uri, time):
        return len(reposts.loc[(reposts['subject_uri'] == uri) & (pd.to_datetime(reposts['created_at']) > time)])

    def get_replies(uri):
        return len(posts.loc[posts['root_uri'] == uri])

    def get_replies_since(uri, time):
        return len(posts.loc[(posts['root_uri'] == uri) & (pd.to_datetime(posts['created_at']) > time)])
    
class UserAPI:
    def get_follows(subject): # uses did for subject
        return len(follows.loc[follows['subject'] == subject])

    def get_follows_since(subject, time): # uses did for subject
        return len(follows.loc[(follows['subject'] == subject) & (pd.to_datetime(follows['created_at']) > time)])
    
test_uri = "at://did:plc:test_poster/app.bsky.feed.post/test_post"
creation_time = PostAPI.get_creation_time(test_uri)
# print(creation_time)

current_time = pd.Timestamp.now(tz='UTC')
current_time = current_time.tz_convert('UTC')  
time_24_hours_ago = current_time - pd.Timedelta(hours=24)


# print(PostAPI.get_likes_since(uri=test_uri, time=time_24_hours_ago))
# print(PostAPI.get_replies_since(uri=test_uri, time=time_24_hours_ago))
# print(PostAPI.get_reposts_since(uri=test_uri, time=time_24_hours_ago))
# poster_did = PostAPI.get_poster(uri=test_uri)
# print(UserAPI.get_follows_since(subject=poster_did, time=time_24_hours_ago))

# Create a dictionary to store the values
data = {}

# Calculate the values and store them in the dictionary
data['uri'] = test_uri
data['likes_since'] = PostAPI.get_likes_since(uri=test_uri, time=time_24_hours_ago)
data['replies_since'] = PostAPI.get_replies_since(uri=test_uri, time=time_24_hours_ago)
data['reposts_since'] = PostAPI.get_reposts_since(uri=test_uri, time=time_24_hours_ago)
poster_did = PostAPI.get_poster(uri=test_uri)
data['follows_since'] = UserAPI.get_follows_since(subject=poster_did, time=time_24_hours_ago)

# # Write the dictionary into a text file
# with open('data.txt', 'w') as file:
#     file.write(f"uri: {test_uri}\n")
#     for key, value in data.items():
#         file.write(f"{key}: {value}\n")

# Convert the dictionary into a DataFrame
df = pd.DataFrame.from_dict(data, orient='index', columns=['Value'])

# Write the DataFrame into a CSV file
df.to_csv('data.csv', index_label='Metric')