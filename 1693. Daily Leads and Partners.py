import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    mydictionary = {}
    for i in range(len(daily_sales)):
        d_id = daily_sales['date_id'][i]
        m_name = daily_sales['make_name'][i]
        l_id  = daily_sales['lead_id'][i]
        p_id = daily_sales['partner_id'][i]
        if (d_id,m_name) not in mydictionary:
            mydictionary[(d_id,m_name)] = [set(),set()]
        mydictionary[(d_id,m_name)][0].add(l_id)
        mydictionary[(d_id,m_name)][1].add(p_id)
    

    result = []
    for key,value in mydictionary.items():
        result.append([key[0],key[1],len(value[0]),len(value[1])])
    return pd.DataFrame(result,columns = ['date_id','make_name','unique_leads','unique_partners'])
    

    