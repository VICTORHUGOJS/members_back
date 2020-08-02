from rest_framework import viewsets
from rest_framework.response import Response
from core.api.serializer import MemberSerializer, MemberSimpleSerializer
from core.models import Member


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def list(self,request,*args,**kwargs):
        queryset = Member.objects.all() #Buscar os itens
        serializer = MemberSimpleSerializer(queryset, many=True)
        return Response(serializer.data)
