import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:

    # melt df grouping around the product id field, col name will be store, value will be price
    # then filter with mask ensuring new price col is not na
    return products.melt(id_vars=['product_id'], var_name='store', value_name='price')[products.melt(id_vars=['product_id'], var_name='store', value_name='price')['price'].notna()]