['ASCII_SPACES', 'DEFAULT_BUILDER_FEATURES', 
'NO_PARSER_SPECIFIED_WARNING', 'ROOT_TAG_NAME',
 '__bool__', '__call__', '__class__', '__contains__', 
 '__copy__', '__delattr__', '__delitem__', '__dict__', 
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
 '__getattr__', '__getattribute__', '__getitem__', '__getstate__',
  '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
  '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', 
  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
  '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
  '__unicode__', '__weakref__', '_all_strings', '_check_markup_is_url',
   '_feed', '_find_all', '_find_one', '_is_xml', '_lastRecursiveChild',
    '_last_descendant', '_linkage_fixer', '_most_recent_element', 
    '_namespaces', '_popToTag', '_should_pretty_print', 'append', 
    'attrs', 'builder', 'can_be_empty_element', 'cdata_list_attributes',
     'childGenerator', 'children', 'clear', 
     'contains_replacement_characters', 'contents', 'currentTag',
      'current_data', 'declared_html_encoding', 'decode', 
      'decode_contents', 'decompose', 'descendants', 'element_classes',
       'encode', 'encode_contents', 'endData', 'extend', 'extract', 
       'fetchNextSiblings', 'fetchParents', 'fetchPrevious', 
       'fetchPreviousSiblings', 'find', 'findAll', 'findAllNext',
        'findAllPrevious', 'findChild', 'findChildren', 'findNext', 
        'findNextSibling', 'findNextSiblings', 'findParent', 
        'findParents', 'findPrevious', 'findPreviousSibling', 
        'findPreviousSiblings', 'find_all', 'find_all_next',
         'find_all_previous', 'find_next', 'find_next_sibling',
          'find_next_siblings', 'find_parent', 'find_parents',
           'find_previous', 'find_previous_sibling',
            'find_previous_siblings', 'format_string',
             'formatter_for_name', 'get', 'getText',
              'get_attribute_list', 'get_text', 'handle_data', 
              'handle_endtag', 'handle_starttag', 'has_attr', 
              'has_key', 'hidden', 'index', 'insert', 'insert_after', 
              'insert_before', 'isSelfClosing', 'is_empty_element', 'is_xml', 'known_xml', 'markup', 'name', 'namespace', 'new_string', 'new_tag', 'next', 'nextGenerator', 'nextSibling', 'nextSiblingGenerator', 'next_element', 'next_elements', 'next_sibling', 'next_siblings', 'object_was_parsed', 'original_encoding', 'parent', 'parentGenerator', 'parents', 'parse_only', 'parserClass', 'parser_class', 'popTag', 'prefix', 'preserve_whitespace_tag_stack', 'preserve_whitespace_tags', 
              'prettify', 'previous', 'previousGenerator', 'previousSibling', 'previousSiblingGenerator', 'previous_element', 'previous_elements', 'previous_sibling', 'previous_siblings', 'pushTag', 'recursiveChildGenerator', 'renderContents', 'replaceWith', 'replaceWithChildren', 'replace_with', 'replace_with_children', 'reset', 'select', 'select_one', 'setup', 'smooth', 'string', 'strings',
 'stripped_strings', 'tagStack', 'text', 'unwrap', 'wrap']


import requests                # Include HTTP Requests module
from bs4 import BeautifulSoup  # Include BS web scraping module
url = "https://americasbiz.net/bid_opportunities/2019/11/15/state/46/" # Website / URL we will contact
r = requests.get(url)           # Sends HTTP GET Request
print(r.status_code)            # ---> Print HTML status code <---
soup = BeautifulSoup(r.text, "html.parser") # Parses HTTP Response
#print(soup.prettify())          # Prints user-friendly results

# returns the first div on the page
soup.find('div')

# find the first div with id='welcome_message'
##soup.find('table', class='partialSolicDisplay')
mydivs = soup.findAll("table", {"class": "partialSolicDisplay"})
print(mydivs)
# finds the respective HTML tag element
soup.title
soup.h1
soup.body.div

soup.find_all('a')      # finds all <a> elements
soup.find_all('a')[0]   # reference the first <a> element
soup.find_all('a')[1]   # reference the second <a> element

stickers_btn=soup.find('div',id='stickers_btn')
print(stickers_btn.get_text())
##print(stickers_btn)
##for link in soup.find_all('a'):
##   print(link.get_text())
for link in soup.find_all('a'):
    print(link.get('href'))


##print(soup.prettify())          # Prints user-friendly results
##partialSolicDisplay = soup.findAll("table", {"class": "partialSolicDisplay"})
##print(partialSolicDisplay.get_text())
##table_info_list = soup.find_all("tr", {"class": "row2"})
##for table_info in table_info_list:
   ## print (table_info)
   ## print(table_info.find_all('td'))
    ##print(soup.find_all('a'))
    ##print(soup.find_all('a').get('href'))
   
