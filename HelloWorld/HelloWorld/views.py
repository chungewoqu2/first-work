from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello world ! ")#without templates,not useful

from django.shortcuts import render
def runoob(request):
    context = {}
    context['name'] = 'Hello World!'
    return render(request, 'runoob.html', context)
    #context is variables. use "runoob.html" to appoint return which html
'''
the upper also can be written as the below:
    views_dict = {"name":"菜鸟教程"}
    return render(request, "runoob.html", {"views_dict": views_dict})
    then we can use it in this way:
    <p>{{views.dict}}</p>
    <p>{{view.dict.name}}</p>  #here, '.name' means the value of the key "name" in views.dict
'''




