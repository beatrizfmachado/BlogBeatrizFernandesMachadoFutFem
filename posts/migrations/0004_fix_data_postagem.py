from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_conteudo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_postagem',
            field=models.DateTimeField(),
        ),
    ]