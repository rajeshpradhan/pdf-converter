# Create your views here.
import os
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
import uuid



@csrf_exempt
def index(request):

	try:
		# save to disk	
		f = request.FILES['htmlfile']

		# generate unique id for filename
		fn = str(uuid.uuid4())
    		with open('static/htmls/'+fn+'.html', 'w+') as destination:
        		for chunk in f.chunks():
            			destination.write(chunk)
	except:
		return HttpResponse('File not found')

        # convert to pdf using wkhtmlpdf
	os.popen("./wkhtmltopdf static/htmls/"+fn+".html static/pdfs/"+fn+".pdf")

	# read the pdf file
	with open('static/pdfs/'+fn+'.pdf', "rb") as fp:
		pdf = fp.read()

	#os.remove('static/pdfs/'+fn+'.pdf')
	#os.remove('static/htmls/'+fn+'.html')	
	return HttpResponse(pdf, mimetype='Application/pdf')

