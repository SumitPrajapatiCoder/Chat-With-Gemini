import requests
from django.shortcuts import render
from .models import ChatMessage
from django.http import HttpResponse
import json
from django.utils.timezone import localtime
from django.shortcuts import redirect
from .models import ChatMessage
from django.conf import settings
import markdown 

API_KEY=settings.GEMINI_API_TOKEN

MODEL_OPTIONS = {
    "gemini-2.0-flash": "models/gemini-1.5-flash",
}


def chat_view(request):
    error_message = ""
    prompt = ""
    response_text = ""
    model_choice = ""
    timestamp = ""
    response_time = ""

    if request.method == "POST":
        prompt = request.POST.get("prompt")
        model_choice = request.POST.get("model")
        model_api = MODEL_OPTIONS.get(model_choice, "models/gemini-1.5-flash")
        timestamp = localtime().strftime("%I:%M %p")

        formatted_prompt = f"""
Please answer the following question in a structured, readable, and professional format. 
Use:
- Headings
- Bullet points or numbered lists
- Bold text for important concepts
- Line breaks for clarity

Question: {prompt}
"""

        url = f"https://generativelanguage.googleapis.com/v1beta/{model_api}:generateContent?key={API_KEY}"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [{"parts": [{"text": formatted_prompt}]}]
        }

        try:
            res = requests.post(url, headers=headers, json=data)
            result = res.json()

            if "candidates" in result:
                raw_text = result['candidates'][0]['content']['parts'][0]['text']
                response_text = markdown.markdown(raw_text)
                response_time = localtime().strftime("%I:%M %p")
                ChatMessage.objects.create(
                    prompt=prompt,
                    response=response_text,
                    model_name=model_choice
                )
            else:
                error_message = result.get("error", {}).get("message", "Unknown error occurred.")
                response_text = "[Error from Gemini API] " + error_message

        except Exception as e:
            error_message = str(e)
            response_text = "[Request Error] " + error_message

        return redirect('chat')

    history = ChatMessage.objects.order_by('timestamp')
    
    return render(request, "chat/chat.html", {
        "prompt": "",
        "response": "",
        "model_choice": "",
        "models": MODEL_OPTIONS,
        "timestamp": "",
        "response_time": "",
        "history": history,
        "error": ""
    })



def download_txt(request):
    messages = ChatMessage.objects.all().order_by('timestamp')
    content = "\n\n".join([
        f"🕒 {localtime(msg.timestamp).strftime('%I:%M %p')}\nUser: {msg.prompt}\nGemini: {msg.response}"
        for msg in messages
    ])
    return HttpResponse(
        content,
        content_type='text/plain',
        headers={'Content-Disposition': 'attachment; filename="chat_history.txt"'}
    )


def clear_chat(request):
    ChatMessage.objects.all().delete()
    return redirect('chat')


