import pandas as pd
from datetime import datetime
import post_DAL


posts = pd.read_csv('demo_csvs/demo_posts.csv')

class CategoryDAL():
    # returns the uris of all posts with this keyword
    def get_posts_with_keyword(keyword):
        return list(posts[posts['text'].str.contains(keyword, case=False)]['uri'])
    
    def get_likes_of_all_posts(uris):
        total_likes = 0
        for uri in uris:
            total_likes += post_DAL.PostAPI.get_all_likes(uri=uri)
        return total_likes
    
    def top_post_by_likes(uris):
        uri_likes = []
        for uri in uris:
            uri_likes.append((uri, post_DAL.PostAPI.get_all_likes(uri=uri)))
        sorted_uri_likes = sorted(uri_likes, key=lambda x: x[1], reverse=True)
        return sorted_uri_likes[0]

    
    def get_authors_of_all_posts(uris):
        authors = set()
        for uri in uris:
            authors.add(post_DAL.PostAPI.get_poster(uri=uri))
        return authors
    
    def get_authors_follower_gain_24_hours(dids):
        current_time = pd.Timestamp.now(tz='UTC')
        current_time = current_time.tz_convert('UTC')  
        time_24_hours_ago = current_time - pd.Timedelta(hours=24)
        follower_gain = 0
        for did in dids:
            follower_gain += post_DAL.UserAPI.get_follows_since(subject=did, time=time_24_hours_ago)
        return follower_gain
    

# print('keyword: \'basketball\'')
# print('post uris', CategoryDAL.get_posts_with_keyword('basketball'))
# all_post_uris = CategoryDAL.get_posts_with_keyword('basketball')
# print('num posts', len(all_post_uris))
# print('total likes of all posts all time', CategoryDAL.get_likes_of_all_posts(all_post_uris))
# author_dids = CategoryDAL.get_authors_of_all_posts(all_post_uris)
# print('num authors talking about this', len(author_dids))
# print('num followers gained by these authors in 24 hours', CategoryDAL.get_authors_follower_gain_24_hours(dids=author_dids))

import json

# Calculate the values
keyword = 'basketball'
post_uris = CategoryDAL.get_posts_with_keyword(keyword)
num_posts = len(post_uris)
total_likes = CategoryDAL.get_likes_of_all_posts(post_uris)
author_dids = CategoryDAL.get_authors_of_all_posts(post_uris)
num_authors = len(author_dids)
follower_gain_24_hours = CategoryDAL.get_authors_follower_gain_24_hours(dids=author_dids)
top_post_uri = CategoryDAL.top_post_by_likes(uris=post_uris)[0]
top_post_text = post_DAL.PostAPI.get_text(top_post_uri)

# Create a dictionary to store the values
data = {
    'Keyword': keyword,
    'Post URIs': post_uris,
    'Num Posts': num_posts,
    'Total Likes': total_likes,
    'Num Authors': num_authors,
    'Follower Gain (24 hours)': follower_gain_24_hours,
    'Top Post URI': top_post_uri,
    'Top Post Text': top_post_text
}

# Write the dictionary into a JSON file
with open('category_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
