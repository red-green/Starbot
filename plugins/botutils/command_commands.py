from api import message
from api.bot import Bot

async def run(message_in):
    cmd_names = []
    cmd_descs = []
    for botcommand in Bot.commands:
        if botcommand.devcommand != True:
            cmd_names.append(botcommand.name)
            cmd_descs.append(botcommand.shortdesc)
    cmd_list = []
    pad_len = len(max(cmd_names, key=len))
    for index, value in enumerate(cmd_names):
        cmd_list.append('{} - {}'.format(cmd_names[index].ljust(pad_len), cmd_descs[index]))
    return message.Message(body='```{}```'.format('\n'.join(cmd_list)))