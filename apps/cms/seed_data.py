from apps.cms.models import (
    Brand,
    Faq,
    Feature,
    GlobalCta,
    HeroSection,
    HowItWork,
    HowItWorkFeature,
    InterviewCoachSection,
    Testimonial,
    Benefit,
    Footer,
    UpcomingFeatureInterestedUser,
)
from django.db import connection
from apps.cms.models import Page


def seed_brands():
    table_name = Brand._meta.db_table

    # Use DELETE for SQLite
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM "{table_name}";')

    # Reset auto-increment for SQLite
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{table_name}";')

    brand_data = [
        {"name_en": "Samsung", "name_de": "Samsung", "logo": "brands/b1.png"},
        {"name_en": "Apple", "name_de": "Apfel", "logo": "brands/b2.png"},
        {"name_en": "Sony", "name_de": "Sony", "logo": "brands/b3.png"},
        {"name_en": "Walton", "name_de": "Walton", "logo": "brands/b1.png"},
        {"name_en": "Walmart", "name_de": "Warenmarkt", "logo": "brands/b2.png"},
        {"name_en": "Google", "name_de": "Gurgeln", "logo": "brands/b3.png"},
        {"name_en": "Amazon", "name_de": "Amazonas", "logo": "brands/b1.png"},
        {"name_en": "Dell", "name_de": "Tal", "logo": "brands/b2.png"},
        {"name_en": "Bose", "name_de": "Böse", "logo": "brands/b3.png"},
        {"name_en": "LG", "name_de": "LG", "logo": "brands/b1.png"},
        {"name_en": "Microsoft", "name_de": "Mikrosoft", "logo": "brands/b2.png"},
        {"name_en": "Facebook", "name_de": "Gesichtsbuch", "logo": "brands/b3.png"},
    ]

    for item in brand_data:
        Brand.objects.create(**item)

    print("✅ Brands seeded successfully.")


def seed_features():
    table_name = Feature._meta.db_table

    # Use DELETE for SQLite
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM "{table_name}";')

    # Reset auto-increment for SQLite
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{table_name}";')

    feature_data = [
        {
            "title_en": "AI-Powered CV Builder",
            "title_de": "KI-gestützter Lebenslauf-Generator",
            "short_description_en": "Create a professional, job-winning CV in minutes with AI guidance—personalized for your career goals and tailored to the job market.",
            "short_description_de": "Erstellen Sie in wenigen Minuten einen professionellen, überzeugenden Lebenslauf mit KI-Unterstützung – individuell auf Ihre Karriereziele und den Arbeitsmarkt zugeschnitten.",
            "logo": "features/1.png",
        },
        {
            "title_en": "ATS-Optimized Resumes",
            "title_de": "ATS-optimierte Lebensläufe",
            "short_description_en": "Ensure your CV passes Applicant Tracking Systems (ATS) with AI-driven keyword optimization.",
            "short_description_de": "Stellen Sie sicher, dass Ihr Lebenslauf von Bewerbermanagementsystemen (ATS) erkannt wird – dank KI-gestützter Keyword-Optimierung.",
            "logo": "features/2.png",
        },
        {
            "title_en": "24/7 Customer Support",
            "title_de": "Kundensupport rund um die Uhr",
            "short_description_en": "Get instant help from our support team anytime you need assistance.",
            "short_description_de": "Erhalten Sie jederzeit sofortige Hilfe von unserem Support-Team, wann immer Sie Unterstützung benötigen.",
            "logo": "features/3.png",
        },
        {
            "title_en": "Professional Templates",
            "title_de": "Professionelle Vorlagen",
            "short_description_en": "Choose from industry-specific CV templates designed by career experts.",
            "short_description_de": "Wählen Sie aus branchenspezifischen Lebenslaufvorlagen, die von Karriereexperten entworfen wurden.",
            "logo": "features/4.png",
        },
        {
            "title_en": "Real-Time Editing & Feedback",
            "title_de": "Bearbeitung & Feedback in Echtzeit",
            "short_description_en": "Get AI-powered suggestions to improve your CV as you write.",
            "short_description_de": "Erhalten Sie KI-gestützte Verbesserungsvorschläge für Ihren Lebenslauf – direkt beim Schreiben.",
            "logo": "features/5.png",
        },
        {
            "title_en": "Secure Cloud Storage",
            "title_de": "Sichere Cloud-Speicherung",
            "short_description_en": "Your CVs are safely stored and accessible anytime, anywhere.",
            "short_description_de": "Ihre Lebensläufe werden sicher in der Cloud gespeichert und sind jederzeit und überall zugänglich.",
            "logo": "features/6.png",
        },
    ]

    for item in feature_data:
        Feature.objects.create(**item)

    print("✅ Features seeded successfully.")


