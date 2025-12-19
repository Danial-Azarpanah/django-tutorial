from django.shortcuts import render, HttpResponse


def say_hello(request):
    # return HttpResponse("Hello world")
    return render(
        request,
        "post/index.html",
        context={"name": "Danial", "age": 22, "scores": [20, 14, 10, 16]}
    )