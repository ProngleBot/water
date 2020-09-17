import schedule,time
from discord import Webhook, RequestsWebhookAdapter
from discord.ext import tasks
print('Penis')
def water():
    webhook = Webhook.partial(752113109904392193,'i3OXo7ct-D2tamzXgbGp6uzbMbN5aaYHYcagiAWeuuAZCrISo_qtyJKa8r0RmLd2fdof', adapter=RequestsWebhookAdapter())
    webhook.send('<@&753266209633337405> Drink water ILY!!')
    print('drank')
def walk():
    webhook = Webhook.partial(752113109904392193,'i3OXo7ct-D2tamzXgbGp6uzbMbN5aaYHYcagiAWeuuAZCrISo_qtyJKa8r0RmLd2fdof', adapter=RequestsWebhookAdapter())
    webhook.send('<@&753266209633337405> Take a break and walk around :heart: :heart: ily!!')
    print('walked')
# schedule.every(1).hour.do(water)
# schedule.every(6).hours.do(walk)
schedule.every(1).hours.do(water)
schedule.every(3).hours.do(walk)
while True:
    schedule.run_pending()
