from google.cloud import ndb
from django.http import HttpResponse
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="credentials.json"
def fun2(request):
    class Book(ndb.Model):
        title = ndb.StringProperty()

    client = ndb.Client()
    with client.context():
        # new_book=Book(title='Harry Potter')
        # new_book.put()
        books=Book.query().fetch()
        print(books)
        print(books[0]._key.id())
    return HttpResponse(books[0].title)