from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Return a list of APIView features"""
        an_apiview=[
            'uses HTTP method as function (get, post, patch and delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})
# Create your views here.
