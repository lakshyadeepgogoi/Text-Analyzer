# #I have created this file -Lakshya
# from django.http import HttpResponse


# code for video 6
# def index(request):
#     return  HttpResponse('''<h1>Navigation Bar----</h1>  <a href="https://lakshyadeepgogoi.netlify.app/"> My website <br> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&ab_channel=CodeWithHarry/"> code with harry  ''')
# def about(request):
#     return  HttpResponse("About lakshya bhai")
# # def contact(request):
#     return  HttpResponse("contact lakshya bhai")


from concurrent.futures.process import _ExecutorManagerThread
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # a='''
    # <button><a href="/about">About</a></button>
    # <button><a href="/gallery">Gallery</a></button>
    # <button><a href="/services">Services</a></button>
    # <button><a href="/contact">Contact</a></button>

    # '''
    # return HttpResponse(a)

# def about(request):
#     a='''
#     <h1>About</h1>
#     <button><a href="/">Back</a></button>

#     '''
#     return HttpResponse(a)

# def gallery(request):
#     a='''
#     <h1>Gallery</h1>
#     <button><a href="/">Back</a></button>


#     '''
#     return HttpResponse(a)

# def services(request):
#     a='''
#     <h1>Services</h1>
#     <button><a href="/">Back</a></button>
#     '''
#     return HttpResponse(a)

def analyze(request):
    data = request.GET.get('text', 'No text entered')

    remPunc = request.GET.get('punc', 'of')
    caps = request.GET.get('caps', 'of')
    newLineRem = request.GET.get('newLineRem', 'of')
    spaceRem = request.GET.get('spaceRem', 'of')

    charcount = request.GET.get('charcount', 'of')
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
        # return render(request, 'analyze.html', params)
    if caps == 'on':
        print("2", strr)
        strr = strr.upper()
        params = {'purpose': 'Caps', 'answer': strr}
        purpose += "| Caps |"
        # return render(request, 'analyze.html', params)

    if newLineRem == 'on':
        tempStr = ""
        for i in strr:
            if i != '\n':
                tempStr += i
        params = {'purpose': 'New Line remove', 'answer': tempStr}
        strr = tempStr
        purpose += "| remove new line "
        # return render(request, 'analyze.html', params)

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
        return HttpResponse('error hai bhai')