def seed_testimonials():
    table_name = Testimonial._meta.db_table

    # Use DELETE for SQLite
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM "{table_name}";')

    # Reset auto-increment for SQLite
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{table_name}";')

        testimonial_data = [
            {
                "name_en": "John Doe",
                "name_de": "Johann Doe",
                "profession_en": "Software Engineer",
                "profession_de": "Softwareentwickler",
                "rating": 5,
                "comment_en": "This service is fantastic! Highly recommend it.",
                "comment_de": "Dieser Service ist fantastisch! Ich kann ihn nur wärmstens empfehlen.",
                "user_image": "testimonials/1.jpg",
            },
            {
                "name_en": "Jane Smith",
                "name_de": "Johanna Schmidt",
                "profession_en": "Product Manager",
                "profession_de": "Produktmanagerin",
                "rating": 4,
                "comment_en": "Very helpful, but could use some improvements.",
                "comment_de": "Sehr hilfreich, aber es gibt noch Verbesserungspotenzial.",
                "user_image": "testimonials/2.jpg",
            },
            {
                "name_en": "Alice Johnson",
                "name_de": "Alice Johannsen",
                "profession_en": "UX Designer",
                "profession_de": "UX-Designerin",
                "rating": 5,
                "comment_en": "Absolutely love it! Made my life so much easier.",
                "comment_de": "Ich liebe es absolut! Es hat mein Leben so viel einfacher gemacht.",
                "user_image": "testimonials/3.jpg",
            },
            {
                "name_en": "Bob Brown",
                "name_de": "Robert Braun",
                "profession_en": "Data Scientist",
                "profession_de": "Datenwissenschaftler",
                "rating": 5,
                "comment_en": "Incredible tool for building my CV!",
                "comment_de": "Ein unglaubliches Tool zum Erstellen meines Lebenslaufs!",
                "user_image": "testimonials/4.jpg",
            },
            {
                "name_en": "Charlie Davis",
                "name_de": "Karl Davis",
                "profession_en": "Marketing Specialist",
                "profession_de": "Marketing-Spezialist",
                "rating": 4,
                "comment_en": "Great experience overall, but I wish there were more templates.",
                "comment_de": "Insgesamt eine tolle Erfahrung, aber ich wünschte, es gäbe mehr Vorlagen.",
                "user_image": "testimonials/5.jpg",
            },
        ]

    for item in testimonial_data:
        Testimonial.objects.create(**item)

    print("✅ Testimonials seeded successfully.")


def seed_benefits():
    table_name = Benefit._meta.db_table

    # Use DELETE for SQLite
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM "{table_name}";')

    # Reset auto-increment for SQLite
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{table_name}";')

    benefit_data = [
        {
            "title_de": "Sofortige Lebenslauf-Erstellung",
            "title_en": "Instant CV Creation",
            "sub_title_de": "Erstellen Sie Ihren Lebenslauf in Minuten mit KI-Unterstützung.",
            "sub_title_en": "Create your CV in minutes with AI assistance.",
            "logo": "benefits/1.png",
        },
        {
            "title_de": "Maßgeschneiderte Bewerbungen",
            "title_en": "Tailored Job Applications",
            "sub_title_de": "Erhalten Sie personalisierte Vorschläge für Bewerbungen.",
            "sub_title_en": "Get personalized job application suggestions.",
            "logo": "benefits/2.png",
        },
        {
            "title_de": "Expert Career Advice",
            "title_en": "Expert Career Advice",
            "sub_title_de": "Zugang zu professioneller Karriereberatung und Tipps.",
            "sub_title_en": "Access professional career guidance and tips.",
            "logo": "benefits/3.png",
        },
        {
            "title_de": "Einblicke in den Arbeitsmarkt",
            "title_en": "Job Market Insights",
            "sub_title_de": "Bleiben Sie über die neuesten Trends auf dem Arbeitsmarkt informiert.",
            "sub_title_en": "Stay updated with the latest job market trends.",
            "logo": "benefits/4.png",
        },
        {
            "title_de": "Networking Opportunities",
            "title_en": "Networking Opportunities",
            "sub_title_de": "Connect with industry professionals and recruiters.",
            "sub_title_en": "Connect with industry professionals and recruiters.",
            "logo": "benefits/5.png",
        },
        {
            "title_de": "Sichere Datenverarbeitung",
            "title_en": "Secure Data Protection",
            "sub_title_de": "Ihre Daten sind bei uns sicher und geschützt.",
            "sub_title_en": "Your data is safe and secure with us.",
            "logo": "benefits/6.png",
        },
        {
            "title_de": "Mobile-Friendly",
            "title_en": "Mobile-Friendly",
            "sub_title_de": "Greifen Sie unterwegs auf Ihren Lebenslauf und Ihre Bewerbungen zu.",
            "sub_title_en": "Access your CV and job applications on the go.",
            "logo": "benefits/7.png",
        },
        {
            "title_de": "Mehrsprachige Unterstützung",
            "title_en": "Multi-Language Support",
            "sub_title_de": "Erstellen Sie Lebensläufe in mehreren Sprachen.",
            "sub_title_en": "Create CVs in multiple languages.",
            "logo": "benefits/8.png",
        },
        {
            "title_de": "Anpassbare Vorlagen",
            "title_en": "Customizable Templates",
            "sub_title_de": "Wählen Sie aus einer Vielzahl von professionellen Vorlagen.",
            "sub_title_en": "Choose from a variety of professional templates.",
            "logo": "benefits/9.png",
        },
        {
            "title_de": "Echtzeit-Zusammenarbeit",
            "title_en": "Real-Time Collaboration",
            "sub_title_de": "Arbeiten Sie in Echtzeit mit anderen an Ihrem Lebenslauf.",
            "sub_title_en": "Work with others on your CV in real-time.",
            "logo": "benefits/10.png",
        },
    ]

    for item in benefit_data:
        Benefit.objects.create(**item)

    print("✅ Benefits seeded successfully.")


