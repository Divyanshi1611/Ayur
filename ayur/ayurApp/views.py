import os
import json
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# In-memory medicine store (for demo; use DB for production)
MEDICINE_STORE = []

@csrf_exempt
def gemini_chat_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")
        try:
            model = genai.GenerativeModel(model_name="gemini-pro")
            prompt = f"""
            As a health assistant, provide information about: {user_message}
            If describing symptoms or health conditions, include:
            1. Common treatments and home remedies
            2. When to see a doctor
            3. Preventive measures

            End the response with:
            ---
            🏥 Need professional help? Consider booking an appointment with a specialist.
            """
            response = model.generate_content(prompt)
            return JsonResponse({"reply": response.text})
        except Exception as e:
            return JsonResponse({"reply": f"Sorry, there was an error connecting to the AI: {str(e)}"})
    return JsonResponse({"reply": "Invalid request."})

@csrf_exempt
def medicine_api(request):
    if request.method == "GET":
        return JsonResponse({"medicines": MEDICINE_STORE})
    elif request.method == "POST":
        data = json.loads(request.body)
        MEDICINE_STORE.append(data)
        return JsonResponse({"status": "success"})
    elif request.method == "DELETE":
        data = json.loads(request.body)
        name = data.get("name")
        MEDICINE_STORE[:] = [m for m in MEDICINE_STORE if m.get("name") != name]
        return JsonResponse({"status": "deleted"})
    return JsonResponse({"status": "invalid request"})

def chat_view(request):
    return render(request, "chatbot/chat.html")
