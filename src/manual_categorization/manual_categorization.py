import pandas as pd

from common import (
    determine_category
)
from categories_examples import category_words

READ_EXCEL = 'Products File.xlsx'
OUTPUT_EXCEL = 'Products File With Categories.xlsx'

def run():
    df = pd.read_excel(READ_EXCEL)
    
    categories = category_words

    df['New Category'] = df.apply(lambda row: determine_category(row['PO Line Description'], 
                                                                categories), axis=1)
    
    df.to_excel(OUTPUT_EXCEL, index=False, engine='openpyxl')

    print(f"Processing completed. Check the file {OUTPUT_EXCEL}.")

if __name__ == '__main__':
    run()

