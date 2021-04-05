import time
from discord_webhook import DiscordWebhook
while True:
    bukiwebhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/756799417243140216/JiTSuzONmFtd0YRjZWf6hYIUlEenoZ8UY_cZRFQt7Pr9hOV_Ch2SX3JJy9MUW4pDPak4', content='<@&755506462834557011> Drink water and stay hydrated i love you :heart: :heart:')
    chaoswebhook = DiscordWebhook(url='https://discord.com/api/webhooks/828721613842677841/0R-QDRNYBUtqWsQKZs8DjzImgeO8xT39AE9awuoJfi7qQhbS7bx0kydbz6aO1ERrpKh_', content='<@&827464478320230460> Drink water and stay hydrated i love you :heart: :heart:')
    bukiwebhook.execute()
    chaoswebhook.execute()
    print("shit worked")
    time.sleep(3600)
