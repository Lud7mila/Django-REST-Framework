from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    '''
    модель отвечающая за информацию о типе литературного произведения
    Поля:
        title(CharField): название категории литературного произведения
    '''
    class Meta:
        verbose_name = 'Категории произведений'
        verbose_name_plural = 'Категории произведений'

    title = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.title


class Author(models.Model):
    '''
    модель отвечающая за информацию об авторе литературного произведения
    Поля:
        name(CharField): имя автора
        surname(CharField): фамилия автора
        age(IntegerField): возраст автора
        greeting(TextField): приветственные слова автора
    '''
    class Meta:
        verbose_name = 'Авторы произведений'
        verbose_name_plural = 'Авторы произведений'

    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    age = models.IntegerField(verbose_name="Возраст")
    greeting = models.TextField(verbose_name="Приветствие")
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.surname


class LitWork(models.Model):
    '''
    модель отвечающая за информацию о литературном произведении
    Поля:
        title(CharField): название литературного произведения
        description(TextField): описание литературного произведения
        text(TextField): техт литературного произведения
        time_create(DateTimeField): дата и время создания
        time_update(DateTimeField): дата и время обновления
        author(ForeignKey): ссылка на автора произведения
        category(ForeignKey): ссылка на тип произведения
    '''
    class Meta:
        verbose_name = 'Литературные произведения'
        verbose_name_plural = 'Литературные произведения'

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    text = models.TextField(verbose_name="Текст")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete = models.CASCADE,
                                    related_name='author', verbose_name="Автор")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                    related_name='Category', verbose_name="Жанр")

    def __str__(self):
        return self.title


