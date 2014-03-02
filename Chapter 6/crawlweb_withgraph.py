#!/usr/bin/python

# Modify the crawl_web procedure so that instead of just returning the 
# index, it returns an index and a graph. The graph should be a 
# Dictionary where the key:value entries are:

#  url: [list of pages url links to] 


def crawl_web(seed): # returns index, graph of outlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>:[list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()	# Retrieves last page in list to initiate crawling process. 
        if page not in crawled:	# Only crawls the page if it hasn't been crawled before. 
            content = get_page(page) # Obtains sample web results from cache below. 
            add_page_to_index(index, page, content)	# Adds all words to index with page as the key and all words on the page as the value. 
            outlinks = get_all_links(content)	# Grabs all links on target page. 
            # New line of code in this block
            graph[page] = outlinks 		# Adds the page as a key with all links from get_all_links as the value.
            union(tocrawl, outlinks)	# Adds next level of links to tocrawl.
            crawled.append(page)		# Appends current page to crawled list. 
    return index, graph


cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipies:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbonzo beans.
<li> Crush them in a blender.
<li> Add 3 tablesppons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>




""", 
}

def get_page(url):
    if url in cache:			# Note: this function is a quick and dirty method for obtaining
        return cache[url]		# sample web results. 
    else:
        return None
    
def get_next_target(page):					# Basic function to retrieve next link on page. 
    start_link = page.find('<a href=')		# Uses html tag to find link. 
    if start_link == -1: 					# Returns None, 0 if there are no links on the page. 
        return None, 0
    start_quote = page.find('"', start_link)	# Looks for quotations followed by html tag. 
    end_quote = page.find('"', start_quote + 1) # Finds end of html tag. 
    url = page[start_quote + 1:end_quote]		# Uses start and end of html tag to derive link. 
    return url, end_quote						# Returns the link (url) and the position after in order 
    											# to continue the search. 


def get_all_links(page):						# Runs get_next_target on the whole page
    links = []									# until it has appended every link to a list. 
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):				# Combines two lists together, leaving out any identical values or strings. 
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):		# Searches through every word on a webpage
    words = content.split()						# and uses the function below to create a list 
    for word in words:							# with keywords and the webpages that contain them. 
        add_to_index(index, word, url)			
        
def add_to_index(index, keyword, url):			# Creates a list of lists for each keyword as follows:
    if keyword in index:						# [[<keyword>, [url1, url2, url3]], [<keyword2>, [url1, url2]]] and so on. 
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):						# Loops through lists and returns position of keyword
    if keyword in index:						# if found, None if not. 
        return index[keyword]
    else:
        return None



index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html') 

if 'http://udacity.com/cs101x/urank/index.html' in graph:
    print graph['http://udacity.com/cs101x/urank/index.html']
#>>> ['http://udacity.com/cs101x/urank/hummus.html',
#'http://udacity.com/cs101x/urank/arsenic.html',
#'http://udacity.com/cs101x/urank/kathleen.html',
#'http://udacity.com/cs101x/urank/nickel.html',
#'http://udacity.com/cs101x/urank/zinc.html']



