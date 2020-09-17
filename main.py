import time,discord
from discord_webhook import DiscordWebhook
from discord.ext import commands,tasks

@tasks.loop(hours=1)
async def waterrem():
    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/752113109904392193/i3OXo7ct-D2tamzXgbGp6uzbMbN5aaYHYcagiAWeuuAZCrISo_qtyJKa8r0RmLd2fdof', content='<@&753266209633337405> Drink water')
    webhook.execute()
    print("shit worked")

@tasks.loop(hours=3)
async def stretch():
    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/752113109904392193/i3OXo7ct-D2tamzXgbGp6uzbMbN5aaYHYcagiAWeuuAZCrISo_qtyJKa8r0RmLd2fdof', content='<@&753266209633337405> Stand up and walk around!')
    webhook.execute()
    print("shit worked")

waterrem.start()
stretch.start()
