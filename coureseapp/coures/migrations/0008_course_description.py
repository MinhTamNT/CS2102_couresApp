# Generated by Django 4.2.6 on 2023-10-29 07:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("coures", "0007_remove_course_descrption"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="description",
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]