import os
import re
import string
import jinja2 as j


def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""
    result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(root) for f in filenames if os.path.splitext(f)[1] == '.txt']
    return result

def get_text(fileName):
    f = open(fileName)
    s = f.read()
    f.close()
    return s


def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)  # delete stuff but leave at least a space to avoid clumping together
    words = nopunct.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, to, at, be, ...
    words = [w.lower() for w in words]
    # print words
    return words


def results(docs, terms):
    """
    Given a list of fully-qualifed filenames, return an HTML file
    that displays the results and up to 2 lines from the file
    that have at least one of the search terms.
    Return at most 100 results.  Arg terms is a list of string terms.
    """
    length = len(docs)
    docs = docs[:100]


    #{% for t in terms %}{% if loop.last %}{{t}}{{% else %}}{{t}},{% endif %}{% endfor %}


    # HTML = """<html>
    # <body>
    # <h2>Search results for <b> {{ terms|join(', ) }}</b> in {{length}} files</h2>
    #
    # {% for d in docs %}<p><a href="file://{{d}}">{{d}}</a><br>
    # {{something}}<br><br>{% endfor %}
    #
    # </body>
    # </html>
    # """
    # return j.Environment().from_string(HTML).render(docs = docs, terms = terms, length = length)


    HTML = """<html>
    <body>
    """

    HTML += "<h2>Search results for {} in {} files</h2>".format(" ".join(terms), length)
    for doc in docs:
        HTML += "<p><a href='file://{}'>{}</a><br/></p>".format(doc, doc)
        
    HTML+= """
    </body>
    </html>
    """
    return HTML


def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]
