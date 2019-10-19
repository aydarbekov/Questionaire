# Generated by Django 2.2.6 on 2019-10-19 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата ответа')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_polls', to='webapp.Choice', verbose_name='Ответ')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll_choices', to='webapp.Poll', verbose_name='Вопрос')),
            ],
        ),
    ]