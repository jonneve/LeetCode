import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    # retrun unspecified ordered df using prefix string as mask filter, \b is word boundary so returns false if prefix is a not start of word
    return patients[patients['conditions'].str.contains(r'\bDIAB1\w*')]