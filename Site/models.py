from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

from Site.apps import *
from mysite.settings import MEDIA_ROOT


class CorruptInfo(models.Model):
    value = models.CharField(max_length=200, verbose_name='Значение', default='')
    info = models.TextField(verbose_name='Информация', default='', blank=True)

    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.value

    class Meta:
        ordering = ['value', 'pk']
        verbose_name_plural = 'Данные'
        verbose_name = 'Данные'


class StatusStage(models.Model):
    type = models.CharField(max_length=200, verbose_name='Тип', default='', unique=True)
    name = models.CharField(max_length=200, verbose_name='Название', default='')
    value = models.IntegerField(verbose_name='Значение', default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['value', 'name']
        verbose_name_plural = 'Этапы статусов'
        verbose_name = 'Этап статуса'


class Status(models.Model):
    type = models.CharField(max_length=200, verbose_name='Тип', default='', unique=True)
    name = models.CharField(max_length=200, verbose_name='Название', default='')
    stage = models.ForeignKey(StatusStage, verbose_name='Этап', on_delete=models.CASCADE, default=None, blank=True,
                              null=True)
    value = models.IntegerField(verbose_name='Значение (%)', default=0)
    color = models.CharField(max_length=200, verbose_name='Цвет', default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['stage', 'value', 'name']
        verbose_name_plural = 'Статусы'
        verbose_name = 'Статусы'


class LastUpdateConfig(models.Model):
    type = models.CharField(max_length=200, verbose_name='Тип', default='')
    dateStart = models.DateTimeField(verbose_name='Дата начала', default=None, blank=True, null=True)
    dateEnd = models.DateTimeField(verbose_name='Дата окончания', default=None, blank=True, null=True)

    def __str__(self):
        return self.type

    class Meta:
        ordering = ['type']
        verbose_name_plural = 'Последние обновления конфигурации'
        verbose_name = 'Последнее обновление конфигурации'


class File(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название', default='')
    file = models.FileField(upload_to=MEDIA_ROOT, verbose_name='Файл')

    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Файлы'
        verbose_name = 'Файл'


class Render(models.Model):
    type = models.CharField(max_length=200, verbose_name='Тип', default='')
    name = models.CharField(max_length=200, verbose_name='Название', default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Рендеры'
        verbose_name = 'Рендер'


class Table(models.Model):
    type = models.CharField(max_length=200, verbose_name='Тип', default='', unique=True)
    name = models.CharField(max_length=200, verbose_name='Название', default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Таблицы'
        verbose_name = 'Таблица'


class Column(models.Model):
    table = models.ForeignKey(Table, verbose_name='Таблица', on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200, verbose_name='Название', default='')
    data = models.CharField(max_length=200, verbose_name='Набор данных', default='')
    order = models.IntegerField(verbose_name='Позиция', default=0)
    view = models.BooleanField(verbose_name='Отображаемый в карточке', default=True)
    viewOrder = models.IntegerField(verbose_name='Позиция в карточке', default=0)
    orderable = models.BooleanField(verbose_name='Сортируемый', default=True)
    fixed = models.BooleanField(verbose_name='Зафиксировать', default=False)
    hide = models.BooleanField(verbose_name='Не скрываемый', default=False)
    visible = models.BooleanField(verbose_name='Отображаемый (по умолчанию)', default=True)
    render = models.ForeignKey(Render, verbose_name='Рендер', on_delete=models.CASCADE, default=None, blank=True,
                               null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['table', 'order']
        verbose_name_plural = 'Столбцы'
        verbose_name = 'Столбец'


class PatternTable(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название', default='')
    table = models.ForeignKey(Table, verbose_name='Таблица', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Шаблоны'
        verbose_name = 'Шаблон'


class PatternColumn(models.Model):
    pattern = models.ForeignKey(PatternTable, verbose_name='Шаблон', on_delete=models.CASCADE, default=None)
    column = models.ForeignKey(Column, verbose_name='Столбец', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.pattern.__str__()

    class Meta:
        verbose_name_plural = 'Шаблоны Столбцы'
        verbose_name = 'Шаблон Столбец'


class Countries(models.Model):
    title = models.CharField(max_length=200, verbose_name='Страна', default='')
    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Страны'
        verbose_name = 'Страна'


class Regions(models.Model):
    title = models.CharField(max_length=200, verbose_name='Регион', default='')
    country = models.ForeignKey(Countries, verbose_name='Страна', on_delete=models.CASCADE, default=None, blank=True,
                                null=True)
    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Регионы'
        verbose_name = 'Регион'


class Cities(models.Model):
    title = models.CharField(max_length=200, verbose_name='Город', default='')
    country = models.ForeignKey(Countries, verbose_name='Страна', on_delete=models.CASCADE, default=None, blank=True,
                                null=True)
    region = models.ForeignKey(Regions, verbose_name='Регион', on_delete=models.CASCADE, default=None, blank=True,
                               null=True)
    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Города'
        verbose_name = 'Город'


class Place(models.Model):
    country = models.ForeignKey(Countries, verbose_name='Страна', on_delete=models.CASCADE, default=None, blank=True,
                                null=True)
    region = models.ForeignKey(Regions, verbose_name='Регион', on_delete=models.CASCADE, default=None, blank=True,
                               null=True)
    city = models.ForeignKey(Cities, verbose_name='Город', on_delete=models.CASCADE, default=None, blank=True,
                             null=True)

    def __str__(self):
        return self.country.__str__() + ' : ' + self.region.__str__() + ' : ' + self.city.__str__()

    class Meta:
        ordering = ['country', 'region', 'city']
        verbose_name_plural = 'Места'
        verbose_name = 'Место'


class Vch(models.Model):
    number = models.CharField(max_length=200, verbose_name='Номер ВЧ', default='')
    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['number']
        verbose_name_plural = 'Воинские части'
        verbose_name = 'Воинская часть'


class ControlUser(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, default=None, blank=True,
                             null=True)

    lastName = models.CharField(max_length=200, verbose_name='Фамилия', default='')
    firstName = models.CharField(max_length=200, verbose_name='Имя', default='')
    patronymic = models.CharField(max_length=200, verbose_name='Отчество', default='', blank=True)

    lastNameT = models.CharField(max_length=200, verbose_name='Фамилия (транслит)', default='', blank=True)
    firstNameT = models.CharField(max_length=200, verbose_name='Имя (транслит)', default='', blank=True)
    patronymicT = models.CharField(max_length=200, verbose_name='Отчество (транслит)', default='', blank=True)

    birthDay = models.IntegerField(verbose_name='День рождения', default=0, blank=True)
    birthMonth = models.IntegerField(verbose_name='Месяц рождения', default=0, blank=True)
    birthYear = models.IntegerField(verbose_name='Год рождения', default=0, blank=True)

    birthPlace = models.ForeignKey(Place, verbose_name='Место рождения', on_delete=models.CASCADE, default=None,
                                   blank=True, null=True, related_name='birthPlace')

    livePlace = models.ForeignKey(Place, verbose_name='Место жительства', on_delete=models.CASCADE, default=None,
                                  blank=True, null=True, related_name='livePlace')

    schools = models.TextField(verbose_name='Школа', default='', blank=True)
    universities = models.TextField(verbose_name='ВУЗ', default='', blank=True)

    work = models.TextField(verbose_name='Место работы', default='', blank=True)

    vch = models.ForeignKey(Vch, verbose_name='Место военной службы', on_delete=models.CASCADE, default=None,
                            blank=True, null=True)

    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.CASCADE,
                               default=None, blank=True, null=True)

    updatedAt = models.DateTimeField(verbose_name='Дата последнего обновления', default=None, blank=True, null=True)
    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.lastName + ' ' + self.firstName

    def fullName(self):
        return self.lastName \
               + ((' ' + self.firstName) if self.firstName != '' else '') \
               + ((' ' + self.patronymic) if self.patronymic != '' else '')

    def shortName(self):
        return self.lastName \
               + ((' ' + self.firstName[0]) if self.firstName != '' else '') \
               + ((' ' + self.patronymic[0]) if self.patronymic != '' else '')

    class Meta:
        ordering = ['lastName', 'firstName', 'patronymic']
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'


class Phone(models.Model):
    controlUser = models.ForeignKey(ControlUser, on_delete=models.CASCADE, default=None, blank=True, null=True)
    value = models.CharField(max_length=200, verbose_name='Значение', default='')

    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.value

    class Meta:
        ordering = ['value']
        verbose_name_plural = 'Номера телефонов'
        verbose_name = 'Номер телефона'


class Mail(models.Model):
    controlUser = models.ForeignKey(ControlUser, on_delete=models.CASCADE, default=None, blank=True, null=True)
    value = models.CharField(max_length=200, verbose_name='Значение', default='')

    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.value

    class Meta:
        ordering = ['value']
        verbose_name_plural = 'Адреса эл.почт'
        verbose_name = 'Адрес эл.почты'


class ControlUserImg(models.Model):
    controlUser = models.ForeignKey(ControlUser, on_delete=models.CASCADE, default=None, blank=True, null=True)
    file = models.ForeignKey(File, on_delete=models.CASCADE, default=None, blank=True, null=True)

    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.controlUser.__str__()

    class Meta:
        verbose_name_plural = 'Фото сотрудников'
        verbose_name = 'Фото сотрудника'


class ControlUserPlace(models.Model):
    controlUser = models.ForeignKey(ControlUser, on_delete=models.CASCADE, default=None, blank=True, null=True)
    place = models.ForeignKey(Place, verbose_name='Место', on_delete=models.CASCADE, default=None, blank=True,
                              null=True)

    def __str__(self):
        return self.controlUser.__str__() + ' : ' + self.place.__str__()

    class Meta:
        verbose_name_plural = 'Фото сотрудников'
        verbose_name = 'Фото сотрудника'


class Social(models.Model):
    controlUser = models.ForeignKey(ControlUser, on_delete=models.CASCADE, default=None, blank=True, null=True)
    value = models.CharField(max_length=200, verbose_name='Значение', default='')

    def __str__(self):
        return self.value

    class Meta:
        ordering = ['value']
        verbose_name_plural = 'Социальные сети'
        verbose_name = 'Социальная сеть'
