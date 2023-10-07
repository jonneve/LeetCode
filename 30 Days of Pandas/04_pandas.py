import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    # get author id where viewer and author id match, then create a sorted unique series of these ids 
    view_id = views[views['author_id'] == views['viewer_id']]['author_id'].sort_values().unique()
    
    # create a new dataframe based on earlier output, change formatting to meet expected requirements, retrun empty df if no matches
    ans = pd.DataFrame(view_id, columns = ['id']) if len(view_id) > 0 else pd.DataFrame({'id' : []})

    return ans