import pandas as pd
from datetime import datetime


posts = pd.read_csv('demo_csvs/demo_posts.csv')

class CategoryDAL():
    # returns the uris of all posts with this keyword
    def get_posts_with_keyword(keyword):
        return list(posts[posts['text'].str.contains(keyword, case=False)]['uri'])
    

print(CategoryDAL.get_posts_with_keyword('basketball'))