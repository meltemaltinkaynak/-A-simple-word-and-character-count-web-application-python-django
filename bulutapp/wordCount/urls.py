from django.urls import path
from . import views
#http://127.0.0.1:8000/  => index.html
#http://127.0.0.1:8000/index  => index.html
#http://127.0.0.1:8000/wordcount => wordcount.html
#http://127.0.0.1:8000/wordcount/3 => wordcount-details.html

urlpatterns = [
    path("" , views.index, name= "home"),         #anasayfa
    path("index" , views.index),    #anasayfa
    path("wordtxtCounter" , views.wordtxt, name= "wordtxt"),
    path('count/', views.count, name='count'),
    path("wordcountDetails" , views.wordcount_details, name= "details"),
    path("wc" , views.wc, name= "wc")
    
        
]