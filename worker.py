#!/usr/bin/env python
import pika
import time
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'
if os.uname()=="Darwin":
    HTMLTOPDF = './wkhtmltopdf.mac '
else:
    HTMLTOPDF = './wkhtmltopdf '

def convert_to_pdf(fn):
        # convert to pdf using wkhtmlpdf
        os.popen(HTMLTOPDF+" static/htmls/"+fn+".html static/pdfs/"+fn+".pdf")

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    fn = body.split('.html')[0]
    cb = body.split('|')[1]
    print fn
    convert_to_pdf(fn)
    #os.popen("wget http://localhost:8000/pdfrequester/upload/download/?pdffile=http://localhost:8000/static/"+fn+".pdf")
    os.popen("wget http://localhost:8000/pdfrequester/upload/download/?pdffile="+cb+fn+".pdf")
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()




