from apps.subscriptions.models import Feature, Package, Subscription
from django.db import connection

def seed_subscription_features():
    table_name = Feature._meta.db_table

    # Use DELETE for SQLite
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM "{table_name}";')

    # Reset auto-increment for SQLite
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{table_name}";')

    
    feature_data = [
        {'name_en': 'Resume Creation','name_de': 'Lebenslauf Erstellung'},
        {'name_en': 'No Watermark','name_de': 'Kein Wasserzeichen'},
        {'name_en': 'Basic Template','name_de': 'Basisvorlage'},
        {'name_en': 'Multilingual','name_de': 'Mehrsprachig'},
        {'name_en': 'Export as PNG','name_de': 'Als PNG exportieren'},
        {'name_en': 'Export as PDF or Word','name_de': 'Als PDF oder Word exportieren'},
        {'name_en': 'Unlimited Resume','name_de': 'Unbegrenzter Lebenslauf'},
        {'name_en': '5 Downloads per Month','name_de': '5 Downloads pro Monat'},
        {'name_en': 'Unlimited Download','name_de': 'Unbegrenzter Download'},
        {'name_en': 'Premium Templates','name_de': 'Premium-Vorlagen'},
        {'name_en': 'AI-generated Cover Letter Tools','name_de': 'KI-generierte Anschreiben-Tools'},
        {'name_en': 'Cover Letter','name_de': 'Anschreiben'},
        {'name_en': 'One-time Export','name_de': 'Einmaliger Export'},

    ]


    for feature in feature_data:
        Feature.objects.create(**feature)
    print(f"Seeded {len(feature_data)} features into the database.")



