import time
from discord_webhook import DiscordWebhook
while True:
    for _ in range(6):
        webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/741276735617761317/RDjGsSfa86vvOd8TqfRxKEUGTEpNRsTDTuizesoqJIY-FWOFB1VEwB9aMhIho_lP43OB', content='<@!518543956787593256> Drink water')
        webhook.execute()
        print("shit worked")
    time.sleep(3600)