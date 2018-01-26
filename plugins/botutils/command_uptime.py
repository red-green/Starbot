import time

from api import message
from api.bot import Bot

from libs import readableTime

async def run(message_in):
    time_current = int(time.time())
    time_str = readableTime.getReadableTimeBetween(Bot.startTime, time_current)
    return message.Message(body='I\'ve been up for *{}*.'.format(time_str))