def seed_faqs():
    table_name = Faq._meta.db_table
    # Use DELETE for SQLite
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM "{table_name}";')
    # Reset auto-increment for SQLite
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{table_name}";')
        cursor.execute(f"VACUUM;")

    faq_data = [
        {
            "question_en": "How do I create a CV?",
            "question_de": "Wie erstelle ich einen Lebenslauf?",
            "answer_en": "<div>To create a CV, simply sign up, choose a template, and fill in your details. Our AI will assist you in crafting a professional CV.</div>",
            "answer_de": "<div>Um einen Lebenslauf zu erstellen, melden Sie sich einfach an, wählen Sie eine Vorlage aus und füllen Sie Ihre Daten aus. Unsere KI hilft Ihnen dabei, einen professionellen Lebenslauf zu erstellen.</div>",
            "is_active": True,
        },
        {
            "question_en": "How does the ‘Industry–Tailored CV’ feature work?",
            "question_de": "Wie funktioniert die Funktion „Branchenangepasster Lebenslauf“?",
            "answer_en": "<div>This feature analyzes job descriptions and tailors your CV to highlight the most relevant skills and experiences. It ensures that your application stands out to potential employers.</div>",
            "answer_de": "<div>Diese Funktion analysiert Stellenbeschreibungen und passt Ihren Lebenslauf an, um die relevantesten Fähigkeiten und Erfahrungen hervorzuheben. So fällt Ihre Bewerbung positiv auf.</div>",
            "is_active": True,
        },
        {
            "question_en": "Can I download my CV in different formats?",
            "question_de": "Kann ich meinen Lebenslauf in verschiedenen Formaten herunterladen?",
            "answer_en": "<div>Yes, you can download your CV in PDF, Word, and plain text formats. This allows you to use your CV across various platforms and applications.</div>",
            "answer_de": "<div>Ja, Sie können Ihren Lebenslauf in PDF-, Word- und Textformaten herunterladen. So können Sie ihn auf verschiedenen Plattformen und Anwendungen verwenden.</div>",
            "is_active": True,
        },
        {
            "question_en": "Is my data secure?",
            "question_de": "Sind meine Daten sicher?",
            "answer_en": "<div>Absolutely! We use industry-standard encryption to protect your data. Your CVs are stored securely and are only accessible by you.</div>",
            "answer_de": "<div>Absolut! Wir verwenden branchenübliche Verschlüsselung, um Ihre Daten zu schützen. Ihre Lebensläufe werden sicher gespeichert und sind nur für Sie zugänglich.</div>",
            "is_active": True,
        },
        {
            "question_en": "Do you offer customer support?",
            "question_de": "Bieten Sie Kundensupport an?",
            "answer_en": "<div>Yes, we provide 24/7 customer support to assist you with any questions or issues you may have while using our service.</div>",
            "answer_de": "<div>Ja, wir bieten rund um die Uhr Kundensupport, um Ihnen bei Fragen oder Problemen während der Nutzung unseres Dienstes zu helfen.</div>",
            "is_active": True,
        },
    ]

    for item in faq_data:
        Faq.objects.create(**item)
    print("✅ FAQs seeded successfully.")


