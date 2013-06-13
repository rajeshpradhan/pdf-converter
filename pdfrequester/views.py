# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

import urllib2
import urlparse
import os

def index(request):
	return render(request, 'pdfrequester/index.html')

def upload(request):
	return render(request, 'pdfrequester/upload.html')


def download(request):
    # Get the url
    url = request.GET['pdffile']

    # Extract filename from the url
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

    # open url for reading
    f = urllib2.urlopen(urllib2.Request(url))
    try:
	# Get the filename
        fileName = getFileName(url,f)

	# Save to disk
        with open(fileName, 'wb+') as destination:
		destination.write(f.read())

    finally:
	# close file
        f.close()

    return HttpResponse('done')

