from django.http import HttpResponse
from django.shortcuts import render
import re
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("<a href='https://www.youtube.com/'>Youtube<a>  <a href='https://pbi-reporting.bosch.com/reports/powerbi/OSM_Dashboards/FAST_REPORTS/Landing%20page/Landing%20Page?rs:embed=true'>Effort Tracker<a>   <a href='https://inside-docupedia.bosch.com/confluence/display/idmfaq/WAM+-+Web+Access+Management#WAMWebAccessManagement-UsingWAMauthentication'>WAM WIKI<a>   <a href='https://inside-docupedia.bosch.com/confluence/display/qdas/Q-DAS+Home'>Q-Das WIKI<a>")
def analyze(request):
    djtext = request.POST.get('text','default')
    removepuncresp = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    analyzed = djtext
    purpose = ""
    if removepuncresp == "on":
        res = re.sub(r'[^\w\s]', '', analyzed)
        analyzed = res
        purpose = purpose + "Removed Punctuations"

    if fullcaps == "on":
        analyzed = analyzed.upper()
        purpose = purpose + " & Capitalized the sentence"

    if newlineremover == "on":
        length = len(analyzed)
        analyzed1 = ""
        for i in range(length):
            if analyzed[i] != '\n':
                analyzed1 = analyzed1 + analyzed[i]
        analyzed = analyzed1
        purpose = purpose + " & Removed the new line"

    if spaceremover == "on":
        length = len(analyzed)
        analyzed1 = ""
        for i in range(length):
            if not(analyzed[i] == ' ' and analyzed[i+1] == ''):
                analyzed1 = analyzed1 + analyzed[i]
        analyzed = analyzed1
        purpose = purpose + " & Removed the space"

    if charcount == "on":
        length = len(djtext)
        analyzed = analyzed + "\nThe number of character in the entered string is:"+str(length)
        purpose = purpose + " & Counted characters"

    params = {'purpose': purpose, 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
    

def remove_punc(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    return HttpResponse("Remove Punc")

def capfirst(request):
    return HttpResponse("Capitalize")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremove(request):
    return HttpResponse("spaceremove")

def charcount(request):
    return HttpResponse("charcount")

