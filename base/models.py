from django.db import models

#Класс отвечает за таблицу в БД. Создание таблицы происходит во время миграции

class Constructor(models.Model):
    #поле в БД, строка не более 250 симв(Название строки, макс длина, значение по умолчанию(не обяз))
    title = models.CharField('Название', max_length=50, default='')
    #поле в БД, текст
    full_text = models.TextField('Полный текст')
    #поле в БД, дата и время. (DateField - только дата)
    date = models.DateTimeField('Дата публикации')

    #Магический метод для отображение объектов таблицы в текстовом виде(если убрать, то будут вызываться объекты)
    def __str__(self):
        return self.title

    #Чтобы изменить название таблицы в панели администратора
    class Meta:
        verbose_name = 'Конструктор'
        verbose_name_plural = 'Конструкторы'
