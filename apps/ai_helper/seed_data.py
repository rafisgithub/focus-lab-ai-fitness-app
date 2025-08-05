"""Module for seeding suggested questions related to AI CV, resume, and cover letter building."""

from apps.ai_helper.models import SuggestedQuestion, ChatHistory

def seed_suggested_questions():

    """Seed suggested questions related to AI CV, resume, and cover letter building."""

    questions_data = [
        {
            "question_en": "How can I improve my resume?",
            "question_de": "Wie kann ich meinen Lebenslauf verbessern?",
        },
        {
            "question_en": "What should I include in a cover letter?",
            "question_de": "Was sollte ich in ein Bewerbungsschreiben aufnehmen?",
        },
        {
            "question_en": "How do I tailor my CV for a specific job?",
            "question_de": "Wie passe ich meinen Lebenslauf für eine bestimmte Stelle an?",
        },
        {
            "question_en": "What are some common CV mistakes to avoid?",
            "question_de": "Welche häufigen Fehler sollte ich in meinem Lebenslauf vermeiden?",
        },
        {
            "question_en": "How can I make my cover letter stand out?",
            "question_de": "Wie kann ich mein Bewerbungsschreiben hervorheben?",
        },
        {
            "question_en": "What are some common cover letter mistakes?",
            "question_de": "Welche häufigen Fehler sollte ich in meinem Bewerbungsschreiben vermeiden?",
        }
    ]

    for item in questions_data:

        SuggestedQuestion.objects.create(
            question_en=item["question_en"],
            question_de=item["question_de"]

        )

