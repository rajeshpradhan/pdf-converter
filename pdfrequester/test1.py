import urllib2
content = urllib2.urlopen('http://localhost:8000/static/pdfs/f430c863-7a5c-415e-bb23-0e13fde0b49c.pdf').read()
print content
