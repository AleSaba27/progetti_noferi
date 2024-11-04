from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.db.models import F
from langchain_ollama import OllamaLLM
# Create your views here.
import markdown
from django.db import models
import requests
import pandas as pd
import random

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Question, Choice,Cat,Price
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
def ollama(request):
    
    model = OllamaLLM(model="gemma2:2b")

    response = model.invoke(input="Fai qualche esempio di progetto web")

    print(response)

    context ={'response': markdown.markdown(response, extensions=['extra', 'codehilite'])}

    return render (request, "polls/ollama.html", context=context)


def gatti(request):
    gatti=Cat.objects.all()  
    context ={
        'gatti':gatti,
        }    
    return render (request, "polls/gatti.html", context=context)



def scarica_gatti(request):
    params={
        'animal_type':'cat',
        'amount': 25,
    }    
    r=requests.get("https://cat-fact.herokuapp.com/facts/random", params=params)
    gatti=r.json()
    for gatto in gatti:
        #crea nuovo oggetto di tipo gcat
        c = Cat(text=gatto['text'])
        c.save()
    context ={
        'gatti':gatti,
        }    
    return render (request, "polls/scarica_gatti.html", context=context)


def dati(request):
    df=pd.read_csv('../Product_v6.csv')
    tabella=df[['name', 'value']]
    tabella=tabella[tabella['value']>0]
    tabella=tabella[tabella['value']<1000]
    context ={
        'tabella':tabella.to_html()
        }    
    return render (request, "polls/dati.html", context=context)


def grafico(request):
    context= {
        
    }
    return render(request, 'polls/grafico.html', context=context)




def scarica_prices(request):
    params={
       
    }    
    r=requests.get("https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=200&aggregate=3&e=CCCAGG", params=params)

    prices=r.json()

    print(prices['Data'])

    for price in prices['Data']:

        p = Price(time=price['time'], close=price['close'])
        p.save()
 
    context ={
        'prices' : prices,
        }    
    return render (request, "polls/scarica_prices.html", context=context)




def prices(request):
    prices = Price.objects.all()
    d = {'Data':
          [{'time':p.time, 'close':p.close} for p in prices]
        }
    print(d)
      
    return JsonResponse(d)


def chart(request):
    context= {
        "labels": ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        "data": [random.randrange(3, 9),random.randrange(3, 9),
                 random.randrange(3, 9),random.randrange(3, 9),
                 random.randrange(3, 9),random.randrange(3, 9)
                ],
        
    }
    return render(request, 'polls/chart.html', context=context)
