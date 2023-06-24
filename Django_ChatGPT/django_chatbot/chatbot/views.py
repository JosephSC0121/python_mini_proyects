from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_api_key = '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'
openai.api_key = openai_api_key
def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens = 150,
        n=1,
        stop = None,
        temperature = 0.7,
    )
    answer = response.choices[0].text.strip()

    return answer
# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message =  request.POST.get('message')
        response = 'Aregar key de OPENAI'
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html') 