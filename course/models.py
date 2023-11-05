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
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules', verbose_name="Учебный курс")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Учебный модуль'
        verbose_name_plural = 'Учебные модули'
