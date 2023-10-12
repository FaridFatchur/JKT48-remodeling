from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Member
from .serializer import MemberSerializer

def home(request):
    return render(request, 'jkt48/home.html')

def members(request):
    allmem = Member.objects.all()
    context = {
        'allmem':allmem,
    }
    return render(request, 'jkt48/members.html', context)

#Create & Display Member
class MemberListCreate(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer