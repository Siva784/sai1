
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.data,name="data-page"),
    path('investment/', views.investmentpage,name="investment"),
    path('bank_int/', views.bankint,name="bank-int"),
    path('stats/', views.stats,name="stats"),
    path('logs/', views.logs,name="logs"),
    path('update/<id>/', views.update,name="update"),
    path('alldata/', views.alldata,name="alldata"),
    path('statistics/', views.statistics,name="statistics"),
    path('retpay/<id>/', views.retpay,name="retpay"),
    
    
]
