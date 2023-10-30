import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    # create dense rnaking column in descending order
    scores['rank'] = scores['score'].rank(method = 'dense', ascending = False)

    # return expected format df
    return scores[['score', 'rank']].sort_values('rank')