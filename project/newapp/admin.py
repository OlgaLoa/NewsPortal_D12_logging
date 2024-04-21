from django.contrib import admin
from .models import Post

# #напишем функцию увеличения рейтинга до 1
def increase_rating(modeladmin, request, queryset): # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(rating = 1)
increase_rating.short_description = 'Nullify rating' # описание для более понятного представления в админ панеле задаётся, как будто это объект

# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('author', 'categoryType', 'title','rating', 'text_length_greater_than_15') #оставляем только 4 поля
    list_filter = ('author', 'categoryType')  # добавляем фильтры группировки в нашу админку (справа фильтр отображается)
    search_fields = ('title', )  # тут всё очень похоже на фильтры из запросов в базу (появляется строка поиска)
    actions = [increase_rating]  # добавляем действия в список

admin.site.register(Post, PostAdmin)

