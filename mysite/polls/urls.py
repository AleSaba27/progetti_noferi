from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("ollama/", views.ollama, name="ollama"),
    path("gatti/", views.gatti, name="gatti"),
    path("scarica_gatti/", views.scarica_gatti, name="scarica_gatti"),
    path("dati/", views.dati, name="dati"),
    path("grafico/", views.grafico, name="grafico"),
    path("scarica_prices/", views.scarica_prices, name="scarica_prices"),
    path("prices/", views.prices, name="prices"),
    path("chart/", views.chart, name="chart"),
    path("scena/", views.scena, name="scena"),
    path("modelli/", views.modelli, name="modelli"),
    path("prove/", views.prove, name="prove"),
    path("provaqr/", views.provaqr, name="provaqr"),
    path("generaqr/", views.generaqr, name="generaqr"),
    path("speech_to_text/", views.speech_to_text, name="speech_to_text"),

]