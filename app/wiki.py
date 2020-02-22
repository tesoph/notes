import wikipedia
from wikipedia import DisambiguationError
import re
import requests


#ny = wikipedia.page("New York")
#g = wikipedia.page("GitHub")
#s = wikipedia.summary('Github')
#s= g.content

#https://www.programcreek.com/python/example/93332/wikipedia.DisambiguationError
'''
def get_wiki_page(search_string, summary=False, content=False):
    #Returns results from searching for search_string with wikipedia wrapper library. 
       Note: Makes a web request
    try:
        page = wikipedia.page(search_string)
        page_data = {"url":page.url,
                     "title":page.title}
        if content:
            page_data["content"] = page.content # Full text content of page.
        if summary:
            page_data["summary"] = page.summary # Summary section only.
    
    except DisambiguationError as e:
        return get_wiki_page(e.options[0]) #naively choose first option
    except Exception as e:
        return None
    
    return page_data '''


#https://stackabuse.com/getting-started-with-pythons-wikipedia-api/
'''
td*
display list of results to choose from instead of picking the first result
'''
def get_content(term):
    try:
        page = wikipedia.page(term)
        s= page.content
    except DisambiguationError as e:
        #listOfOptions= get_content(e.options)
        #return listOfOptions
        return get_content(e.options[0])
    except Exception as e:
        return None
    #return s
    return clean(s)

#!/usr/bin/python3

"""
    parse.py

    MediaWiki API Demos
    Demo of `Parse` module: Parse content of a page

    MIT License
"""




def get_title(url_):
    S = requests.Session()

    PARAMS = {
         "action": "parse",
         "format": "json"
    }
    url=url_
    response = S.get(url=url, params=PARAMS)
    data= response.json()
    return data
'''
def clean(text):
    l = []
    print('cleaning')
    text.split('===')
    l=text.split('==')
    return l
'''
def clean(text):
    l= re.split('===|==', text)
    return l