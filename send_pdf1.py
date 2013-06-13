from google.appengine.api import urlfetch
from poster.encode import multipart_encode
payload = {}
payload['test.pdf'] = self.request.POST['test.pdf']
to_post = multipart_encode(payload)
send_url = "http://127.0.0.1:8000/"
result = urlfetch.fetch(url=send_url, payload="".join(to_post[0]), method=urlfetch.POST, headers=to_post[1])
