# Create your views here.
import os
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
import uuid
from threading import Thread



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
	

	t1 = Thread(target=convert_to_pdf, args=(fn,))
	t1.start()
	#os.remove('static/pdfs/'+fn+'.pdf')
	#os.remove('static/htmls/'+fn+'.html')	
	#return HttpResponse(pdf, mimetype='Application/pdf')
	# return the filename for later retrieval
	return HttpResponse('http://localhost:8000/static/'+fn+".pdf")


def convert_to_pdf(fn):

        # convert to pdf using wkhtmlpdf
	os.popen("./wkhtmltopdf static/htmls/"+fn+".html static/pdfs/"+fn+".pdf")


def get_url(pathname):

    import urllib  
      
    return urllib.pathname2url(pathname)  


@csrf_exempt
def upload(request):
	try:
		# save to disk	
		f = request.FILES['htmlfile']
		cb = request.POST['callbackurl']

		# generate unique id for filename
		fn = str(uuid.uuid4())
    		with open('static/htmls/'+fn+'.html', 'w+') as destination:
        		for chunk in f.chunks():
            			destination.write(chunk)
		#new_task(fn+'.html')
		new_task(fn+'.html'+"|"+cb)
	except:
		return HttpResponse('File not found')

	return HttpResponse('http://localhost:8000/static/'+fn+".pdf")


import pika
import sys

def new_task(task):


	connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
	channel = connection.channel()

	channel.queue_declare(queue='task_queue', durable=True)

	message =  task
	
	channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
	#print " [x] Sent %r" % (message,)
	connection.close()





