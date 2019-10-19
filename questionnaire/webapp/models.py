from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=100, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.question


class Choice(models.Model):
    answer = models.TextField(max_length=200, null=False, blank=False, verbose_name='Ответ')
    poll = models.ForeignKey('Poll', related_name='choices', null=False, blank=False, on_delete=models.CASCADE, verbose_name='Вопрос')

    def __str__(self):
        return self.answer


class Answer(models.Model):
    poll = models.ForeignKey('Poll', related_name='poll_choices', on_delete=models.CASCADE, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата ответа')
    answer = models.ForeignKey('Choice', related_name='choice_polls', on_delete=models.CASCADE, verbose_name='Ответ')

    def __str__(self):
        return "{} | {}".format(self.poll, self.answer)

