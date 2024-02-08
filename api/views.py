# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from restaurant.models import Menu
from .serializers import s1

@api_view(['GET'])
def handler(request):
    if request.method == 'GET':
        all_objs = Menu.objects.all()
        s= s1(all_objs,many=True)
        return Response(s.data)
    
@api_view(['GET'])
def slk(request, pk):
    if request.method == 'GET':
        all_objs = Menu.objects.get(pk=pk)
        ss= s1(all_objs)
        return Response(ss.data)