def seed_chat_history():

    """Seed chat history for AI helper app."""

    # Example data for chat history
    chat_history_data = [
        {
            "user_id": 2,
            "question_en": "How can I improve my resume?",
            "question_de": "Wie kann ich meinen Lebenslauf verbessern?",
            "answer_en": "You can improve your resume by focusing on relevant experience and skills. Use action verbs and quantify your achievements where possible. Tailor your resume to the job description. Consider using a clean, professional format.",
            "answer_de": "Sie können Ihren Lebenslauf verbessern, indem Sie sich auf relevante Erfahrungen und Fähigkeiten konzentrieren. Verwenden Sie Aktionsverben und quantifizieren Sie Ihre Erfolge, wo immer möglich. Passen Sie Ihren Lebenslauf an die Stellenbeschreibung an. Erwägen Sie die Verwendung eines klaren, professionellen Formats.",
        },
        {
            "user_id": 2,
            "question_en": "What should I include in a cover letter?",
            "question_de": "Was sollte ich in ein Bewerbungsschreiben aufnehmen?",
            "answer_de": "Nennen Sie Ihre Motivation für die Stelle und wie Ihre Fähigkeiten den Anforderungen entsprechen. Heben Sie spezifische Erfahrungen hervor, die Ihre Qualifikationen belegen. Verwenden Sie einen professionellen Ton und Format und halten Sie es prägnant. Stellen Sie sicher, dass das Schreiben an den Personalverantwortlichen gerichtet ist, wenn möglich.",
            "answer_en": "Include your motivation for the job and how your skills match the requirements. Be sure to highlight specific experiences that demonstrate your qualifications. Use a professional tone and format, and keep it concise. Make sure to address the letter to the hiring manager if possible.",
        },
        {
            "user_id": 2,
            "question_en": "How do I tailor my CV for a specific job?",
            "question_de": "Wie passe ich meinen Lebenslauf für eine bestimmte Stelle an?",
            "answer_en": "To tailor your CV, read the job description carefully and identify key skills and experiences that the employer is looking for. Adjust your CV to highlight those aspects, using similar language to that in the job description. Remove any irrelevant information that does not pertain to the job.",
            "answer_de": "Um Ihren Lebenslauf anzupassen, lesen Sie die Stellenbeschreibung sorgfältig durch und identifizieren Sie die wichtigsten Fähigkeiten und Erfahrungen, die der Arbeitgeber sucht. Passen Sie Ihren Lebenslauf an, um diese Aspekte hervorzuheben, und verwenden Sie eine ähnliche Sprache wie in der Stellenbeschreibung. Entfernen Sie alle irrelevanten Informationen, die nicht zur Stelle passen.",
        },
        {
            "user_id": 3,
            "question_en": "How can I improve my resume?",
            "question_de": "Wie kann ich meinen Lebenslauf verbessern?",
            "answer_de": "Sie können Ihren Lebenslauf verbessern, indem Sie sich auf relevante Erfahrungen und Fähigkeiten konzentrieren. Verwenden Sie Aktionsverben und quantifizieren Sie Ihre Erfolge, wo immer möglich. Passen Sie Ihren Lebenslauf an die Stellenbeschreibung an. Erwägen Sie die Verwendung eines klaren, professionellen Formats.",
            "answer_en": "You can improve your resume by focusing on relevant experience and skills. Use action verbs and quantify your achievements where possible. Tailor your resume to the job description. Consider using a clean, professional format.",
        },
        {
            "user_id": 3,
            "question_en": "What should I include in a cover letter?",
            "question_de": "Was sollte ich in ein Anschreiben aufnehmen?",
            "answer_en": "Include your motivation for the job and how your skills match the requirements. Be sure to highlight specific experiences that demonstrate your qualifications. Use a professional tone and format, and keep it concise. Make sure to address the letter to the hiring manager if possible.",
            "answer_de": "Fügen Sie Ihre Motivation für die Stelle und die Übereinstimmung Ihrer Fähigkeiten mit den Anforderungen hinzu. Heben Sie spezifische Erfahrungen hervor, die Ihre Qualifikationen belegen. Verwenden Sie einen professionellen Ton und ein professionelles Format und halten Sie es prägnant. Stellen Sie sicher, dass das Schreiben, wenn möglich, an den Personalverantwortlichen gerichtet ist.",
        },
        {
            "user_id": 3,
            "question_en": "How do I tailor my CV for a specific job?",
            "question_de": "Wie passe ich meinen Lebenslauf für eine bestimmte Stelle an?",
            "answer_en": "To tailor your CV, read the job description carefully and identify key skills and experiences that the employer is looking for. Adjust your CV to highlight those aspects, using similar language to that in the job description. Remove any irrelevant information that does not pertain to the job.",
            "answer_de": "Um Ihren Lebenslauf anzupassen, lesen Sie die Stellenbeschreibung sorgfältig durch und identifizieren Sie die wichtigsten Fähigkeiten und Erfahrungen, die der Arbeitgeber sucht. Passen Sie Ihren Lebenslauf an, um diese Aspekte hervorzuheben, und verwenden Sie eine ähnliche Sprache wie in der Stellenbeschreibung. Entfernen Sie alle irrelevanten Informationen, die nicht zur Stelle passen.",
        },
        {
            "user_id": 4,
            "question_en": "How can I improve my resume?",
            "question_de": "Wie kann ich meinen Lebenslauf verbessern?",
            "answer_en": "You can improve your resume by focusing on relevant experience and skills. Use action verbs and quantify your achievements where possible. Tailor your resume to the job description. Consider using a clean, professional format.",
            "answer_de": "Sie können Ihren Lebenslauf verbessern, indem Sie sich auf relevante Erfahrungen und Fähigkeiten konzentrieren. Verwenden Sie Aktionsverben und quantifizieren Sie Ihre Erfolge, wo immer möglich. Passen Sie Ihren Lebenslauf an die Stellenbeschreibung an. Erwägen Sie die Verwendung eines klaren, professionellen Formats.",
        },
        {
            "user_id": 4,
            "question_en": "What should I include in a cover letter?",
            "question_de": "Was sollte ich in ein Bewerbungsschreiben aufnehmen?",
            "answer_de": "Nennen Sie Ihre Motivation für die Stelle und wie Ihre Fähigkeiten den Anforderungen entsprechen. Heben Sie spezifische Erfahrungen hervor, die Ihre Qualifikationen belegen. Verwenden Sie einen professionellen Ton und Format und halten Sie es prägnant. Stellen Sie sicher, dass das Schreiben an den Personalverantwortlichen gerichtet ist, wenn möglich.",
            "answer_en": "Include your motivation for the job and how your skills match the requirements. Be sure to highlight specific experiences that demonstrate your qualifications. Use a professional tone and format, and keep it concise. Make sure to address the letter to the hiring manager if possible.",
        },
        {
            "user_id": 4,
            "question_en": "How do I tailor my CV for a specific job?",
            "question_de": "Wie passe ich meinen Lebenslauf für eine bestimmte Stelle an?",
            "answer_en": "To tailor your CV, read the job description carefully and identify key skills and experiences that the employer is looking for. Adjust your CV to highlight those aspects, using similar language to that in the job description. Remove any irrelevant information that does not pertain to the job.",
            "answer_de": "Um Ihren Lebenslauf anzupassen, lesen Sie die Stellenbeschreibung sorgfältig durch und identifizieren Sie die wichtigsten Fähigkeiten und Erfahrungen, die der Arbeitgeber sucht. Passen Sie Ihren Lebenslauf an, um diese Aspekte hervorzuheben, und verwenden Sie eine ähnliche Sprache wie in der Stellenbeschreibung. Entfernen Sie alle irrelevanten Informationen, die nicht zur Stelle passen.",
        },
        {
            "user_id": 5,
            "question_en": "How can I improve my resume?",
            "question_de": "Wie kann ich meinen Lebenslauf verbessern?",
            "answer_en": "You can improve your resume by focusing on relevant experience and skills. Use action verbs and quantify your achievements where possible. Tailor your resume to the job description. Consider using a clean, professional format.",
            "answer_de": "Sie können Ihren Lebenslauf verbessern, indem Sie sich auf relevante Erfahrungen und Fähigkeiten konzentrieren. Verwenden Sie Aktionsverben und quantifizieren Sie Ihre Erfolge, wo immer dies möglich ist. Passen Sie Ihren Lebenslauf an die Stellenbeschreibung an. Erwägen Sie die Verwendung eines klaren, professionellen Formats.",
        },
        {
            "user_id": 5,
            "question_en": "What should I include in a cover letter?",
            "question_de": "Was sollte ich in ein Bewerbungsschreiben aufnehmen?",
            "answer_en": "Include your motivation for the job and how your skills match the requirements. Be sure to highlight specific experiences that demonstrate your qualifications. Use a professional tone and format, and keep it concise. Make sure to address the letter to the hiring manager if possible.",
            "answer_de": "Nennen Sie Ihre Motivation für die Stelle und wie Ihre Fähigkeiten den Anforderungen entsprechen. Heben Sie spezifische Erfahrungen hervor, die Ihre Qualifikationen belegen. Verwenden Sie einen professionellen Ton und Format und halten Sie es prägnant. Stellen Sie sicher, dass das Schreiben an den Personalverantwortlichen gerichtet ist, wenn möglich.",
        },
        {
            "user_id": 5,
            "question_en": "How do I tailor my CV for a specific job?",
            "question_de": "Wie passe ich meinen Lebenslauf für eine bestimmte Stelle an?",
            "answer_de": "Um Ihren Lebenslauf anzupassen, lesen Sie die Stellenbeschreibung sorgfältig durch und identifizieren Sie die wichtigsten Fähigkeiten und Erfahrungen, die der Arbeitgeber sucht. Passen Sie Ihren Lebenslauf an, um diese Aspekte hervorzuheben, und verwenden Sie eine ähnliche Sprache wie in der Stellenbeschreibung. Entfernen Sie alle irrelevanten Informationen, die nicht zur Stelle passen.",
            "answer_en": "To tailor your CV, read the job description carefully and identify key skills and experiences that the employer is looking for. Adjust your CV to highlight those aspects, using similar language to that in the job description. Remove any irrelevant information that does not pertain to the job.",
        },
    ]

    for item in chat_history_data:
        ChatHistory.objects.create(
            user_id=item["user_id"],
            question_en=item["question_en"],
            question_de=item["question_de"],
            answer_en=item["answer_en"],
            answer_de=item["answer_de"]
        )