import os
import google.generativeai as genai
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from chatbot1.tts.tts import text_to_speech  # Import your TTS function

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Configure the AI model
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 256,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
    system_instruction="Weather Assistant that replies only about weather-related queries in 20 words."
)
chat_session = model.start_chat(history=[])

@csrf_exempt  # Disable CSRF for now (better to handle in frontend later)
def chat(request):
    if request.method == "GET":
        return render(request, 'chatbot1/chat.html')  # Render chatbot page for GET requests

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")

            # Check if message is empty
            if not user_message.strip():
                return JsonResponse({"error": "Empty message"}, status=400)

            # Get AI response
            try:
                response = chat_session.send_message(user_message)
                bot_reply = response.text if response else "No response from AI"
            except Exception as ai_error:
                return JsonResponse({"error": f"AI Error: {str(ai_error)}"}, status=500)

            # Convert text to speech
            try:
                audio_path = text_to_speech(bot_reply)
                if not audio_path:
                    return JsonResponse({"error": "TTS failed"}, status=500)
            except Exception as tts_error:
                return JsonResponse({"error": f"TTS Error: {str(tts_error)}"}, status=500)

            # Construct static file path
            audio_url = "/static/response.mp3"
            return JsonResponse({"response": bot_reply, "audio": audio_url})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)