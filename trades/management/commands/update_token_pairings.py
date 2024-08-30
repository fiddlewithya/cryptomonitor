import requests
from django.core.management.base import BaseCommand
from pathlib import Path

class Command(BaseCommand):
    help = 'Fetches the latest Bybit symbols and updates TOKEN_PAIRINGS in token_pairings.py'

    def handle(self, *args, **kwargs):
        response = requests.get('https://api.bybit.com/v2/public/symbols')
        data = response.json()

        if response.status_code == 200 and 'result' in data:
            # Prepare the token pairings with correct formatting and indentation
            token_pairings = []
            for item in data['result']:
                token_pairings.append(f"    ('{item['name']}', '{item['base_currency']}/{item['quote_currency']} Perpetual'),")

            formatted_token_pairings = "TOKEN_PAIRINGS = [\n" + "\n".join(token_pairings) + "\n]"

            # Path to your token_pairings.py file
            token_pairings_path = Path(__file__).resolve().parent.parent.parent / 'token_pairings.py'

            if token_pairings_path.exists():
                with open(token_pairings_path, 'w') as file:
                    file.write(formatted_token_pairings)

                self.stdout.write(self.style.SUCCESS(f'Successfully updated TOKEN_PAIRINGS with {len(token_pairings)} pairs.'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to find token_pairings.py at: {token_pairings_path}'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch the latest Bybit symbols.'))
