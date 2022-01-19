from django.shortcuts import render

# Create your views here.

def view_count(request):
    new_view_count = request.session.get('views', 0) + 1
    request.session['views'] = new_view_count
    response = render(request, 'hello/view_count.html', {'view_count' : new_view_count})
    response.set_cookie('dj4e_cookie', '556af255', max_age=1000)
    return response