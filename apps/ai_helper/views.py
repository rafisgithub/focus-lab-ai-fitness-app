import json
from PyPDF2 import PdfReader
from django.shortcuts import render
import openai

from apps.ai_helper.models import SuggestedQuestion, ChatHistory, Resume, CoverLetter
from apps.ai_helper.serializers import SuggestedQuestionSerializer, ChatHistorySerializer, ResumeSerializer, CoverLetterSerializer
from rest_framework.views import APIView
from apps.utils.helpers import success, error
from django.utils import translation
from rest_framework.permissions import IsAuthenticated
from openai import OpenAI


from project import settings
import base64
from django.core.files.base import ContentFile


class SuggestedQuestionAPIView(APIView):

    permission_classes = []

    def get(self, request):
        try:
            lang_code = request.GET.get('lan', 'de')  
            translation.activate(lang_code)

            questions = SuggestedQuestion.objects.all()
            serializer = SuggestedQuestionSerializer(questions, many=True)
            return success(data=serializer.data, message="Suggested questions fetched successfully")
        except Exception as e:
            return error(message="Failed to fetch suggested questions", errors=str(e))



class ChatHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            lang_code = request.GET.get('lan', 'de')  
            translation.activate(lang_code)

            chat_histories = ChatHistory.objects.filter(user=request.user).order_by('-created_at')
            serializer = ChatHistorySerializer(chat_histories, many=True)
            return success(data=serializer.data, message="Chat histories fetched successfully")
        except Exception as e:
            return error(message="Failed to fetch chat histories", errors=str(e))


class ChatsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    openai.api_key = settings.OPENAI_API_KEY

    def post(self, request):
        try:
            question = request.data.get('question')
            # print(question)
            if not question:
                return error(message="Question is required", errors="No question provided")

            # Here you would typically call your AI model to get an answer
            # answer = "This is a mock answer for the question: {}".format(question)

  
            client = OpenAI()
            
            response = client.responses.create(
            model="gpt-3.5-turbo",
            input=question,
        )
           
            answer = response.output[0].content[0].text

            chat_history = ChatHistory.objects.create(
                user=request.user,
                question=question,
                answer=answer
            )

            serializer = ChatHistorySerializer(chat_history)
            return success(data=serializer.data, message="Chat created successfully")

        except Exception as e:
            return error(message="Failed to create chat", errors=str(e))


class CreateResumeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            resume_language = request.data.get('resume_language')
            tailor_documents_voice = request.data.get('tailor_documents_voice')
            gender_language = request.data.get('gender_language')
            complexity = request.data.get('complexity')
            creativity = request.data.get('creativity')

            data = request.data.copy()
            base_64_photo = data.get('profile_photo')

            photo = None
            if base_64_photo:
                format, imgstr = base_64_photo.split(';base64,')
                ext = format.split('/')[-1]
                photo = ContentFile(base64.b64decode(imgstr), name=f"profile_photo.{ext}")

            gpt_input_data = dict(data)
            gpt_input_data.pop('profile_photo', None) 

            if(resume_language == "en"):
                prompt = (
                "You are a professional resume editor specialized in the German local job market. "
                "Given a JSON input containing resume fields, do the following:\n"
                "- DO NOT change the structure or keys of the JSON.\n"
                "- correct spelling, grammar, and sentence construction. and if think need add some context or details, feel free to do so.specifically about column.\n"
                "- Make sure the sentences sound natural and professional for a job in Germany.\n"
                "- keep the text in English.\n"
                "- DO NOT add, remove, or rename any fields.\n"
                "- Return the corrected version with the exact same JSON structure."
                )
            elif(resume_language == "de"):
                prompt = (
                    "Sie sind ein professioneller Lebenslauf-Editor mit Spezialisierung auf den deutschen Arbeitsmarkt. "
                    "Gegeben ist eine JSON-Eingabe mit Lebenslauf-Feldern. Führen Sie bitte Folgendes durch:\n"
                    "- Ändern Sie NICHT die Struktur oder die Schlüssel der JSON.\n"
                    "- Korrigieren Sie NUR Rechtschreibung, Grammatik und Satzbau. Falls es notwendig erscheint, fügen Sie gerne Kontext oder Details hinzu – insbesondere in Bezug auf die jeweilige Spalte.\n"
                    "- Achten Sie darauf, dass die Sätze natürlich und professionell für eine Bewerbung in Deutschland klingen.\n"
                    "- Übersetzen Sie ins Deutsche.\n"
                    "- Fügen Sie KEINE Felder hinzu, entfernen Sie KEINE Felder und benennen Sie KEINE Felder um.\n"
                    "- Geben Sie die korrigierte Version mit exakt derselben JSON-Struktur zurück."
                )

            else:
                return error(message="Invalid resume language", errors="Language not supported")

            if tailor_documents_voice:
                prompt += "- tailor_documents_voice: " + tailor_documents_voice + "\n"
            if gender_language:
                prompt += "- gender_language: " + gender_language + "\n"
            if complexity:
                prompt += "- complexity: " + complexity + "\n"
            if creativity:
                prompt += "- creativity: " + creativity + "\n"

            # return success(prompt, message="Prompt generated successfully")
            client = OpenAI()
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": prompt,
                    },
                    {
                        "role": "user",
                        "content": json.dumps(gpt_input_data)
                    }
                ]
            )

            corrected_data = json.loads(response.choices[0].message.content)

            serializer = ResumeSerializer(data=corrected_data, context={'request': request})
            if serializer.is_valid():
                resume_instance = serializer.save()

                if photo:
                    resume_instance.profile_photo = photo
                    resume_instance.save()

                return success(data=ResumeSerializer(resume_instance).data, message="Resume created successfully")
            else:
                return error(message="Invalid data", errors=serializer.errors)

        except Exception as e:
            return error(message="Failed to create resume", errors=str(e))

class ResumeHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            resumes = Resume.objects.filter(user=request.user).all()
            if not resumes:
                return error(message="No resume found for this user", errors="Resume not found")

            serializer = ResumeSerializer(resumes, many=True)
            return success(data=serializer.data, message="Resumes fetched successfully")
        except Exception as e:
            return error(message="Failed to fetch resume", errors=str(e))
        

class CreateCoverLetterAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
                resume_language = request.data.get('resume_language')
                tailor_documents_voice = request.data.get('tailor_documents_voice')
                gender_language = request.data.get('gender_language')
                complexity = request.data.get('complexity')
                creativity = request.data.get('creativity')
                
                data = request.data.copy()
            
                upload_resume = request.FILES.get('upload_resume')
                # data = dict(data)
                
                data.pop('upload_resume', None)
                # return success(data, message="Data received successfully")
                

                reader = PdfReader(upload_resume)
                text = ""

                for page in reader.pages:
                    text += page.extract_text() + "\n"
                
                if(resume_language == "en"):
                    prompt = (
                        "You are a professional cover letter writer specialized in the German local job market. "
                        "Given a JSON input containing resume fields, do the following:\n"
                        "- Write a cover letter based on the provided information.\n"
                        "- Make sure the sentences sound natural and professional for a job in Germany.\n"
                        "- keep the text in English.\n"
                        "- DO NOT add, remove, or rename any fields.\n"
                        "- Return the cover letter content. and others fields should be same as input JSON.\n"
                        "- This is my Resume content  " + text +  " use these information for writing.cover letter content" + "\n"
                    )
                elif(resume_language == "de"):
                    prompt = (
                        "Sie sind ein professioneller Anschreiben-Schreiber mit Spezialisierung auf den deutschen Arbeitsmarkt. "
                        "Gegeben ist eine JSON-Eingabe mit Lebenslauf-Feldern. Führen Sie bitte Folgendes durch:\n"
                        "- Schreiben Sie ein Anschreiben basierend auf den bereitgestellten Informationen.\n"
                        "- Achten Sie darauf, dass die Sätze natürlich und professionell für eine Bewerbung in Deutschland klingen.\n"
                        "- Übersetzen Sie ins Deutsche.\n"
                        "- Fügen Sie KEINE Felder hinzu, entfernen Sie KEINE Felder und benennen Sie KEINE Felder um.\n"
                        "- Geben Sie den Inhalt des Anschreibens zurück. und andere Felder sollten gleich wie die Eingabe-JSON sein.\n"
                        "- Dies ist mein Lebenslauf-Inhalt " + text + " verwenden Sie diese Informationen zum Schreiben des Anschreibens.\n")

                else:
                    return error(message="Invalid resume language", errors="Language not supported")
                
                
                if tailor_documents_voice:
                    prompt += "- tailor_documents_voice: " + tailor_documents_voice + "\n"
                    prompt += "- gender_language: " + gender_language + "\n"
                    prompt += "- complexity: " + complexity + "\n"
                    prompt += "- creativity: " + creativity + "\n"
                # return success(prompt, message="Prompt generated successfully")

                client = OpenAI()
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": prompt,
                        },
                        {
                            "role": "user",
                            "content": text
                        }
                    ]
                )
                resume_content = response.choices[0].message.content
                data['resume_content'] = resume_content
                # return success(data, message="Cover letter content generated successfully")

                serializer = CoverLetterSerializer(data=data)
                if serializer.is_valid():
                    serializer.save(user=request.user)
                    return success(data=serializer.data, message="Cover letter created successfully")
                else:
                    return error(message="Invalid data", errors=serializer.errors)
        except Exception as e:
                return error(message="Failed to create cover letter", errors=str(e))
    

class CoverLetterHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            cover_letters = CoverLetter.objects.filter(user=request.user).all()
            if not cover_letters:
                return error(message="No cover letter found for this user", errors="Cover letter not found")

            serializer = CoverLetterSerializer(cover_letters, many=True)
            return success(data=serializer.data, message="Cover letters fetched successfully")
        except Exception as e:
            return error(message="Failed to fetch cover letters", errors=str(e))