import numpy as np
import pandas as pd
import requests
import json
import re
import argparse


def access_guardian(api_key,comment_ids,API_ENDPOINT):
    
    responses=[]
    for idx,comment_id in enumerate(comment_ids):
        
        get_call=f'comment/{comment_id}'
        api_call = {'api-key': api_key}
        #print(get_call)
        response=requests.get(f'{API_ENDPOINT}{get_call}', api_call)
        
        #print(response.json())
        if response.json()['status']!='ok':
            if response.json()['statusCode']==429:
                print(f'Limit exceeded, stopped at idx: {idx}, comment_id:{comment_id}')
                break
                
            else:
                print(f'Error at {comment_id}, idx: {idx}, status: {response.json()["statusCode"]}')
                
        else:
            responses.append(response)
            
        #if(idx==0):
            #break
    
    return responses

def extract_data_from_responses(responses,old_df):
    comment_id_dict={}
    
    if old_df is not None:
        old_df=old_df.fillna('')
        for idx, row in old_df.iterrows():
            comment_id_dict[row['comment_id']]=(str(row['comment_id']),
                                                str(row['article_id']),
                                                str(row['author_id']),
                                                str(row['comment_text']),
                                                str(row['timestamp']),
                                                str(row['parent_comment_id']),
                                                str(row['upvotes']),
                                                str(row['responses']),
                                                str(row['child_comment_id']))

    regex='[\<].*?[\>]'
    for response in responses:
        json_resp=response.json()
        comment_id=str(json_resp['comment']['id'])
        article_id=str(json_resp['comment']['discussion']['webUrl'])
        author_id=str(json_resp['comment']['userProfile']['userId'])
        comment_text=re.sub(regex, '', json_resp['comment']['body'])
        timestamp=str(json_resp['comment']['isoDateTime'])
        
        if 'responseTo' in json_resp['comment'].keys():
            parent_comment_id=str(json_resp['comment']['responseTo']['commentId'])
        else:
            parent_comment_id=''
        
        upvotes=json_resp['comment']['numRecommends']
        number_of_responses=str(json_resp['comment']['numResponses'])
        child_comment_id=''
            
        comment_id_dict[comment_id]=(comment_id,article_id,author_id,comment_text,timestamp,parent_comment_id,upvotes,number_of_responses,child_comment_id)

    return list(comment_id_dict.values())

def last_id_from(df):
    return df.comment_id[len(df)-1]


def to_dataframe(records):
    df=pd.DataFrame.from_records(records,columns=['comment_id',
                                                  'article_id',
                                                  'author_id',
                                                  'comment_text',
                                                  'timestamp',
                                                  'parent_comment_id',
                                                  'upvotes',
                                                  'responses',
                                                  'child_comment_id'])
    
    return df

def compute_children(df):
    
    parent_dict={}
    for idx, row in df.iterrows():
        if row['parent_comment_id']!='':
            old_val=parent_dict.get(row['parent_comment_id'])
            if old_val is None:
                parent_dict[row['parent_comment_id']]=row['comment_id']
            else:
                parent_dict[row['parent_comment_id']]=old_val+';'+row['comment_id']
                
    
    for key in parent_dict.keys():
        df.loc[df.loc[df['comment_id'] == key].index, 'child_comment_id'] = parent_dict[key]
    return df

def get_comment_ids(file_path):
    comment_ids=np.array(pd.read_csv(file_path,usecols =['comment_id']))
    
    return comment_ids.flatten()

def run(api_key,comment_ids,API_ENDPOINT,file_path):
    
    
    comment_ids =list(map(str, comment_ids))
        
    try:
        old_df=pd.read_csv(file_path,dtype={'comment_id': str,
                                            'article_id':str,
                                            'author_id':str,
                                            'comment_text':str,
                                            'timestamp':str,
                                            'parent_comment_id':str,
                                            'upvotes':str,
                                            'responses':str,
                                            'child_comment_id':str})
        last_id=last_id_from(old_df)
        last_idx=comment_ids.index(str(last_id))+1
        comment_ids=comment_ids[last_idx:]
    except FileNotFoundError:
        old_df=None
        
        
    responses=access_guardian(api_key,comment_ids,API_ENDPOINT)
    records=extract_data_from_responses(responses,old_df)
    df=to_dataframe(records)
    df=compute_children(df)
    df.to_csv(file_path,index=False)
    return df

parser = argparse.ArgumentParser(description='Calls the Guardian API to get comment data from a list of comment IDs.')
parser.add_argument('--output', default='result.csv', type=str, help='Filepath of outputfile')
parser.add_argument('--apikey', type=str, help='The Guardian API Key')
parser.add_argument('--source', type=str, help='CSV-Source-File with comment IDs in column "comment_id"')
args = parser.parse_args()


if args.apikey==None:
    args.apikey=''#your_key
    
if args.source==None:
    args.source=''#default loading file

API_ENDPOINT = 'http://discussion.theguardian.com/discussion-api/'

df=run(args.apikey,get_comment_ids(args.source)[:10],API_ENDPOINT,args.output)
