from django.contrib.auth.models import User
from django.db import models

from Site.apps import *


class Logs(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.SET_NULL, default=None, blank=True,
                             null=True)
    place = models.CharField(max_length=200, default='')
    action = models.CharField(max_length=200, default='')
    details = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    date = models.DateTimeField(verbose_name='Дата', default=None, blank=True, null=True)

    def __str__(self):
        return self.action

    class Meta:
        ordering = ['action', 'pk']


class Environments(models.Model):
    key = models.CharField(max_length=200, default='', db_index=True, unique=True)
    value = models.TextField(default='')

    def __str__(self):
        return self.key

    class Meta:
        ordering = ['key', 'pk']
        verbose_name_plural = 'Переменные окружения'
        verbose_name = 'Переменая окружения'


class CorruptInfo(models.Model):
    value = models.CharField(max_length=200, verbose_name='Значение', default='', db_index=True)
    info = models.TextField(verbose_name='Информация', default='', blank=True)
    tech = models.BooleanField(verbose_name='Управление администратором', default=False)
    extend_finish = models.IntegerField(verbose_name='Завершение формирования словаря', default=0)
    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.value

    class Meta:
        ordering = ['value', 'pk']
        verbose_name_plural = 'Ключевые слова'
        verbose_name = 'Ключевое слово'


class CorruptExtend(models.Model):
    corruptInfo = models.ForeignKey(CorruptInfo, verbose_name='Ключевое слово', on_delete=models.SET_NULL, default=None,
                                    blank=True, null=True)
    value = models.CharField(max_length=200, verbose_name='Мутант', default='', db_index=True)

    def __str__(self):
        return self.value

    class Meta:
        ordering = ['value', 'pk']
        verbose_name_plural = 'Ключевые слова (мутации)'
        verbose_name = 'Ключевое слово (мутация)'


