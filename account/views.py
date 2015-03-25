from django.shortcuts import render_to_response


def cabinet_index(request):
    return render_to_response("cabinet_index.html")
