import urllib3
## Given a url, try to retrieve it. If it's text/html,
## print its base url and its text.
def wget(url):
    print(url)
    ufile = urllib.urlopen(url)  ## get file-like object for url
    info = ufile.info()   ## meta-info about the url content
    if info.gettype() == 'text/html':
        print 'base url:' + ufile.geturl()
        text = ufile.read()  ## read all its text
        print text

wget('www.google.ca')