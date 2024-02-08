from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

############
#  Version 1
#  Multiple view functions for multiple urls


# def smoothie(request):
#     health_quote = 'Start your day with a smoothie'
#     return HttpResponse(health_quote)

# def salad(request):
#     health_quote = 'Salad is good for your health'
#     return HttpResponse(health_quote)

############
#  Version 2
#  Single view function for multiple urls
#  -> Dynamic URLs

# def handle_recipe(request, recipe):
#     # return HttpResponse(f'The recipe argument is {recipe}')
#     health_quote = ''

#     if recipe == 'smoothie':
#         health_quote = 'Start your day with a smoothie'
#     elif recipe == 'salad':
#         health_quote = 'Salad is good for your health'
#     else:
#         return HttpResponseNotFound(f'The recipe {recipe} was not found!!')

#     return HttpResponse(health_quote)
    
# def handle_recipe_with_number(request, recipe):
#     health_quote = ''
#     if recipe == 1:
#         health_quote = 'Start your day with a smoothie'
#     elif recipe == 2:
#         health_quote = 'Salad is good for your health'
#     else:
#         return HttpResponseNotFound(f'The recipe {recipe} was not found!!')
    
#     return HttpResponse(health_quote)



####################
# Version 3

# Use one view function with dynamic urls
# reduce code duplication

recipes_and_quotes = {
    'smoothie': 'Start your day with smoothie',
    'salad': 'Salad is good for your health'
}

# def handle_recipe(request, recipe):
#     # return HttpResponse(f'The recipe argument is {recipe}')
#     health_quote = ''

#     # if recipe not in recipes_and_quotes:
#     #     return HttpResponseNotFound('No info')
    
#     # health_quote = recipes_and_quotes[recipe]

#     try:
#         health_quote = recipes_and_quotes[recipe]
#         return HttpResponse(health_quote)
#     except:
#         return HttpResponseNotFound('No info')

    
# def handle_recipe_with_number(request, recipe):
#     health_quote = ''
#     # if recipe == 1:
#     #     health_quote = 'Start your day with a smoothie'
#     # elif recipe == 2:
#     #     health_quote = 'Salad is good for your health'
#     # else:
#     #     return HttpResponseNotFound(f'The recipe {recipe} was not found!!')
    
#     recipe_list = list(recipes_and_quotes.keys())
#     try:
#         if recipe <= 0 or recipe > len(recipe_list):
#             raise Exception()
        
#         selected_recipe = recipe_list[recipe - 1]
#     except:
#         return HttpResponseNotFound('No info')
    
#     health_quote = recipes_and_quotes[selected_recipe]
#     return HttpResponse(health_quote)



#####################
# Version 4

# Use handle_recipe in handle_recipe_with_number
# using redirect


def handle_recipe(request, recipe):
    # return HttpResponse(f'The recipe argument is {recipe}')
    health_quote = ''

    # if recipe not in recipes_and_quotes:
    #     return HttpResponseNotFound('No info')
    
    # health_quote = recipes_and_quotes[recipe]

    try:
        health_quote = recipes_and_quotes[recipe]
        health_quote = f'<h1>{health_quote}</h1>'
        return HttpResponse(health_quote)
    except:
        return HttpResponseNotFound('<h3>No info</h3>')

    
def handle_recipe_with_number(request, recipe):
    health_quote = ''
    # if recipe == 1:
    #     health_quote = 'Start your day with a smoothie'
    # elif recipe == 2:
    #     health_quote = 'Salad is good for your health'
    # else:
    #     return HttpResponseNotFound(f'The recipe {recipe} was not found!!')
    
    # recipe_list = list(recipes_and_quotes.keys())
    # try:
    #     if recipe <= 0 or recipe > len(recipe_list):
    #         raise Exception()
        
    #     selected_recipe = recipe_list[recipe - 1]
    # except:
    #     return HttpResponseNotFound('No info')
    
    # health_quote = recipes_and_quotes[selected_recipe]
    # return HttpResponse(health_quote)

    recipe_list = list(recipes_and_quotes.keys())

    if recipe <= 0 or recipe > len(recipes_and_quotes):
        return HttpResponseNotFound('<h3>No info</h3>')
    
    recipe_name = recipe_list[recipe - 1]

    # redirect_url = f'/recipes/{recipe_name}/'

    redirect_url = reverse('healthy-recipe', args=[recipe_name])
    return HttpResponseRedirect(redirect_url)


def index(request):
    response_data = '<ul>'
    recipe_list = list(recipes_and_quotes.keys())
    for recipe in recipe_list:
        capatilized_recipe = recipe.capitalize()
        response_data += f'<li><a href="{recipe}">{capatilized_recipe}</a></li>'
    response_data += '</ul>'

    return HttpResponse(response_data)