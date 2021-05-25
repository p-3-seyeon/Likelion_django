from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def result(request):
    team = request.GET['team']

    wordList = team.split()

    wordDict = {}

    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    return render(request, "result.html", {'fulltext':team, 'count': len(wordList), "wordDict": wordDict.keys})


