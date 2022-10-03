# #I have created this file -Lakshya
# from django.http import HttpResponse


#code for video 6
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
    #Get the text
    djtext = request.GET.get('text', 'default')
    removepunc  = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)

    if removepunc == "on":
        # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed punctuations', 'analyzed_text': analyzed}

        #Analyze the text
        return render(request, 'analyze.html',params)

    else:
        return HttpResponse("Error")