class CorruptExtendFin(models.Model):
    corruptInfo = models.ForeignKey(CorruptInfo, verbose_name='Ключевое слово', on_delete=models.SET_NULL, default=None,
                                    blank=True, null=True)
    type = models.CharField(max_length=200, verbose_name='Тип', default='', db_index=True)
    count = models.IntegerField(verbose_name='Размер словаря', default=0)

    def __str__(self):
        return self.type

    class Meta:
        ordering = ['type', 'pk']
        verbose_name_plural = '(мутации)'
        verbose_name = '(мутация)'


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
    type = models.CharField(max_length=200, verbose_name='Тип', default='')
    name = models.CharField(max_length=200, verbose_name='Название', default='')
    stage = models.ForeignKey(StatusStage, verbose_name='Этап', on_delete=models.SET_NULL, default=None, blank=True,
                              null=True)
    value = models.IntegerField(verbose_name='Значение (%)', default=0)
    block = models.BooleanField(verbose_name='Заблокирован', default=True)
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
    file = models.FileField(verbose_name='Файл')

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
    type = models.CharField(max_length=200, verbose_name='Тип', default='', unique=True, db_index=True)
    name = models.CharField(max_length=200, verbose_name='Название', default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Таблицы'
        verbose_name = 'Таблица'


class Column(models.Model):
    table = models.ForeignKey(Table, verbose_name='Таблица', on_delete=models.SET_NULL, default=None, null=True)
    title = models.CharField(max_length=200, verbose_name='Название', default='')
    data = models.CharField(max_length=200, verbose_name='Набор данных', default='')
    order = models.IntegerField(verbose_name='Позиция', default=0)
    view = models.BooleanField(verbose_name='Отображаемый в карточке', default=True)
    viewOrder = models.IntegerField(verbose_name='Позиция в карточке', default=0)
    orderable = models.BooleanField(verbose_name='Сортируемый', default=True)
    searchable = models.BooleanField(verbose_name='Поиск в столбце', default=True)
    fixed = models.BooleanField(verbose_name='Зафиксировать', default=False)
    hide = models.BooleanField(verbose_name='Не скрываемый', default=False)
    visible = models.BooleanField(verbose_name='Отображаемый (по умолчанию)', default=True)
    render = models.ForeignKey(Render, verbose_name='Рендер', on_delete=models.SET_NULL, default=None, blank=True,
                               null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['table', 'order']
        verbose_name_plural = 'Столбцы'
        verbose_name = 'Столбец'


class PatternTable(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название', default='')
    table = models.ForeignKey(Table, verbose_name='Таблица', on_delete=models.SET_NULL, default=None, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Шаблоны'
        verbose_name = 'Шаблон'


class PatternColumn(models.Model):
    pattern = models.ForeignKey(PatternTable, verbose_name='Шаблон', on_delete=models.SET_NULL, default=None, null=True)
    column = models.ForeignKey(Column, verbose_name='Столбец', on_delete=models.SET_NULL, default=None, null=True)

    def __str__(self):
        return self.pattern.__str__()

    class Meta:
        verbose_name_plural = 'Шаблоны Столбцы'
        verbose_name = 'Шаблон Столбец'


class Countries(models.Model):
    title = models.CharField(max_length=200, verbose_name='Страна', default='', db_index=True)
    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Страны'
        verbose_name = 'Страна'


class Regions(models.Model):
    title = models.CharField(max_length=200, verbose_name='Регион', default='', db_index=True)
    country = models.ForeignKey(Countries, verbose_name='Страна', on_delete=models.SET_NULL, default=None, blank=True,
                                null=True)
    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Регионы'
        verbose_name = 'Регион'


class Cities(models.Model):
    title = models.CharField(max_length=200, verbose_name='Город', default='', db_index=True)
    country = models.ForeignKey(Countries, verbose_name='Страна', on_delete=models.SET_NULL, default=None, blank=True,
                                null=True)
    region = models.ForeignKey(Regions, verbose_name='Регион', on_delete=models.SET_NULL, default=None, blank=True,
                               null=True)
    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Города'
        verbose_name = 'Город'


class Place(models.Model):
    country = models.ForeignKey(Countries, verbose_name='Страна', on_delete=models.SET_NULL, default=None, blank=True,
                                null=True)
    region = models.ForeignKey(Regions, verbose_name='Регион', on_delete=models.SET_NULL, default=None, blank=True,
                               null=True)
    city = models.ForeignKey(Cities, verbose_name='Город', on_delete=models.SET_NULL, default=None, blank=True,
                             null=True)

    def __str__(self):
        return self.country.__str__() + ' : ' + self.region.__str__() + ' : ' + self.city.__str__()

    class Meta:
        ordering = ['country', 'region', 'city']
        verbose_name_plural = 'Места'
        verbose_name = 'Место'


class Vch(models.Model):
    number = models.CharField(max_length=200, verbose_name='Номер ВЧ', default='', db_index=True)
    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['number']
        verbose_name_plural = 'Воинские части'
        verbose_name = 'Воинская часть'


class ControlUser(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.SET_NULL, default=None, blank=True,
                             null=True)

    lastName = models.CharField(max_length=200, verbose_name='Фамилия', default='', db_index=True)
    firstName = models.CharField(max_length=200, verbose_name='Имя', default='', db_index=True)
    patronymic = models.CharField(max_length=200, verbose_name='Отчество', default='', blank=True)

    lastNameT = models.CharField(max_length=200, verbose_name='Фамилия (транслит)', default='', blank=True)
    firstNameT = models.CharField(max_length=200, verbose_name='Имя (транслит)', default='', blank=True)
    patronymicT = models.CharField(max_length=200, verbose_name='Отчество (транслит)', default='', blank=True)

    birthDay = models.IntegerField(verbose_name='День рождения', default=0, blank=True)
    birthMonth = models.IntegerField(verbose_name='Месяц рождения', default=0, blank=True)
    birthYear = models.IntegerField(verbose_name='Год рождения', default=0, blank=True)

    birthPlace = models.ForeignKey(Place, verbose_name='Место рождения', on_delete=models.SET_NULL, default=None,
                                   blank=True, null=True, related_name='birthPlace')

    livePlace = models.ForeignKey(Place, verbose_name='Место жительства', on_delete=models.SET_NULL, default=None,
                                  blank=True, null=True, related_name='livePlace')

    schools = models.TextField(verbose_name='Школа', default='', blank=True)
    universities = models.TextField(verbose_name='ВУЗ', default='', blank=True)

    work = models.TextField(verbose_name='Место работы', default='', blank=True)

    vch = models.ForeignKey(Vch, verbose_name='Место военной службы', on_delete=models.SET_NULL, default=None,
                            blank=True, null=True)

    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.SET_NULL, default=None, blank=True,
                               null=True)

    updatedAt = models.DateTimeField(verbose_name='Дата последнего обновления', default=None, blank=True, null=True)
    lastSearchAt = models.DateTimeField(verbose_name='Дата последнего поиска', default=None, blank=True, null=True)
    lastAnalysisAt = models.DateTimeField(verbose_name='Дата последнего анализа', default=None, blank=True, null=True)
    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.lastName + ' ' + self.firstName

    def fullName(self):
        return self.lastName + ((' ' + self.firstName) if self.firstName != '' else '') + (
            (' ' + self.patronymic) if self.patronymic != '' else '')

    def shortName(self):
        return self.lastName + ((' ' + self.firstName[0] + '.') if self.firstName != '' else '') + (
            (self.patronymic[0] + '.') if self.patronymic != '' else '')

    class Meta:
        ordering = ['lastName', 'firstName', 'patronymic']
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'


class Phone(models.Model):
    controlUser = models.ForeignKey(ControlUser, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    value = models.CharField(max_length=200, verbose_name='Значение', default='', db_index=True)

    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.value

    class Meta:
        ordering = ['value']
        verbose_name_plural = 'Номера телефонов'
        verbose_name = 'Номер телефона'


class Mail(models.Model):
    controlUser = models.ForeignKey(ControlUser, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    value = models.CharField(max_length=200, verbose_name='Значение', default='', db_index=True)

    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.value

    class Meta:
        ordering = ['value']
        verbose_name_plural = 'Адреса эл.почт'
        verbose_name = 'Адрес эл.почты'


class ControlUserImg(models.Model):
    controlUser = models.ForeignKey(ControlUser, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    file = models.ForeignKey(File, on_delete=models.SET_NULL, default=None, blank=True, null=True)

    removeAt = models.DateTimeField(verbose_name='Дата удаления', default=None, blank=True, null=True)

    def __str__(self):
        return self.controlUser.__str__()

    class Meta:
        verbose_name_plural = 'Фото сотрудников'
        verbose_name = 'Фото сотрудника'


class ControlUserPlace(models.Model):
    controlUser = models.ForeignKey(ControlUser, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    place = models.ForeignKey(Place, verbose_name='Место', on_delete=models.SET_NULL, default=None, blank=True,
                              null=True)

    def __str__(self):
        return self.controlUser.__str__() + ' : ' + self.place.__str__()

    class Meta:
        verbose_name_plural = 'Фото сотрудников'
        verbose_name = 'Фото сотрудника'


class Social(models.Model):
    controlUser = models.ForeignKey(ControlUser, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    prefix = models.CharField(max_length=200, verbose_name='Префикс', default='https://vk.com/id')
    value = models.CharField(max_length=200, verbose_name='Значение', default='', db_index=True)

    confirmedAt = models.DateTimeField(verbose_name='Дата подтверждения', default=None, blank=True, null=True)

    def __str__(self):
        return self.value

    class Meta:
        ordering = ['value']
        verbose_name_plural = 'Социальные сети'
        verbose_name = 'Социальная сеть'


class Post(models.Model):
    social = models.ForeignKey(Social, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    id_post = models.IntegerField(verbose_name='Номер поста', blank=True, default=0)
    date = models.DateTimeField(verbose_name='Дата добавления', default=None, blank=True, null=True)
    text = models.TextField(verbose_name='Текст поста', default='', blank=True)

    def __str__(self):
        return self.id_post.__str__()

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'


class PostCorrupt(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    corrupt = models.ForeignKey(CorruptInfo, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    confirmedAt = models.DateTimeField(verbose_name='Дата подтверждения', default=None, blank=True, null=True)


class Video(models.Model):
    social = models.ForeignKey(Social, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    id_video = models.IntegerField(verbose_name='Номер видеозаписи', blank=True, default=0)
    date = models.DateTimeField(verbose_name='Дата добавления', default=None, blank=True, null=True)
    name = models.TextField(verbose_name='Название видеозаписи', default='', blank=True)
    link = models.TextField(verbose_name='Ссылка на видеозапись', default='', blank=True)

    def __str__(self):
        return self.id_video.__str__()

    class Meta:
        verbose_name_plural = 'Видеозаписи'
        verbose_name = 'Видеозапись'


class VideoCorrupt(models.Model):
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    corrupt = models.ForeignKey(CorruptInfo, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    confirmedAt = models.DateTimeField(verbose_name='Дата подтверждения', default=None, blank=True, null=True)


class Groups(models.Model):
    social = models.ForeignKey(Social, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    id_groups = models.IntegerField(verbose_name='Номер сообщества', blank=True, default=0)
    name = models.TextField(verbose_name='Название сообщества', default='', blank=True)

    def __str__(self):
        return self.id_groups.__str__()

    class Meta:
        verbose_name_plural = 'Сообщества'
        verbose_name = 'Сообщество'


class GroupsCorrupt(models.Model):
    groups = models.ForeignKey(Groups, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    corrupt = models.ForeignKey(CorruptInfo, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    confirmedAt = models.DateTimeField(verbose_name='Дата подтверждения', default=None, blank=True, null=True)


class Inf(models.Model):
    social = models.ForeignKey(Social, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    about = models.TextField(verbose_name='О себе', default='', blank=True)
    activities = models.TextField(verbose_name='Деятельность', default='', blank=True)
    books = models.TextField(verbose_name='Любимые книги', default='', blank=True)
    games = models.TextField(verbose_name='Любимые игры', default='', blank=True)
    interests = models.TextField(verbose_name='Интересы', default='', blank=True)
    movies = models.TextField(verbose_name='Любимые фильмы', default='', blank=True)
    music = models.TextField(verbose_name='Любимая музыка', default='', blank=True)
    nickname = models.TextField(verbose_name='Никнейм', default='', blank=True)
    quotes = models.TextField(verbose_name='Любимые цитаты', default='', blank=True)
    status = models.TextField(verbose_name='Статус пользователя', default='', blank=True)
    tv = models.TextField(verbose_name='Любимые телешоу', default='', blank=True)

    def __str__(self):
        return self.social.__str__()

    class Meta:
        verbose_name_plural = 'Информация о пользователях'
        verbose_name = 'Информация о пользователе'


class InfCorrupt(models.Model):
    inf = models.ForeignKey(Inf, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    corrupt = models.ForeignKey(CorruptInfo, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    confirmedAt = models.DateTimeField(verbose_name='Дата подтверждения', default=None, blank=True, null=True)


class Photos(models.Model):
    social = models.ForeignKey(Social, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    link = models.TextField(verbose_name='Ссылка на фотоизображение', default='', blank=True)

    def __str__(self):
        return self.social.__str__()

    class Meta:
        verbose_name_plural = 'Фотоизображения'
        verbose_name = 'Фотоизображение'


class PhotosCorrupt(models.Model):
    photo = models.ForeignKey(Photos, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    corrupt = models.ForeignKey(CorruptInfo, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    confirmedAt = models.DateTimeField(verbose_name='Дата подтверждения', default=None, blank=True, null=True)


class PostsChecks(models.Model):
    social = models.ForeignKey(Social, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    id_post = models.IntegerField(verbose_name='Номер поста', blank=True, default=0)

    def __str__(self):
        return self.id_post.__str__()

    class Meta:
        verbose_name_plural = 'Проверенные посты'
        verbose_name = 'Проверенный пост'


class VideoChecks(models.Model):
    social = models.ForeignKey(Social, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    id_video = models.IntegerField(verbose_name='Номер видеозаписи', blank=True, default=0)

    def __str__(self):
        return self.id_video.__str__()

    class Meta:
        verbose_name_plural = 'Проверенные видеозаписи'
        verbose_name = 'Проверенная видеозапись'


class GroupsChecks(models.Model):
    social = models.ForeignKey(Social, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    id_groups = models.IntegerField(verbose_name='Номер сообщества', blank=True, default=0)

    def __str__(self):
        return self.id_groups.__str__()

    class Meta:
        verbose_name_plural = 'Проверенные сообщества'
        verbose_name = 'Проверенное сообщество'


class PhotosChecks(models.Model):
    social = models.ForeignKey(Social, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    link = models.TextField(verbose_name='Ссылка на фотоизображение', default='', blank=True)

    def __str__(self):
        return self.social.__str__()

    class Meta:
        verbose_name_plural = 'Проверенные фотоизображения'
        verbose_name = 'Проверенное фотоизображение'


class AllUsersVK(models.Model):
    id_user = models.IntegerField(verbose_name='id пользователя', default=0, blank=True)
    first_name = models.TextField(verbose_name='Имя', default='', blank=True)
    last_name = models.TextField(verbose_name='Фамилия', default='', blank=True)
    bdate = models.TextField(verbose_name='Дата рождения', default="", blank=True)
    home_town = models.TextField(verbose_name='Место рождения', default='', blank=True)
    city = models.TextField(verbose_name='Место жительства', default='', blank=True)

    def __str__(self):
        return self.id_user.__str__()

    class Meta:
        verbose_name_plural = 'Пользователи VK'
        verbose_name = 'Пользователь VK'


class TokenAdmin(models.Model):
    tokenVK = models.TextField(verbose_name='Токен администратора', default='')

    def __str__(self):
        return self.tokenVK.__str__()

    class Meta:
        verbose_name_plural = 'Токены администратора'
        verbose_name = 'Токен администратора'


class TokensForVkUpdate(models.Model):
    tokenVK = models.TextField(verbose_name='Токен', default='')

    def __str__(self):
        return self.tokenVK.__str__()

    class Meta:
        verbose_name_plural = 'Токены для обновления базы пользователей VK'
        verbose_name = 'Токен для обновления базы пользователей VK'
