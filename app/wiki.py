import wikipedia

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


def get_content(term):
    page = wikipedia.page(term)
    s= page.content
    return s

    