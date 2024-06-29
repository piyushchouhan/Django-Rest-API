from rest_framework.response import Response
from rest_framework.decorators import api_view  
from base.models import Items
from .serializers import ItemsSerializer 

@api_view(['GET'])
def getData(request):
    items = Items.objects.all()
    serializer = ItemsSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = ItemsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

