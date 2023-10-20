import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    # make new exam df witth aggregate count of attended exams for each student
    exam_df = examinations.reset_index().groupby(['student_id', 'subject_name']).count().reset_index()

    # merge students with subjects using cross join, then left join resultant df with our exam df to get count where applicable
    df = students.merge(subjects, how='cross').merge(exam_df, on=['student_id', 'subject_name'], how='left')

    # reformatting of col names, replacing nan's and converting float to int
    df.columns = ['student_id', 'student_name', 'subject_name', 'attended_exams']
    df['attended_exams'].fillna(0, inplace = True)
    df['attended_exams'] = df['attended_exams'].astype('int32')
    
    return df.sort_values(['student_id', 'subject_name'])