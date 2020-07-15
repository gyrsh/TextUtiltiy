from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Posting
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import PostingSerializer

class employeeList(APIView):
    def get(self,request):
        employee=Posting.objects.all()
        serializer=PostingSerializer(employee,many=True)
        return Response(serializer.data)
    def post(self,request):
        pass





def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


#def ex1(request):
    #sites = ['''For Entertainment youtube video''',
        #     '''For Interaction Facebook''',
       #      '''For Insight   Ted Talk''',
      #       '''For Internship   Intenship''',
     #        ]
    #return HttpResponse((sites))'''

def about(request):
    return render(request,'about.html')

def analyze(request):
    #Get the text
    uname=request.POST.get('username')
    mail=request.POST.get('mail_id')
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if(uname=='' or mail==''):
        #messages.warning(request, 'Please enter Username or Password!')
        return render(request,'sorry.html')
    #Check which checkbox is on
    poster=Posting()
    poster.username=uname
    poster.email_id=mail
    poster.save()
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'username':uname,'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'username':uname,'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'username':uname,'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char

        params = {'username':uname,'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
