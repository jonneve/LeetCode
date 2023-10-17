import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    
    # group df by count of student in class
    df = courses.groupby('class').count().reset_index()

    # return selected col if 5 of more students in class
    return df[df['student'] >= 5][['class']]