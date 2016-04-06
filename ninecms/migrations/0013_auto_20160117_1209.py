# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 10:09

# Overridden migration to prepare default value for block name
# and to transfer elements to new m2m field

# Several lines excluded from tests with pragma nocover
# Haven't found a working way to test migrations, the following have been tested:
# https://micknelson.wordpress.com/2013/03/01/testing-django-migrations/
# https://www.caktusgroup.com/blog/2016/02/02/writing-unit-tests-django-migrations/
# Other migrations include 0009

from __future__ import unicode_literals
from django.db import migrations, models


def str_block(block):  # pragma: nocover
    """ Get title based on block type
    The default `__str__` methods do not operate within migrations
    :return: model title
    """
    if block.type == 'static':
        return '-'.join((block.type, block.node.title))
    elif block.type == 'menu':
        return '-'.join((block.type, block.menu_item.title))
    elif block.type == 'signal':
        return '-'.join((block.type, block.signal))
    return block.type


# noinspection PyUnusedLocal
# noinspection PyPep8Naming
def provide_block_name_default(apps, schema_editor):
    """ Provide a default block name in order for the next migration to establish field unique
    :param apps: app registry
    :param schema_editor
    :return: None
    """
    Block = apps.get_model('ninecms', 'ContentBlock')
    for block in Block.objects.all():  # pragma: nocover
        block.name = '%s-%d' % (str_block(block), block.pk)
        block.save()


# noinspection PyUnusedLocal
# noinspection PyPep8Naming
def transfer_elements(apps, schema_editor):
    """ Transfer records from deprecated PageLayoutElements to new page_types block field
    :param apps
    :param schema_editor
    :return: None
    """
    PageLayoutElement = apps.get_model('ninecms', 'PageLayoutElement')
    for element in PageLayoutElement.objects.all():  # pragma: nocover
        element.block.page_types.add(element.page_type)


# noinspection PyUnusedLocal
def reverse(apps, schema_editor):  # pragma: nocover
    """
    Reverse the above operations
    Nothing to do here, data in fields will be removed anyway
    :param apps: app registry
    :param schema_editor
    :return: None
    """
    pass


class Migration(migrations.Migration):
    """ Migration class """

    dependencies = [
        ('ninecms', '0012_auto_20151218_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentblock',
            name='name',
            field=models.CharField(
                help_text='Specify a unique block machine name.',
                max_length=100,
                null=True,
                verbose_name='name'
            ),
        ),
        migrations.AddField(
            model_name='contentblock',
            name='page_types',
            field=models.ManyToManyField(
                blank=True,
                related_name='blocks',
                to='ninecms.PageType',
                verbose_name='page types'
            ),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='language',
            field=models.CharField(
                blank=True,
                choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-co', 'Colombian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmal'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese')], max_length=2, verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='node',
            name='language',
            field=models.CharField(
                blank=True,
                choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-co', 'Colombian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmal'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese')], max_length=2, verbose_name='language'),
        ),
        migrations.RemoveField(
            model_name='pagetype',
            name='template',
        ),
        migrations.RunPython(provide_block_name_default, reverse),
        migrations.RunPython(transfer_elements, reverse),
    ]
