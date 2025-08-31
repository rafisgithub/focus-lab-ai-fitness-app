from apps.cms.models import FAQ, Page

def seed_page():
    pages = [
 {
        "title": "Privacy Policy",
        "slug": "privacy-policy",
        "content": "This Privacy Policy explains how we collect, use, and protect your personal information when you interact with our website, mobile application, and services. By using our platform, you acknowledge that you have read and understood the terms outlined in this policy.\n\nWe collect information that you provide voluntarily, such as your name, email address, phone number, or any other details you share during registration, purchases, or inquiries. Additionally, we automatically gather certain data through cookies and analytics tools to improve your experience, such as browser type, device information, and pages visited.\n\nYour personal data is primarily used to provide, improve, and personalize our services. For example, we use your information to process orders, respond to support requests, send updates about our services, and enhance the overall usability of our platform. We may also use anonymized data for research, analysis, and business improvement.\n\nWe prioritize your privacy and implement robust security measures, including encryption, secure servers, and access controls, to protect your information from unauthorized access, alteration, or disclosure. However, no method of online transmission is 100% secure, and we cannot guarantee absolute safety.\n\nWe never sell, rent, or trade your personal data to third parties for marketing purposes. However, we may share your information with trusted service providers or as required by law to comply with legal obligations or protect our rights.\n\nBy continuing to use our platform, you agree to this Privacy Policy. We may update this policy from time to time, and the latest version will always be available on this page. If you have any concerns or questions, please contact our support team for assistance.",
        "type": "privacy_policy",
        "status": True
    },
    {
        "title": "Terms and Conditions",
        "slug": "terms-and-conditions",
        "content": "These Terms and Conditions govern your access to and use of our website, mobile application, and related services. By using our platform, you agree to comply with these terms. Please read them carefully, as they outline your rights, obligations, and the rules that govern your relationship with us.\n\nOur services are intended for lawful use only. You agree not to misuse the platform in any way that could harm other users, disrupt the system, or violate applicable laws. Examples of prohibited activities include hacking, spreading malicious code, or engaging in fraudulent transactions.\n\nAccounts created on our platform are personal to you. You are responsible for maintaining the confidentiality of your login information and for all activities conducted under your account. If you suspect unauthorized use, you must notify us immediately.\n\nWe strive to keep the platform available and secure, but we do not guarantee uninterrupted access or error-free performance. We may modify, update, or discontinue certain features without prior notice to enhance functionality or security.\n\nIntellectual property rights for all content, designs, and materials on our platform belong to us or our licensors. Unauthorized reproduction, distribution, or modification of any content is strictly prohibited without prior written consent.\n\nOur liability for any damages is limited to the maximum extent permitted by law. We are not responsible for indirect, incidental, or consequential damages resulting from the use or inability to use our services.\n\nWe reserve the right to update these Terms and Conditions at any time. Changes will be effective upon posting, and continued use of the platform after changes means you accept the updated terms. If you disagree with these terms, you must stop using our services immediately.",
        "type": "terms_and_conditions",
        "status": True
    },
    {
        "title": "Cookie Policy",
        "slug": "cookie-policy",
        "content": "This Cookie Policy explains how our website uses cookies and similar technologies to enhance your browsing experience. By accessing or using our platform, you agree to the use of cookies as described in this policy.\n\nCookies are small text files stored on your device that help us recognize your preferences, understand how you interact with our site, and deliver a more personalized experience. We use different types of cookies, including:\n\n- Essential cookies: These are necessary for the website to function correctly, such as maintaining your session or processing transactions.\n- Performance cookies: These collect information about how you use our site, helping us improve performance and usability.\n- Functional cookies: These remember your settings and preferences to make your experience more convenient.\n- Advertising cookies: These help us deliver relevant ads based on your browsing history and preferences.\n\nYou have the right to control and manage cookies through your browser settings. You can choose to block or delete cookies at any time; however, this may affect the performance and functionality of our site. Detailed instructions for managing cookies can typically be found in your browser’s help section.\n\nWe also work with trusted third-party partners for analytics and advertising. These partners may set cookies to gather information about your activities on our site and across other platforms to provide targeted advertising and measure its effectiveness.\n\nOur use of cookies helps us enhance security, personalize content, and analyze trends to improve our services. We do not store sensitive personal information in cookies, nor do we sell this information to third parties.\n\nThis policy may be updated periodically to reflect changes in technology, legal requirements, or our business practices. We encourage you to review this page regularly to stay informed about how we use cookies and protect your data.",
        "type": "cookie_policy",
        "status": True
    },
    {
        "title": "Imprint",
        "slug": "imprint",
        "content": "This Imprint provides legal information about our company, including address, contact details, and responsible representatives.",
        "type": "imprint",
        "status": True
    }
]
    for page in pages:
        Page.objects.create(**page)
    print("✅ Pages seeded successfully.")


def seed_faq():
    faqs = [
        {
            "question": "How can I create an account?",
            "answer": "You can create an account by clicking the 'Sign Up' button and filling out the registration form.",
            "status": True
        },
        {
            "question": "How do I reset my password?",
            "answer": "Click on 'Forgot Password' on the login page, then follow the instructions to reset your password.",
            "status": True
        },
        {
            "question": "Can I change my email address?",
            "answer": "Yes, you can update your email in your profile settings under 'Account Information'.",
            "status": True
        },
        {
            "question": "How do I contact support?",
            "answer": "You can reach our support team via the 'Contact Us' page or by emailing support@example.com.",
            "status": True
        },
        {
            "question": "Is my personal information safe?",
            "answer": "Yes, we use industry-standard security measures to protect your data.",
            "status": True
        }
    ]

    for faq in faqs:
        FAQ.objects.create(**faq)

    print("✅ FAQs seeded successfully.")