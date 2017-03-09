import urllib.request
import urllib.error
import json
import plugin
import command
import message
import os
import caching

def onInit(plugin):
    xkcd_command = command.command(plugin, 'xkcd', shortdesc='Posts the latest XKCD, or by specific ID')
    return plugin.plugin.plugin(plugin, 'comics', [xkcd_command])

def onCommand(message_in):
    if message_in.command == 'xkcd':
        if message_in.body != '':
            try:
                if int(message_in.body) < 0:
                    return message.message(body="ID `{}` is not a valid ID".format(message_in.body))
            except:
                return message.message(body='Input of `{}` is not a valid number'.format(message_in.body))

            data = json.loads(caching.getJson("https://xkcd.com/{}/info.0.json".format(message_in.body.strip())))
        else:
            data = json.loads(caching.getJson("https://xkcd.com/info.0.json"))

        caching.downloadToCache(data['img'], '{}.png'.format(data['num']), caller='xkcd')

        return message.message(body='**{}/{}/{} - {}**\n_{}_'.format(data['month'], data['day'], data['year'], data['safe_title'], data['alt']),
                              file='cache/xkcd_{}.png'.format(data['num']))