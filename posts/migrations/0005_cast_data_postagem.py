from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_fix_data_postagem'),
    ]

    operations = [
        migrations.RunSQL(
            """
            ALTER TABLE posts_post
            ALTER COLUMN data_postagem
            TYPE timestamp USING to_timestamp(data_postagem);
            """,
            reverse_sql="""
            ALTER TABLE posts_post
            ALTER COLUMN data_postagem
            TYPE integer;
            """
        ),
    ]