def seed_subscription_packages():
    table_name = Package._meta.db_table
    # Use DELETE for SQLite
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM "{table_name}";')
# Reset auto-increment for SQLite
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{table_name}";')

    package_data = [
            {
            'name_en': 'Free Plan',
            'name_de': 'Kostenloser Plan',
            # 'stripe_product_id': 'prod_SfL7ICehxZCtyp',
            # 'stripe_price_id': 'price_1Rk1n5PSJG5U2meYIOPrSuZ6',
            'price': 0.00,
            'type': Package.PackageType.MONTHLY,
            'enabled': True,
            'feature_names': ['Resume Creation', 'No Watermark', 'Basic Template']
            
        },
        {
            'name_en': 'Basic Plan',
            'name_de': 'Basisplan',
            # 'stripe_product_id': 'prod_SfL9AD31dLRaTL',
            # 'stripe_price_id': 'price_1RntKgPSJG5U2meYewd6n9lK',
            'price': 4.99,
            'type': Package.PackageType.MONTHLY,
            'enabled': True,
            'feature_names': ['Resume Creation', 'No Watermark', 'Basic Template', 'Multilingual']
        },
        {
            'name_en': 'Pro Plan',
            'name_de': 'Pro-Plan',
            # 'stripe_product_id': 'prod_SfLAwdFiWg1rT2',
            # 'stripe_price_id': 'price_1Rk0TmPSJG5U2meYXLDvlgxW',
            'price': 9.99,
            'type': Package.PackageType.MONTHLY,
            'enabled': True,
            'feature_names': ['Resume Creation', 'No Watermark', 'Basic Template', 'Multilingual']
        },

        {
            'name_en': 'Pay Per Download',
            'name_de': 'Bezahlung pro Download',
            # 'stripe_product_id': 'prod_SfLAsv9HmNylIG',
            # 'stripe_price_id': 'price_1Rk1nmPSJG5U2meYoKXeYdH0',
            'price': 9.99,
            'type': Package.PackageType.PAY_PER_DOWNLOAD,
            'enabled': True,
            'feature_names': ['Resume Creation', 'No Watermark', 'Basic Template']
        }
    ]

    for package_info in package_data:
        feature_names = package_info.pop('feature_names', [])
        
        package = Package.objects.create(**package_info)
        
        features = Feature.objects.filter(name__in=feature_names)
        package.features.set(features)
    
    print(f"Seeded {len(package_data)} packages into the database.")


    subscription_data = [
        {
            'user_id': 3,  # Assuming user with ID 3 exists
            'package_id': 1,  # Assuming package with ID 3 exists
            'stripe_subscription_id': 'sub_1122334455',
            'status': 'pending',
            'start_date': '2023-03-01T00:00:00Z',
            'end_date': '2024-03-01T00:00:00Z'
        },
        {
            'user_id': 4,  # Assuming user with ID 4 exists
            'package_id': 2,  # Assuming package with ID 2 exists
            'stripe_subscription_id': 'sub_5566778899',
            'status': 'cancelled',
            'start_date': '2023-04-01T00:00:00Z',
            'end_date': '2024-04-01T00:00:00Z'
        },
        {
            'user_id': 5,  # Assuming user with ID 5 exists
            'package_id': 3,  # Assuming package with ID 3 exists
            'stripe_subscription_id': 'sub_123123123',
            'status': 'active',
            'start_date': '2023-05-01T00:00:00Z',
            'end_date': '2024-05-01T00:00:00Z'
        },
        {
            'user_id': 6,  # Assuming user with ID 6 exists
            'package_id': 4,  # Assuming package with ID 4 exists
            'stripe_subscription_id': 'sub_456456456',
            'status': 'expired',
            'start_date': '2023-06-01T00:00:00Z',
            'end_date': '2024-06-01T00:00:00Z'
        },
        {
            'user_id': 7,  # Assuming user with ID 7 exists
            'package_id': 1,  # Assuming package with ID 7 exists
            'stripe_subscription_id': 'sub_789789789',
            'status': 'active',
            'start_date': '2023-07-01T00:00:00Z',
            'end_date': '2024-07-01T00:00:00Z'
        },
        {
            'user_id': 8,  # Assuming user with ID 8 exists
            'package_id': 2,  # Assuming package with ID 2 exists
            'stripe_subscription_id': 'sub_1010101010',
            'status': 'pending',
            'start_date': '2023-08-01T00:00:00Z',
            'end_date': '2024-08-01T00:00:00Z'
        },
        {
            'user_id': 9,  # Assuming user with ID 9 exists
            'package_id': 3,  # Assuming package with ID 3 exists
            'stripe_subscription_id': 'sub_1111111111',
            'status': 'cancelled',
            'start_date': '2023-09-01T00:00:00Z',
            'end_date': '2024-09-01T00:00:00Z'
        },
        {
            'user_id': 10,  # Assuming user with ID 10 exists
            'package_id': 2,  # Assuming package with ID 2 exists
            'stripe_subscription_id': 'sub_2222222222',
            'status': 'active',
            'start_date': '2023-10-01T00:00:00Z',
            'end_date': '2024-10-01T00:00:00Z'
        }
    ]

    for subscription_info in subscription_data:
        Subscription.objects.create(**subscription_info)

    print(f"Seeded {len(subscription_data)} subscriptions into the database.")

    payment_history_data = [
        {
            'user_id': 3,
            'package_id': 1,
            'amount': 9.99,
            'payment_gateway': 'stripe',
            'payment_status': 'success',
            'transaction_id': 'txn_1234567890',
            'paid_at': '2023-03-01T00:00:00Z'
        },
        {
            'user_id': 4,
            'package_id': 2,
            'amount': 4.99,
            'payment_gateway': 'stripe',
            'payment_status': 'failed',
            'transaction_id': '',
            'paid_at': '2023-04-01T00:00:00Z'
        },
        {
            'user_id': 5,
            'package_id': 3,
            'amount': 9.99,
            'payment_gateway': 'paypal',
            'payment_status': 'success',
            'transaction_id': 'txn_0987654321',
            'paid_at': '2023-05-01T00:00:00Z'
        },
        {
            'user_id': 6,
            'package_id': 1,
            'amount': 0.00,
            'payment_gateway': 'stripe',
            'payment_status': 'pending',
            'transaction_id': '',
            'paid_at': '2023-06-01T00:00:00Z'
        },
        {
            'user_id': 7,
            'package_id': 2,
            'amount': 4.99,
            'payment_gateway': 'paypal',
            'payment_status': 'success',
            'transaction_id': 'txn_1122334455',
            'paid_at': '2023-07-01T00:00:00Z'
        },
        {
            'user_id': 8,
            'package_id': 3,
            'amount': 9.99,
            'payment_gateway': 'stripe',
            'payment_status': 'failed',
            'transaction_id': '',
            'paid_at': '2023-08-01T00:00:00Z'
        },
        {
            'user_id': 9,
            'package_id': 1,
            'amount': 0.00,
            'payment_gateway': 'paypal',
            'payment_status': 'success',
            'transaction_id': 'txn_5566778899',
            'paid_at': '2023-09-01T00:00:00Z'
        },
        {
            'user_id': 10,
            'package_id': 2,
            'amount': 4.99,
            'payment_gateway': '',
            'payment_status': '',
            'transaction_id': '',
            'paid_at': None
        }
    ]

    from apps.subscriptions.models import PaymentHistory
    for payment_info in payment_history_data:
        PaymentHistory.objects.create(**payment_info)
    print(f"Seeded {len(payment_history_data)} payment histories into the database.")