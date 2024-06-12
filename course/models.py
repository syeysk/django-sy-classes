from django.db import models


class Course(models.Model):
    title = models.CharField('Наименование', max_length=100)
    description = models.TextField('Описание', max_length=1000, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Учебный курс'
        verbose_name_plural = 'Учебные курсы'


class Module(models.Model):
    title = models.CharField('Наименование', max_length=100)
    description = models.TextField('Описание', max_length=1000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules', verbose_name='Учебный курс')

    def __str__(self):
        return f'{self.course.title} - {self.title}'

    class Meta:
        verbose_name = 'Учебный модуль'
        verbose_name_plural = 'Учебные модули'


class Part(models.Model):
    title = models.CharField('Наименование', max_length=100)
    description = models.TextField('Описание', max_length=1000)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='parts', verbose_name='Модуль')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел модуля'
        verbose_name_plural = 'Разделы модуля'


class Relation(models.Model):
    title = models.CharField('Что', max_length=100)
    answer = models.CharField('Значение', max_length=100)
    theme = models.CharField('Тема факта', max_length=100)
    source = models.CharField('Источник факта', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Факт'
        verbose_name_plural = 'Факты'


class Exercise(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name='exercises', verbose_name='Раздел')
    lesson_number = models.IntegerField('Номер урока')
    relation = models.ForeignKey(
        Relation,
        on_delete=models.CASCADE,
        related_name='exercises',
        verbose_name='Изучаемый факт',
    )

    def __str__(self):
        return f'Урок {self.lesson_number} ({self.part}): упражнение "{self.relation}"'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
