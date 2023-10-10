import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    # apply lambda func to create a new col showing tweet char length
    tweets['tweet_length'] = tweets['content'].apply(lambda x: len(x))

    # create a filtered df containing invalid tweets
    ans = tweets[tweets['tweet_length'] > 15][['tweet_id']]
    
    return ans
