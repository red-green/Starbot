#    Copyright 2017 Starbot Discord Project
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0
# 
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

class Command():
    '''Store information about a command'''
    def __init__(self, plugin, name, shortdesc='no description', devcommand=False):
        self.plugin = plugin
        self.name = name
        self.shortdesc = shortdesc
        self.devcommand = devcommand

def is_command(message_in, prefix, command):
    '''Check if a given message is a command'''

    # Get user.
    if message_in.server:
        me = message_in.server.me
    else:
        me = message_in.channel.me

    #First we check if the message starts with our prefix
    if message_in.content.startswith(prefix):
        pass

    #Otherwise, we check if the message starts with a ping for the bot
    elif message_in.content.startswith(me.mention):
        pass

    #Otherwise, the inputted message does not start with a valid bot trigger
    else:
        return False

    # The first part of the message, before the first space
    command_try = message_in.content.split(' ')

    # If the first part of the message is equal to the server prefix + the command name
    # This would be used for commands with arguments
    if command_try[0] == prefix + command.name:
        return True

    # If the entire inputted message is equal to a command
    # This will mean the command has no arguments
    elif message_in.content == prefix + command.name:
        return True

    # First check that the first word in the message is a mention for the bot, a.k.a. an @ ping
    # Then we check that the second word in the message is the name of a command
    # This would mean that the command has been used with arguments
    elif command_try[0] == me.mention and command_try[1] == command.name:
        return True

    # First we check that the firct word in the message is a mention for the bot
    # Then we check that the rest of the message is equal to the name of a command
    # This would mean that the command has no arguments
    elif message_in.content == me.mention + command.name:
        return True

    # We have exhausted the possibilities for running a command, so it must not be a command.
    else:
        return False
