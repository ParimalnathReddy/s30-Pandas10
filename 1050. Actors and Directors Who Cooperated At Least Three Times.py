import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # mydictionary = {}
    # for i in range(len(actor_director)):
    #     a_id = actor_director['actor_id'][i]
    #     d_id = actor_director['director_id'][i]
    #     if (a_id,d_id) not in mydictionary:
    #         mydictionary[(a_id, d_id)] = 0
    #     mydictionary[(a_id,d_id)] +=1
    # result = []
    # for key,value in mydictionary.items():
    #     if value >= 3:
    #         result.append(key)
    # return pd.DataFrame(result,columns = ['actor_id','director_id'])
    group = actor_director.groupby(['actor_id','director_id']).size().reset_index(name= 'count')
    df = group[group['count']>=3]
    return df[['actor_id','director_id']]






    