def seed_pages():

    pages_data = [
        {
            "title_en": "Terms and Conditions – Clever CV",
            "title_de": "Allgemeine Geschäftsbedingungen – Clever CV",
            "content_en": """
                <p><em>Last updated: May 16, 2025</em></p>
                <p><a href="#">Click here to view our privacy policy. This policy explains how we collect, use, and protect your personal data.</a></p>

                <h2>1. Introduction</h2>
                <p>Welcome to Clever-CV, a platform that enables users to create, optimize, and manage professional resumes, cover letters, and application packages using AI-based tools. These Terms and Conditions govern your use of our website and services.</p>
                <p>By accessing or using Clever-CV, you agree to these Terms.</p>

                <h2>2. Services Provided</h2>
                <p>Clever-CV offers the following services:</p>
                <ul>
                    <li>AI-powered resume and cover letter generation</li>
                    <li>Resume optimization and translation</li>
                    <li>Interview coaching features (beta)</li>
                    <li>Exporting documents in PDF and DOCX</li>
                    <li>Customization and editing tools</li>
                    <li>Optional premium features and downloadable templates</li>
                </ul>

                <h2>3. User Obligations</h2>
                <p>You agree to:</p>
                <ul>
                    <li>Provide accurate and lawful personal information</li>
                    <li>Use the platform solely for personal job application purposes</li>
                    <li>Not upload content that is unlawful, misleading, or infringes on third-party rights</li>
                    <li>Respect the intellectual property rights of Clever-CV and its partners</li>
                </ul>

                <h2>4. Account And Access</h2>
                <ul>
                    <li>You must be at least 16 years old to register.</li>
                    <li>You are responsible for safeguarding your login credentials.</li>
                    <li>Clever-CV reserves the right to suspend or terminate access for violations of these Terms.</li>
                </ul>

                <h2>5. Payment And Subscriptions</h2>
                <ul>
                    <li>Some features are free, while others require a one-time payment or subscription.</li>
                    <li>Payments are handled via Stripe and PayPal.</li>
                    <li>Subscriptions auto-renew unless canceled before the renewal date.</li>
                    <li>Refunds are only issued for technical errors or as required by law.</li>
                </ul>

                <h2>6. Document Storage</h2>
                <p>User files (resumes, templates, etc.) are securely stored on AWS S3.</p>

                <h2>7. Intellectual Property</h2>
                <ul>
                    <li>All templates, designs, and tools are the intellectual property of Clever-CV.</li>
                    <li>You retain rights over your personal information and uploaded content.</li>
                </ul>

                <h2>8. Modifications To The Service</h2>
                <p>Clever-CV may update or modify features, services, and pricing. Major changes will be announced in advance.</p>

                <h2>9. Limitation Of Liability</h2>
                <p>Clever-CV is not responsible for any job outcomes or decisions made by employers. We do not guarantee employment or interview success.</p>

                <h2>10. Governing Law</h2>
                <p>These Terms are governed by the laws of Germany. Any disputes shall be resolved in German courts, unless otherwise required by local laws.</p>

                <h2>11. Contact</h2>
                <p>For questions or support, email us at: <a href="mailto:support@clevercv.ai">support@clevercv.ai</a></p>
            """,
            "content_de": """
                <p><em>Letzte Aktualisierung: 16. Mai 2025</em></p>
                <p><a href="#">Klicken Sie hier, um unsere Datenschutzrichtlinie zu lesen. Diese Richtlinie erklärt, wie wir Ihre persönlichen Daten erfassen, verwenden und schützen.</a></p>

                <h2>1. Einführung</h2>
                <p>Willkommen bei Clever-CV – einer Plattform, mit der Benutzer professionelle Lebensläufe, Anschreiben und Bewerbungsunterlagen mit KI-gestützten Tools erstellen, optimieren und verwalten können. Diese AGB regeln Ihre Nutzung unserer Website und Dienste.</p>
                <p>Durch die Nutzung von Clever-CV stimmen Sie diesen Bedingungen zu.</p>

                <h2>2. Unsere Leistungen</h2>
                <p>Clever-CV bietet folgende Leistungen an:</p>
                <ul>
                    <li>KI-gestützte Erstellung von Lebensläufen und Anschreiben</li>
                    <li>Optimierung und Übersetzung von Lebensläufen</li>
                    <li>Interview-Coaching-Funktionen (Beta-Version)</li>
                    <li>Export von Dokumenten im PDF- und DOCX-Format</li>
                    <li>Anpassungs- und Bearbeitungsfunktionen</li>
                    <li>Optionale Premiumfunktionen und herunterladbare Vorlagen</li>
                </ul>

                <h2>3. Pflichten der Nutzer</h2>
                <p>Sie verpflichten sich:</p>
                <ul>
                    <li>korrekte und rechtmäßige persönliche Angaben zu machen</li>
                    <li>die Plattform ausschließlich für private Bewerbungszwecke zu nutzen</li>
                    <li>keine rechtswidrigen, irreführenden oder rechtsverletzenden Inhalte hochzuladen</li>
                    <li>die geistigen Eigentumsrechte von Clever-CV und Partnern zu respektieren</li>
                </ul>

                <h2>4. Konto und Zugang</h2>
                <ul>
                    <li>Sie müssen mindestens 16 Jahre alt sein, um sich zu registrieren.</li>
                    <li>Sie sind für die Sicherheit Ihrer Zugangsdaten verantwortlich.</li>
                    <li>Clever-CV behält sich das Recht vor, den Zugang bei Verstößen gegen diese Bedingungen zu sperren oder zu beenden.</li>
                </ul>

                <h2>5. Zahlungen und Abonnements</h2>
                <ul>
                    <li>Einige Funktionen sind kostenlos, andere erfordern eine einmalige Zahlung oder ein Abonnement.</li>
                    <li>Zahlungen erfolgen über Stripe oder PayPal.</li>
                    <li>Abonnements verlängern sich automatisch, sofern sie nicht vor dem Verlängerungsdatum gekündigt werden.</li>
                    <li>Rückerstattungen erfolgen nur bei technischen Fehlern oder wenn gesetzlich vorgeschrieben.</li>
                </ul>

                <h2>6. Dokumentenspeicherung</h2>
                <p>Benutzerdokumente (Lebensläufe, Vorlagen usw.) werden sicher auf AWS S3 gespeichert.</p>

                <h2>7. Geistiges Eigentum</h2>
                <ul>
                    <li>Alle Vorlagen, Designs und Tools sind geistiges Eigentum von Clever-CV.</li>
                    <li>Sie behalten die Rechte an Ihren persönlichen Informationen und hochgeladenen Inhalten.</li>
                </ul>

                <h2>8. Änderungen am Dienst</h2>
                <p>Clever-CV kann Funktionen, Dienste und Preise aktualisieren oder ändern. Wichtige Änderungen werden im Voraus angekündigt.</p>

                <h2>9. Haftungsbeschränkung</h2>
                <p>Clever-CV übernimmt keine Verantwortung für Bewerbungsergebnisse oder Arbeitgeberentscheidungen. Eine Jobgarantie oder Einladung zum Vorstellungsgespräch wird nicht gegeben.</p>

                <h2>10. Anwendbares Recht</h2>
                <p>Diese AGB unterliegen deutschem Recht. Streitigkeiten werden vor deutschen Gerichten geregelt, sofern nicht anders gesetzlich vorgeschrieben.</p>

                <h2>11. Kontakt</h2>
                <p>Bei Fragen oder Supportanfragen schreiben Sie uns an: <a href="mailto:support@clevercv.ai">support@clevercv.ai</a></p>
            """,
            "type": Page.Type.TERMSANDCONDITIONS,
            "is_active": True,
        },
        {
            "title_en": "Privacy Policy – Clever CV",
            "title_de": "Datenschutzrichtlinie – Clever CV",
            "content_en": """
                <p><em>Last updated: May 16, 2025</em></p>
                <p>Clever-CV values your privacy. This policy explains how we collect, use, and protect your personal data.</p>

                <h2>1. Data We Collect</h2>
                <ul>
                    <li>Personal information (name, email, location)</li>
                    <li>Uploaded documents (resumes, cover letters, certificates)</li>
                    <li>Responses in resume questionnaire</li>
                    <li>Payment details (handled securely via Stripe or PayPal)</li>
                    <li>Usage data (analytics, device/browser)</li>
                </ul>

                <h2>2. How We Use Your Data</h2>
                <ul>
                    <li>To generate and optimize resumes and application materials</li>
                    <li>To provide AI-based language improvement and feedback</li>
                    <li>To personalize design and content suggestions</li>
                    <li>To process payments and manage your account</li>
                    <li>To improve our services through analytics</li>
                </ul>

                <h2>3. AI And Third-Party Services</h2>
                <p>We use third-party APIs for AI processing and transcription:</p>
                <ul>
                    <li>OpenAI API for resume writing</li>
                    <li>CloudAI API for interview feedback</li>
                    <li>Google Speech-to-Text API for voice recognition</li>
                    <li>Firebase for user authentication</li>
                    <li>AWS S3 for file storage</li>
                </ul>

                <h2>4. Data Sharing</h2>
                <p>We do not sell your data. Your data may be shared with:</p>
                <ul>
                    <li>Service providers (e.g., hosting, analytics, payments)</li>
                    <li>Legal authorities (if required by law)</li>
                </ul>

                <h2>5. Your Rights (GDPR)</h2>
                <p>You have the right to:</p>
                <ul>
                    <li>Access and download your data</li>
                    <li>Request correction or deletion</li>
                    <li>Withdraw consent</li>
                    <li>File a complaint with a Data Protection Authority</li>
                </ul>

                <h2>6. Cookies And Tracking</h2>
                <p>Clever-CV uses cookies to improve functionality and analytics. You may manage cookie preferences in your browser settings.</p>

                <h2>7. Data Retention</h2>
                <p>Your data will be retained for as long as your account is active or as required by law. Inactive accounts may be purged after 12 months of inactivity.</p>

                <h2>8. Security Measures</h2>
                <p>We implement encryption, firewalls, and secure storage practices to protect your data.</p>

                <h2>9. Policy Updates</h2>
                <p>We may revise this policy. Major changes will be communicated via email or platform notices.</p>

                <h2>10. Contact Us</h2>
                <p>For any data protection inquiries or access requests: <a href="mailto:privacy@clevercv.ai">privacy@clevercv.ai</a></p>
            """,
            "content_de": """
                <p><em>Letzte Aktualisierung: 16. Mai 2025</em></p>
                <p>Clever-CV nimmt den Schutz Ihrer Daten sehr ernst. Diese Richtlinie erklärt, wie wir Ihre persönlichen Daten erfassen, verwenden und schützen.</p>

                <h2>1. Erhobene Daten</h2>
                <ul>
                    <li>Persönliche Informationen (Name, E-Mail, Standort)</li>
                    <li>Hochgeladene Dokumente (Lebensläufe, Anschreiben, Zertifikate)</li>
                    <li>Antworten im Lebenslauf-Fragebogen</li>
                    <li>Zahlungsdaten (sicher verarbeitet über Stripe oder PayPal)</li>
                    <li>Nutzungsdaten (Analysen, Gerät/Browserversion)</li>
                </ul>

                <h2>2. Verwendung der Daten</h2>
                <ul>
                    <li>Zur Erstellung und Optimierung von Lebensläufen und Bewerbungsunterlagen</li>
                    <li>Zur Bereitstellung KI-gestützter Sprachverbesserungen und Feedbacks</li>
                    <li>Zur Personalisierung von Design- und Inhaltsvorschlägen</li>
                    <li>Zur Zahlungsabwicklung und Verwaltung Ihres Kontos</li>
                    <li>Zur Verbesserung unserer Dienste durch Analysefunktionen</li>
                </ul>

                <h2>3. KI- und Drittanbieterdienste</h2>
                <p>Wir verwenden Drittanbieter-APIs für KI-Verarbeitung und Transkription:</p>
                <ul>
                    <li>OpenAI API für das Schreiben von Lebensläufen</li>
                    <li>CloudAI API für Interview-Feedback</li>
                    <li>Google Speech-to-Text API für Spracherkennung</li>
                    <li>Firebase für Benutzer-Authentifizierung</li>
                    <li>AWS S3 für Dateispeicherung</li>
                </ul>

                <h2>4. Datenweitergabe</h2>
                <p>Wir verkaufen Ihre Daten nicht. Ihre Daten können weitergegeben werden an:</p>
                <ul>
                    <li>Dienstleister (z. B. Hosting, Analysen, Zahlungsabwicklung)</li>
                    <li>Gesetzliche Behörden (falls gesetzlich erforderlich)</li>
                </ul>

                <h2>5. Ihre Rechte (DSGVO)</h2>
                <p>Sie haben das Recht auf:</p>
                <ul>
                    <li>Zugang und Download Ihrer Daten</li>
                    <li>Berichtigung oder Löschung verlangen</li>
                    <li>Einwilligung widerrufen</li>
                    <li>Beschwerde bei einer Datenschutzbehörde einreichen</li>
                </ul>

                <h2>6. Cookies und Tracking</h2>
                <p>Clever-CV verwendet Cookies zur Verbesserung der Funktionalität und Analyse. Sie können Ihre Cookie-Einstellungen im Browser verwalten.</p>

                <h2>7. Aufbewahrung von Daten</h2>
                <p>Ihre Daten werden so lange gespeichert, wie Ihr Konto aktiv ist oder gesetzlich erforderlich. Inaktive Konten können nach 12 Monaten gelöscht werden.</p>

                <h2>8. Sicherheitsmaßnahmen</h2>
                <p>Wir setzen Verschlüsselung, Firewalls und sichere Speicherpraktiken ein, um Ihre Daten zu schützen.</p>

                <h2>9. Aktualisierungen der Richtlinie</h2>
                <p>Wir können diese Richtlinie aktualisieren. Größere Änderungen werden per E-Mail oder auf unserer Plattform mitgeteilt.</p>

                <h2>10. Kontakt</h2>
                <p>Bei Datenschutzfragen oder Zugriffsanfragen schreiben Sie uns an: <a href="mailto:privacy@clevercv.ai">privacy@clevercv.ai</a></p>
            """,
            "type": Page.Type.PRIVACYPOLICY,
            "is_active": True,
        },
        {
            "title_en": "Imprint",
            "title_de": "Impressum",
            "content_en": """
            <h2>Company Information</h2>
            <p>Company Name: Clever-CV GmbH<br>
            Address: Example Street 12, 12345 Berlin, Germany<br>
            Phone: +49 30 12345678<br>
            Email: contact@clever-cv.com</p>

            <h2>Legal Representatives</h2>
            <p>Managing Director: John Doe<br>
            Commercial Register: HRB 123456, Berlin<br>
            VAT ID: DE123456789</p>

            <h2>Regulatory Authority</h2>
            <p>Berlin Chamber of Commerce<br>
            Address: Chamber Street 1, 10115 Berlin, Germany</p>

            <h2>Disclaimer</h2>
            <p>The content of this website is for general information purposes only.<br>
            We do not accept liability for the accuracy or completeness of the information.</p>

            <h2>Contact Us</h2>
            <p>If you have any questions or concerns, please contact us at:<br>
            Email: support@clever-cv.com<br>
            Phone: +49 30 12345678</p>
        """,
            "content_de": """
            <h2>Unternehmensinformationen</h2>
            <p>Firmenname: Clever-CV GmbH<br>
            Adresse: Beispielstraße 12, 12345 Berlin, Deutschland<br>
            Telefon: +49 30 12345678<br>
            E-Mail: contact@clever-cv.com</p>

            <h2>Rechtliche Vertreter</h2>
            <p>Geschäftsführer: John Doe<br>
            Handelsregister: HRB 123456, Berlin<br>
            USt-ID: DE123456789</p>

            <h2>Aufsichtsbehörde</h2>
            <p>IHK Berlin<br>
            Adresse: Chamberstraße 1, 10115 Berlin, Deutschland</p>

            <h2>Haftungsausschluss</h2>
            <p>Die Inhalte dieser Website dienen nur zur allgemeinen Information.<br>
            Wir übernehmen keine Haftung für die Richtigkeit oder Vollständigkeit der Informationen.</p>

            <h2>Kontakt</h2>
            <p>Wenn Sie Fragen oder Bedenken haben, kontaktieren Sie uns bitte unter:<br>
            E-Mail: support@clever-cv.com<br>
            Telefon: +49 30 12345678</p>
        """,
            "type": Page.Type.IMPRINT,
            "is_active": True,
        },
    ]

    for item in pages_data:
        Page.objects.create(**item)
    print("✅ Pages seeded successfully.")


