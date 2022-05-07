from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def calculation(recipe, quantity):
	dic_context={}
	dic_context['recipe'] = DATA.get(recipe).copy()
	quantity = int(quantity)
	if quantity > 1:
		tmp = {}
		tmp = dic_context.get('recipe')
		for k,v in tmp.items():
			tmp.update({k:v*quantity})
	return dic_context


def omlet_view(request):
	return render(request, 'calculator/index.html', calculation('omlet',request.GET.get('servings',1)))
	
	
def pasta_view(request):
	return render(request, 'calculator/index.html', calculation('pasta',request.GET.get('servings',1)))
	
	
def buter_view(request):
	return render(request, 'calculator/index.html', calculation('buter',request.GET.get('servings',1)))
