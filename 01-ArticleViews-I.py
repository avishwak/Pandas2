# Problem 1 : Article Views I	(	https://leetcode.com/problems/article-views-i/  )

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id']==views['viewer_id']]\
        .drop_duplicates(subset=['author_id'])\
        .sort_values(by=['author_id'])\
        .rename(columns={'author_id':'id'})[['id']]
    return df

#May be a bit faster on large datasets since it avoids creating a NumPy array

def article_views(views: pd.DataFrame) -> pd.DataFrame:

    df = views[views['author_id']==views['viewer_id']]
    df = df['author_id'].unique()
    df = pd.DataFrame(df, columns=['id'])
    return df.sort_values(by=['id'])