def seed_hero_section():

    hero_data = {
        "title_en": "Build Your Perfect Resume Smarter, Faster, with AI.",
        "title_de": "Erstellen Sie Ihren perfekten Lebenslauf intelligenter, schneller, mit KI.",
        "sub_title_en": "Professional resumes made easy — create or upgrade with real-time smart suggestions.",
        "sub_title_de": "Professionelle Lebensläufe leicht gemacht – erstellen oder verbessern Sie Ihren Lebenslauf mit intelligenten Echtzeit-Vorschlägen.",
        "banner": "hero-section/banner.png",
    }

    HeroSection.objects.create(**hero_data)

    print("✅ Hero Section seeded successfully.")


def how_it_work_feature_seed():
    seed_data = [
        {
            "name_en": "AI Resume Builder (Create from zero)",
            "name_de": "KI-Lebenslauf-Generator (Erstellen von Grund auf)",
        },
        {
            "name_en": "AI Resume Optimizer (Upload & improve)",
            "name_de": "KI-Lebenslauf-Optimierer (Hochladen & Verbessern)",
        },
        {
            "name_en": "AI Cover Letter Generator (Create from zero)",
            "name_de": "KI-Anschreiben-Generator (Erstellen von Grund auf)",
        },
        {
            "name_en": "You can also enter a target job title or company to personalize the tone and style of your application.",
            "name_de": "Sie können auch einen gewünschten Jobtitel oder ein Unternehmen eingeben, um den Ton und Stil Ihrer Bewerbung zu personalisieren.",
        },
        {
            "name_en": "Add multiple languages to create localized versions of your resume in seconds.",
            "name_de": "Fügen Sie mehrere Sprachen hinzu, um in Sekundenschnelle lokalisierte Versionen Ihres Lebenslaufs zu erstellen.",
        },
        {
            "name_en": "Customize colors, fonts, and layout",
            "name_de": "Passen Sie Farben, Schriftarten und Layout an",
        },
        {
            "name_en": "Edit any text live",
            "name_de": "Bearbeiten Sie jeden Text live",
        },
        {
            "name_en": "Translate into other languages",
            "name_de": "In andere Sprachen übersetzen",
        },
        {
            "name_en": "Resume",
            "name_de": "Lebenslauf",
        },
        {
            "name_en": "Cover Letter",
            "name_de": "Anschreiben",
        },
        {
            "name_en": "Export in PDF or Word format",
            "name_de": "Export im PDF- oder Word-Format",
        },
    ]

    for item in seed_data:
        HowItWorkFeature.objects.create(**item)

    print("✅ How It Works Features seeded successfully.")


