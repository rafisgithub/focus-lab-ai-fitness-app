
from apps.contacts.models import Contact


def seed_contacts():

    contacts_data = [
        {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone_number': '1234567890',
            'message': 'Hello, this is a test message.',
            'agree_terms': True,
            'created_at': '2023-10-01T12:00:00Z',
            'updated_at': '2023-10-01T12:00:00Z'
        },
        {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'j ane.smith@example.com',
            'phone_number': '0987654321',
            'message': 'Hi, I would like to know more about your services.',
            'agree_terms': True,
            'created_at': '2023-10-01T12:00:00Z',
            'updated_at': '2023-10-01T12:00:00Z'
        },
        {
            'first_name': 'Alice',
            'last_name': 'Johnson',
            'email': 'alice.johnson@example.com',
            'phone_number': '5551234567',
            'message': 'I have a question about my order.',
            'agree_terms': True,
            'created_at': '2023-10-01T12:00:00Z',
            'updated_at': '2023-10-01T12:00:00Z'
        },
        {
            'first_name': 'Bob',
            'last_name': 'Brown',
            'email': 'bob.brown@example.com',
            'phone_number': '5559876543',
            'message': 'I would like to provide some feedback.',
            'agree_terms': True,
            'created_at': '2023-10-01T12:00:00Z',
            'updated_at': '2023-10-01T12:00:00Z'
        },
        {
            'first_name': 'Charlie',
            'last_name': 'Davis',
            'email': 'charlie.davis@example.com',
            'phone_number': '5556543210',
            'message': 'Can you assist me with my account?',
            'agree_terms': True,
            'created_at': '2023-10-01T12:00:00Z',
            'updated_at': '2023-10-01T12:00:00Z'
        }
    ]


    for item in contacts_data:
        Contact.objects.create(
            first_name=item['first_name'],
            last_name=item['last_name'],
            email=item['email'],
            phone_number=item['phone_number'],
            message=item['message'],
            agree_terms=item['agree_terms']
        )