import pandas as pd

from common import (
    determine_category,
    determine_scope
)
from categories_examples import category_words
from scopes_example import scope_part_numbers

READ_EXCEL = 'Products File.xlsx'
OUTPUT_EXCEL = 'Products File With Categories and Scopes.xlsx'

def run():
    df = pd.read_excel(READ_EXCEL)
    
    categories = category_words

    df['New Category'] = df.apply(lambda row: determine_category(row['PO Line Description'], 
                                                                categories), axis=1)
    
    in_scope = scope_part_numbers

    df['In Scope/Out of Scope'] = df.apply(lambda row: determine_scope(row['PO Source Part Number'], 
                                                                in_scope), axis=1)
    
    df.to_excel(OUTPUT_EXCEL, index=False, engine='openpyxl')

    print(f"Processing completed. Check the file {OUTPUT_EXCEL}.")

if __name__ == '__main__':
    run()

