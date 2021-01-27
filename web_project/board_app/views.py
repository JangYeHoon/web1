from django.shortcuts import render
from .forms import BoardForm
from .services import BoardService
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def board_list(request):
    content = BoardService().board_list(request)
    return render(request, 'board_list.html', content)

def board_input(request):
    user_id = request.session.get('login_id')
    if user_id == 'admin@admin.com':
        content = BoardService().board_input(request)
        return render(request, 'board_input.html', content)
    else:
        return render(request, 'board_input.html')

def board_add(request):
    input_value = BoardForm(request.POST)
    login_check = BoardService().board_add(request, input_value)
    if login_check == True:
        return HttpResponseRedirect(reverse('board_list'))
    else:
        return render(request, 'login.html')

def board_view(request):
    content = BoardService().board_view(request)
    return render(request, 'board_view.html', content)

def board_modify_input(request):
    content = BoardService().board_modify_input(request)
    return render(request, 'board_modify.html', content)

def board_modify(request):
    BoardService().board_modify(request)
    return HttpResponseRedirect(reverse('board_list'))

def board_delete(request):
    board_id = request.POST['board_id']
    BoardService().board_delete(board_id)
    return HttpResponseRedirect(reverse('board_list'))