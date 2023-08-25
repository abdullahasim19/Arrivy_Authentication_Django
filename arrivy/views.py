from google.cloud import ndb
from django.http import HttpResponse
import os
from signups.ndbModels.ndbEntity import Entity
from signups.ndbModels.ndbUser import User
from signups.ndbModels.ndbCompanyProfile import CompanyProfile
from signups.ndbModels.ndbEntityProfile import EntityProfile
from signups.ndbModels.ndbUserProfile import UserProfile

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"


def fun2(request):
    class Book(ndb.Model):
        title = ndb.StringProperty()

    client = ndb.Client()
    with client.context():
        pp = User.query().fetch()
        for p in pp:
            k = ndb.Key('User', p._key.id())
            k.delete()

        # new_book=Book(title='Harry Potter 3')
        # new_book.put()
        # print(new_book.title)
        #
        # books=Book.query().fetch()
        # print(books)
        # print(books[0]._key.id())
        # t=Book.query(Book.title=='Harry Potter 2').get()
        # print(t.title)
    return HttpResponse('Hello')

def home(request):
    return HttpResponse('HELLO')

# pp = Entity.query().fetch()
# print(pp[0]._key.id())
# k = ndb.Key('Entity', pp[0]._key.id())
# k.delete()
