import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:

    # group by id, then get count of unique entries per col
    # return select cols with subject id renamed to cnt
    return teacher.groupby('teacher_id').nunique().reset_index()[['teacher_id', 'subject_id']].rename({'subject_id':'cnt'}, axis = 1)