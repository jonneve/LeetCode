import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    
    # group by id, aggregate by min to find first login
    # retrun seect cols with event date renamed to first login
    return activity.groupby('player_id').min().reset_index()[['player_id', 'event_date']].rename({'event_date':'first_login'}, axis =1)