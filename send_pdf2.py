import urllib2

data = {'name': 'pdffile',
        'file':  open('test.pdf')
       }
edata = urllib2.urlencode(data)
urllib2.urlopen('http://localhost:8000/', edata)

