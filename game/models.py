from django.db import models


class Scene(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    background_image = models.ImageField(max_length=255, blank=True, default='', upload_to='images/')

    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=200)
    first_scene = models.ForeignKey(Scene, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Answer(models.Model):
    scene = models.ForeignKey(Scene, null=True, related_name='scene', on_delete=models.CASCADE)
    next_scene = models.ForeignKey(Scene, null=True, related_name='next_scene', on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    
    def __str__(self):
        return self.answer

