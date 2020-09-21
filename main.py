import time
from discord_webhook import DiscordWebhook
while True:
    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/752113109904392193/i3OXo7ct-D2tamzXgbGp6uzbMbN5aaYHYcagiAWeuuAZCrISo_qtyJKa8r0RmLd2fdof', content='<@&753266209633337405> Drink water and stay hydrated i love you :heart: :heart:')
    webhook.execute()
    print("shit worked")
    time.sleep(3600)
