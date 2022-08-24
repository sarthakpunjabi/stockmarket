from threading import Thread
from django.http import HttpResponse
from django.shortcuts import render
from yahoo_fin.stock_info import *
from django.contrib.auth.decorators import login_required
import requests
import queue
from twilio.rest import Client
from .data_collection import get_tweets

# Create your views here.
def stockPicker(request):
    """
    This Picks up the stocks list in real time
    """
    stock_picker = tickers_nifty50()
    return render(request,'main/stockpicker.html',context={'stockpicker':stock_picker })

@login_required
def stockTracker(request):
    """
    Retrieves the selected stocks information asynchronously with help of celery and cronjob
    """
    stockpicker = request.GET.getlist('stockpicker')
    data = {}
    available_stocker = tickers_nifty50()
    for i in stockpicker:
        if i in available_stocker:
            pass
        else:
            return HttpResponse('Error')
    
    n_threads = len(stockpicker)
    thread_list = []
    que = queue.Queue()
    for i in range(n_threads):
        thread = Thread(target = lambda q, arg1: q.put({stockpicker[i]:get_quote_table(arg1)}),args=(que,stockpicker[i]))
        thread_list.append(thread)
        thread_list[i].start()

    for thread in thread_list:
        thread.join()

    while not que.empty():
        result = que.get()
        data.update(result)

    return render(request,'main/stocktracker.html',context={'data':data,'room_name':'track'})



def getnews(request,key):
    """
    This retrieves the news of selected stock
    """
    api_key = "8357dc57ac6c4135ab3521c423f7f960"
    a = get_company_info(key)
    play = a.to_dict()
    fin = str(play["Value"]["longBusinessSummary"]).split(" ")[0]

    api = f"https://newsapi.org/v2/everything?q={fin}&apiKey=8357dc57ac6c4135ab3521c423f7f960"

    response = requests.get(api)
    articles = response.json()["articles"]
    some = {}
    main_dict = {}
    counter = 1
    for i in articles:
        for k,v in i.items():
            some[k] = v
        main_dict[str(counter)] = some
        some = {}
        counter+=1

    
    
    return render(request,"main/news.html",{"data":main_dict})


def fullnews(request):
    user = request.user
    data = request.POST
    client = Client("AC0ca78fcbadc1bf428b81539bf0317838", "af31ed74dcace769ef714438f6e20d63")
    api_key = "8357dc57ac6c4135ab3521c423f7f960"
    a = get_company_info(data.get("ticker"))
    play = a.to_dict()
    fin = str(play["Value"]["longBusinessSummary"]).split(" ")[0]

    api = f"https://newsapi.org/v2/everything?q={fin}&apiKey=8357dc57ac6c4135ab3521c423f7f960"

    response = requests.get(api)
    articles = response.json()["articles"][:3]
    formatted_articles = [f"Headiline: {article['title']}. \n Brief: {article['description']}" for article in articles]

    for ar in formatted_articles:
        message = client.messages.create(
                        body=ar,
                        from_='+15086905145',
                        to='+353894952273'
                    )

    return HttpResponse(articles)


def getaffirmation(request,news):
    answer = get_tweets(news)
    if answer:
        return HttpResponse("The news is not reliable")
    else:
        return HttpResponse("The news is reliable ")
