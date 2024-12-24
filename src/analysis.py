import pandas
import argparse
import os
from datetime import datetime

def clean_price(val):
    if '$' in val:
        return float(val[1:])
    else:
        if val=='':
            return 0
    return float(val)
        
def clean_stock(val):
    if val == 'out of stock' or val == '':
        return 0
    return int(val)

def clean_category(val):
    if val!='':
        return val.lower()
    return ''

def clean_exp_date(val):
    if val != '':
        format = '%Y-%m-%d' if '-' in val else '%m/%d/%Y'
        date_obj = datetime.strptime(val,format)
        return date_obj.strftime('%Y-%m-%d')

def main(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError('File not found')
        with open(file_path,'r') as file:
            columns = []
            products = []
            for i,v in enumerate(file.readlines()):
                if i == 0:
                    columns = v.strip().split()
                else:
                    item_info = v.strip().split(',')
                    products.append({
                        'product_name':item_info[0],
                        'our_price':clean_price(item_info[1]),
                        'category':clean_category(item_info[2]),
                        'current_stock':clean_stock(item_info[3]),
                        'restock_threshold':clean_stock(item_info[4]),
                        'last_update':clean_exp_date(item_info[5]),
                    })
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(type(e).__name__)
    else:
        df = pandas.DataFrame(products)
        
        #Analysis
        low_stock = df[df['current_stock'] <= df['restock_threshold']]
        out_stock = df[df['current_stock'] == 0]
        recent_updates = df[df['last_update'] > '2024-11-15']
        price_analysis = df['our_price'].describe()
        products_no_price = df[df['our_price'] == 0]
        
        with open('../report.md', 'w') as file: 
            file.write("Inventory report\n\n") 
            file.write("# Low stock products\n") 
            file.write(str(low_stock)) 
            file.write("\n\n") 
            file.write("# Productos without stock\n") 
            file.write(str(out_stock)) 
            file.write("\n\n") 
            file.write("# latest updates\n") 
            file.write(str(recent_updates)) 
            file.write("\n\n")
            file.write("# Price anaylsis\n") 
            file.write(str(price_analysis)) 
            file.write("\n\n") 
            file.write("# Free products?\n") 
            file.write(str(products_no_price)) 
            file.write("\n")
    
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='script2run') 
    parser.add_argument('file_path', type=str, help='Path to CSV file') 
    args = parser.parse_args() 
    main(args.file_path)


