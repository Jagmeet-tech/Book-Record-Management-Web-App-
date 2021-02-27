from django.shortcuts import render
from django.http import HttpResponse

def showtest(request):
     #s="<h1>THIS IS TEST PAGE</h1>"
     que="Who developed C Language?"
     a="Ken Thompson"
     b="Dennis Ritchie"
     c="Bjarne Stroustrup"
     d="Saurabh Sir"
     level="easy"
     data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level}
     res=render(request,'exam/test.html',context=data)
     return res

def showresult(request):
     s="<h1>THIS IS RESULT PAGE</h1>"
     return HttpResponse(s)
