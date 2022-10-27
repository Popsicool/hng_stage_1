from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    me = {"slackUsername": "Popsicool","backend":True, "age":27, "bio": "I'm a fullstack developer in developments stage, i'm passionate about learning and willing to do hard things" }
    return Response(me)