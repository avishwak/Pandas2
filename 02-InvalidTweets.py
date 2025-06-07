#Problem 2 :Invalid Tweets	(	https://leetcode.com/problems/invalid-tweets/ )

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[ tweets['content'].str.len() >15 ][['tweet_id']]
    return df