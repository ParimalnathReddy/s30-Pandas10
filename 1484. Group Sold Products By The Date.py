import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # dictionary = {}
    # for i in range(len(activities)):
    #     sell_d = activities['sell_date'][i]
    #     prod = activities['product'][i]
    #     if sell_d not in dictionary:
    #         dictionary[sell_d] = set()
    #     dictionary[sell_d].add(prod)
    # result = []
    # for key,value in dictionary.items():
    #     temp = []
    #     for product in value:
    #         temp.append(product)
    #     temp.sort()
    #     s = ""
    #     for i in range(len(temp)):
    #         s = s + temp[i]
    #         if i != len(temp) - 1:
    #             s = s+ ','

    #     result.append([key,len(value),s])
    # df = pd.DataFrame(result,columns = ['sell_date','num_sold','products'])
    # df.sort_values(by = ['sell_date'], inplace = True)  
    # return df       

    groups = activities.groupby(['sell_date'])
    result = groups.agg(
        num_sold=('product', 'nunique'),
        products=('product', lambda x: ','.join(sorted(set(x))))
    ).reset_index()
    
    result.sort_values(by=['sell_date'], inplace=True)
    return result