def how_it_work_seed():

    seed_data = [
        {
            "title_en": "Choose Your Path.",
            "title_de": "Wählen Sie Ihren Weg.",
            "sub_title_en": "Start from scratch or upload your existing resume.",
            "sub_title_de": "Starten Sie von Grund auf oder laden Sie Ihren bestehenden Lebenslauf hoch.",
            "short_description_en": "The AI instantly generates a resume and/or cover letter tailored to your industry and the job market. You get 3–5 design variants to choose from each editable.",
            "short_description_de": "Die KI erstellt sofort einen Lebenslauf und/oder ein Anschreiben, das auf Ihre Branche und den Arbeitsmarkt zugeschnitten ist. Sie erhalten 3–5 Designvarianten zur Auswahl, die alle bearbeitet werden können.",
            "side_image": "how-it-works/1.png",
            "features": [1, 2, 3],
        },
        {
            "title_en": "Fill In Your Details.",
            "title_de": "Geben Sie Ihre Details ein.",
            "sub_title_en": "Simple, guided steps tailored to your job goals.",
            "sub_title_de": "Einfache, geführte Schritte, die auf Ihre beruflichen Ziele zugeschnitten sind.",
            "short_description_en": "Fill out a guided form with your work experience, education, and career goals—or let the AI extract this automatically from your uploaded resume.",
            "short_description_de": "Füllen Sie ein geführtes Formular mit Ihren beruflichen Erfahrungen, Ihrer Ausbildung und Ihren Karrierezielen aus – oder lassen Sie die KI dies automatisch aus Ihrem hochgeladenen Lebenslauf extrahieren.",
            "side_image": "how-it-works/2.png",
            "features": [4, 5],
        },
        {
            "title_en": "AI Builds & Designs Your Resume.",
            "title_de": "KI erstellt und gestaltet Ihren Lebenslauf.",
            "sub_title_en": "Watch AI turn your data into a job-winning document.",
            "sub_title_de": "Sehen Sie zu, wie KI Ihre Daten in ein gewinnendes Dokument verwandelt.",
            "short_description_en": "Fill out a guided form with your work experience, education, and career goals—or let the AI extract this automatically from your uploaded resume.",
            "short_description_de": "Füllen Sie ein geführtes Formular mit Ihren beruflichen Erfahrungen, Ihrer Ausbildung und Ihren Karrierezielen aus – oder lassen Sie die KI dies automatisch aus Ihrem hochgeladenen Lebenslauf extrahieren.",
            "side_image": "how-it-works/3.png",
            "features": [7, 8, 9],
        },
        {
            "title_en": "Download your Resume or Cover letter.",
            "title_de": "Laden Sie Ihren Lebenslauf oder Ihr Anschreiben herunter.",
            "sub_title_en": "Export bundle everything into one file.",
            "sub_title_de": "Exportieren Sie alles in eine Datei.",
            "short_description_en": "Once satisfied, download your resume and cover letter in PDF or Word format. You can even generate a complete application package including",
            "short_description_de": "Sobald Sie zufrieden sind, laden Sie Ihren Lebenslauf und Ihr Anschreiben im PDF- oder Word-Format herunter. Sie können sogar ein komplettes Bewerbungspaket erstellen, das",
            "side_image": "how-it-works/4.png",
            "features": [10, 11],
        },
    ]

    for item in seed_data:
        features = item.pop("features")
        obj = HowItWork.objects.create(**item)
        obj.features.set(features)

    print("✅ How It Works seeded successfully.")


