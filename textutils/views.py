from django.http import  HttpResponse
from django.shortcuts import render
    

def index(request):
   return render(request, 'index.html')

def home(request):
   return render(request, 'index.html')

def aboutus(request):
   return render(request, 'aboutus.html')

def contact(request):
   return render(request, 'contactus.html')




def analyze(request):
    djtext = request.POST.get('text', 'default')         
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    if (extraspaceremover=="on" or newlineremover=="on" or removepunc=="on" or fullcaps=="on"):
        flag=False
        my_string=""
        
        if extraspaceremover=="on" and flag==False:
            analyzed=""
            for index, char in enumerate(djtext):
                if not(djtext[index] == " " and djtext[index+1]==" "):
                    analyzed = analyzed + char
            flag=True 
            my_string+=" -Extra_Space_Removed- "

        elif extraspaceremover=="on" and flag==True:
            temp=analyzed
            analyzed=""
            for index, char in enumerate(temp):
                if not(temp[index] == " " and temp[index+1]==" "):
                    analyzed = analyzed + char
            flag==True
            my_string+=" -Extra_Space_Removed- "
    

        if removepunc=="on" and flag==True :
            temp=analyzed
            analyzed=""
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            for char in temp:
                if char not in punctuations:                            
                    analyzed = analyzed + char 
            temp=""
            my_string+=" -Punctuation_Removed- " 
        elif removepunc=="on" and flag==False :
            temp=djtext
            analyzed=""
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            for char in temp:
                if char not in punctuations:                            
                    analyzed = analyzed + char 
            temp="" 
            flag=True
            my_string+=" -Punctuation_Removed- "
      

        if newlineremover=="on" and flag==True:
            temp=analyzed
            analyzed=""
            for char in temp:
                if char != "\n" and char!="\r":
                    analyzed = analyzed + char
            temp=""
            my_string+=" -Newline_Remover- "

        elif newlineremover=="on" and flag==False:
            temp=djtext
            analyzed=""
            for char in temp:
                if char != "\n" and char!="\r":
                    analyzed = analyzed + char
            temp=""
            flag=True
            my_string+=" -Newline_Remover- "
            

        if fullcaps=="on" and flag==True :
            analyzed=analyzed.upper()
            my_string+=" -Uppercase- "
        elif fullcaps=="on" and flag==False :
            analyzed=djtext.upper()
            flag=True
            my_string+=" -Uppercase- "                                  
        
            

        params = {'purpose': my_string, 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
        
    else:
        return HttpResponse("error")

   




