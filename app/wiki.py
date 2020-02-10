import wikipedia
from wikipedia import DisambiguationError
import re
'''

The code that caused this warning is on line 389 of the file 
/home/ray/ms3/venv/lib/python3.7/site-packages/wikipedia/wikipedia.py. 
To get rid of this warning, pass the additional argument 
'features="html.parser"' to the BeautifulSoup constructor.

  lis = BeautifulSoup(html).find_all('li')
Traceback (most recent call last):
'''


'''
headings look like
 === GitHub Enterprise ===
 '''

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

'''
/home/ray/microblog/venv/lib/python3.7/site-packages/wikipedia/wikipedia.py:389: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser")
This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
The code that caused this warning is on line 389 of the file /home/ray/microblog/venv/lib/python3.7/site-packages/wikipedia/wikipedia.py. 
To get rid of this warning, pass the additional argument 'features="html.parser"' to the BeautifulSoup constructor.
'''