def seed_interview_coach_section():
    seed_data = {
        "title_en": "Interview Coach",
        "title_de": "Interview Coach",
        "short_description_en": "Practice with AI-powered mock interviews. Master your interview skills with personalized AI feedback. Get ready for your dream job with realistic practice sessions.",
        "short_description_de": "Üben Sie mit KI-gestützten simulierten Interviews. Verbessern Sie Ihre Interviewfähigkeiten mit personalisiertem KI-Feedback. Bereiten Sie sich auf Ihren Traumjob mit realistischen Übungssitzungen vor.",
    }

    InterviewCoachSection.objects.create(**seed_data)


def seed_footer():
    seed_data = {
        "content_en": "CleverCV is an AI-powered resume and cover letter builder that helps you stand out with confidence. Whether you're starting from scratch or improving an existing CV, our platform gives you step-by-step guidance, smart design suggestions, and powerful language enhancements.",
        "content_de": "CleverCV ist ein KI-gestützter Lebenslauf- und Anschreiben-Generator, der Ihnen hilft, mit Selbstvertrauen aufzufallen. Egal, ob Sie von Grund auf neu beginnen oder einen bestehenden Lebenslauf verbessern möchten, unsere Plattform bietet Ihnen Schritt-für-Schritt-Anleitungen, intelligente Designvorschläge und leistungsstarke Sprachverbesserungen.",
        "copyright_text_en": "© 2025 CleverCV. All rights reserved.",
        "copyright_text_de": "© 2025 CleverCV. Alle Rechte vorbehalten.",
    }

    Footer.objects.create(**seed_data)
    print("✅ Footer seeded successfully.")


def seed_upcoming_feature_interested_user():
    seed_data = [
        {"email": "user1@example.com"},
        {"email": "user2@example.com"},
        {"email": "user3@example.com"},
    ]

    for item in seed_data:
        UpcomingFeatureInterestedUser.objects.create(**item)


def seed_global_cta():
    seed_data = {
        "title_en": "Ready to Land Your Next Job with a Perfect Resume?",
        "title_de": "Bereit, Ihren nächsten Job mit einem perfekten Lebenslauf zu bekommen?",
        "description_en": "Let Clever-CV guide you with expert AI tools — build, improve, and export your resume in minutes.",
        "description_de": "Lassen Sie Clever-CV Sie mit Experten-KI-Tools leiten – erstellen, verbessern und exportieren Sie Ihren Lebenslauf in wenigen Minuten.",
        "button_text_en": "Get Started Now",
        "button_text_de": "Jetzt starten",
    }

    GlobalCta.objects.create(**seed_data)
    print("✅ Global CTA seeded successfully.")