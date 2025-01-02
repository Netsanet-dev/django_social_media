from django.core.management.utils import get_random_secret_key

generate_key = get_random_secret_key()
print(generate_key)