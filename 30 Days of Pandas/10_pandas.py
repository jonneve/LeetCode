import pandas as pd

# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:

    # Sort table by id col so drop duplicates keeps unique emails with smallest id's
    # Operations happen in place so underlying person table is changed as nothing returned from function
    person.sort_values('id', inplace = True)
    person.drop_duplicates('email', inplace = True)