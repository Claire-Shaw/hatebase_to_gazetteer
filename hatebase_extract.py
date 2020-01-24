import config

import requests
import json
import os

def get_vocabulary(path, extract_params={}):

    auth_params = {
        'api_key': config.api_key
    }

    print('authenticating...')
    auth = requests.post('https://api.hatebase.org/4-4/authenticate', data=auth_params).json()
    token = auth['result']['token']
    print('authentication successful')

    get_vocab_params = {
        'token': token,
        **extract_params
    }

    print('retrieving page 1')
    vocab = requests.post('https://api.hatebase.org/4-4/get_vocabulary', data=get_vocab_params).json()
    number_of_pages = vocab['number_of_pages']

    #Write first page of resuls to file
    filepath = os.path.join(path, 'get_vocab_1.txt')
    with open(filepath, 'w') as f:
        json.dump(vocab, f, indent=4)

    #Read and write the rest of the pages
    for page in range(2, number_of_pages + 1):
        next_page_params = {**get_vocab_params,
                            'page': page} 
        print(f'retrieving page {page}')
        vocab = requests.post('https://api.hatebase.org/4-4/get_vocabulary', data=next_page_params).json()
        filepath = os.path.join(path, f'get_vocab_{page}.txt')
        with open(filepath, 'w') as f:
            json.dump(vocab, f, indent=4)

    print('done!')




