from google.cloud import ndb
from django.http import HttpResponse, JsonResponse
import os
from signups.ndbModels.ndbEntity import Entity
from signups.ndbModels.ndbUser import User
from signups.ndbModels.ndbCompanyProfile import CompanyProfile
from signups.ndbModels.ndbEntityProfile import EntityProfile
from signups.ndbModels.ndbUserProfile import UserProfile
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .auth import generate_access_token, generate_refresh_token
from rest_framework.permissions import AllowAny

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


# @api_view(['GET'])
def home(request):
    return HttpResponse('HELLO WORLD')
    # client = ndb.Client()
    # with client.context():
    #     currentUser = User.query(User.email == 'a@arrivy.com').get()
    #     if not currentUser:
    #         return HttpResponse('Error')
    #     return HttpResponse('FOUND')
    # return HttpResponse('HELLO')


@api_view(['GET'])
@permission_classes([AllowAny])
def generate(request):
    client = ndb.Client()
    with client.context():
        user = User.query(User.email == 'a@arrivy.com').get()

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    res = Response()
    res.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    res.data = {
        'access_token': access_token,
        'user': user.email,
    }
    return res
    # return JsonResponse({'email':currentUser.email})


@api_view(['GET'])
def protecteds(request):
    print(request.user.email)
    return HttpResponse('HELLo')

# pp = Entity.query().fetch()
# print(pp[0]._key.id())
# k = ndb.Key('Entity', pp[0]._key.id())
# k.delete()
