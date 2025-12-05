from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='conteudo',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]