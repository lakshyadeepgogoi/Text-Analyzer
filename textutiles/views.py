# #I have created this file -Lakshya

from concurrent.futures.process import _ExecutorManagerThread
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    data = request.POST.get('text', 'No text entered')
    

    remPunc = request.POST.get('punc', 'of')
    caps = request.POST.get('caps', 'of')
    newLineRem = request.POST.get('newLineRem', 'of')
    spaceRem = request.POST.get('spaceRem', 'of')

    charcount = request.POST.get('charcount', 'of')
    strr = data
    purpose = ""

    if remPunc == 'on':
        tempStr = ""
        puns = '''!@#$%^&*();'.,/:?>'''
        for i in data:
            if i not in puns:
                tempStr = tempStr + i
        params = {'purpose': 'remove Punctuations', 'answer': tempStr}
        strr = tempStr
        purpose += " | Remove Punctuations "
        
    if caps == 'on':
        print("2", strr)
        strr = strr.upper()
        params = {'purpose': 'Caps', 'answer': strr}
        purpose += "| Caps |"
       

    if newLineRem == 'on':
        tempStr = ""
        for i in strr:
            if  i != '\n' and i !='\r':
                tempStr +=   i
        params = {'purpose': 'New Line remove', 'answer': tempStr}
        strr = tempStr
        purpose += "| remove new line "
       

    if spaceRem == 'on':
        tempStr = ""
        for index, ch in enumerate(strr):
            if not (strr[index] == " " and strr[index+1] == " "):
                tempStr += ch
        params = {'purpose': 'spaces remove', 'answer': tempStr}
        strr = tempStr
        purpose += "| Spaces remove |"

    params = {'purpose': purpose, 'answer': strr}

    if remPunc == 'on' or caps == 'on' or newLineRem == 'on' or spaceRem == 'on':
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('ERROR!!! ')
