

import urllib2
import urlparse
import os

def download():
    url = 'http://localhost:8000/static/pdfs/f430c863-7a5c-415e-bb23-0e13fde0b49c.pdf'
    def getFileName(url,openUrl):
        if 'Content-Disposition' in openUrl.info():
            # If the response has Content-Disposition, try to get filename from it
            cd = dict(map(
                lambda x: x.strip().split('=') if '=' in x else (x.strip(),''),
                openUrl.info()['Content-Disposition'].split(';')))
            if 'filename' in cd:
                filename = cd['filename'].strip("\"'")
                if filename: return filename
        # if no filename was found above, parse it out of the final URL.
        return os.path.basename(urlparse.urlsplit(openUrl.url)[2])

    f = urllib2.urlopen(urllib2.Request(url))
    try:
        fileName = fileName or getFileName(url,f)
        print filename
        with open(fileName, 'wb+') as destination:
                for chunk in f.chunks():
                        destination.write(chunk)

    finally:
        r.close()
    return HttpResponse('done')

download()
