import time
from discord_webhook import DiscordWebhook
while True:
    for _ in range(6):
        webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/752113109904392193/i3OXo7ct-D2tamzXgbGp6uzbMbN5aaYHYcagiAWeuuAZCrISo_qtyJKa8r0RmLd2fdof', content='<@!518543956787593256> Drink water')
        webhook.execute()
        print("shit worked")
    time.sleep(3600)