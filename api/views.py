from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def demo_endpoint(request):
    return Response({
        "id": 1,
        "title": "Demo",
        "message": "API is working!"
    })