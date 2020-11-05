from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Game, Scene, Answer


def index(request):

    games = Game.objects.all()
    return render(request, 'game/index.html', {'game_list': games})


def game(request, slug):
 
    if request.method == 'POST':
        answer = request.POST.get('answer', None)
        new_scene = get_object_or_404(Scene, id=answer)
        new_answers = Answer.objects.all().filter(scene=new_scene.id)
        return render(request, 'game/game.html',
                {'scene': new_scene,
                 'answerlist': new_answers})  
    
    else:
        game = get_object_or_404(Game, slug=slug)
        first_scene = get_object_or_404(Scene,
                                        id=game.first_scene_id)
        answers = get_list_or_404(Answer, scene=first_scene.id)
        return render(request, 'game/game.html',
                      {'scene': first_scene,
                       'answerlist': answers})

