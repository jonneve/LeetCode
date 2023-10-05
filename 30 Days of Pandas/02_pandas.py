import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:

    # define filter mask
    mask = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')

    # return only product id where mask applies, use [[]] to ensure df is retruend and not a series
    return products[mask][['product_id']]