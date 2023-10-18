import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    
    # make new df after grouping by actor and director id, aggregate by count of primary key ids (timestamp)
    df = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].count().reset_index()

    # return selected cols if count is 3 or more 
    return df[df['timestamp'] >= 3][['actor_id', 'director_id']]