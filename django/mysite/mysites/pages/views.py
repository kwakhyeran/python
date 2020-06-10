from django.shortcuts import render
from datetime import datetime

# Create your views here.
def dtl(request):
    my_list=['간짜장',"해물짬뽕","꿔바로우","콩국수"]
    empty_list=[]
    my_string = "Life is short, You need enjoy"
    today = datetime.now()
    context ={
        'my_list':my_list,
        'empty_list':empty_list,
        'my_string':my_string,
        'today':today
    }
    return render(request,'dtl.html',context)