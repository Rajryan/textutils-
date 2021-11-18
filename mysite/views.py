from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return render(request,'index.html')

def analyze(request):
  djtext=request.GET.get('text','default')
  removepunc=request.GET.get('removepunc','off')
  capstext=request.GET.get('capstext','off')
  extraspaceremover=request.GET.get('extraspaceremover','off')
  newlineremover=request.GET.get('newlineremover','off')
  purpose1=''
  
  # remove punctuations marks
  if removepunc=='on':
    analyzed_text=""
    punctuations='''!;:'"?&$#@*\✓™®©%£¢€¥^°~`|•√π÷×¶∆-_,.[]{}()+~'''
    for char in djtext:
      if char not in punctuations:
        analyzed_text+=char
    params={'purpose':'Removed punctuations','analyzed':analyzed_text}
    djtext=analyzed_text
    purpose1+=params['purpose']+"|"
    
    
    
  
  if capstext=='on':
  #capitalaze the text
    analyzed_text=""
    
    analyzed_text+=djtext.upper()
    params={'purpose':'full uppercase','analyzed':analyzed_text}
    djtext=analyzed_text
    purpose1+=params['purpose']+"|"
    
 
  #remove the extra space between characters   
  if extraspaceremover=='on':
    analyzed_text=""
    for index,char in enumerate(djtext):
      if not (djtext[index]==' ' and djtext[index+1]==' '):
        analyzed_text+=char
      else:
        pass
    params={'purpose':'extraspace removed','analyzed':analyzed_text}
    djtext=analyzed_text
    purpose1+=params['purpose']+"|"
  
   #count chars
    
    
    
  
  #remove new line char
  if newlineremover=="on":
    analyzed_text=""
    for char in djtext:
      if(char!='\n' and char!='\r'):
        analyzed_text+=char
    params={'purpose':'newline removed','analyzed':analyzed_text}
    purpose1+=params['purpose']+'|'
   
  
  
 

   
  if (capstext!="on" and removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" ):
      return HttpResponse("please Select any switch.")
  
  
  params['purpose']=purpose1 
  return render(request,'analyze.html',params)
 
