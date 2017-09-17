from api import command, plugin
from plugins.botutils import command_plugins, command_info, command_commands

def onInit(plugin_in):
    plugins_command    = command.Command(plugin_in, 'plugins', 
        shortdesc='Print a list of plugins', devcommand=True, 
        customfunction=command_plugins.run)

    commands_command   = command.Command(plugin_in, 'commands', 
        shortdesc='Print a list of commands', customfunction=command_commands.run)
    
    help_command       = command.Command(plugin_in, 'help', 
        shortdesc='Redirects to !commands', customfunction=command_commands.run)

    info_command       = command.Command(plugin_in, 'info', 
        shortdesc='Print some basic bot info', customfunction=command_info.run)

    plugintree_command = command.Command(plugin_in, 'plugintree', shortdesc='Print a tree of plugins and commands', devcommand=True)
    uptime_command     = command.Command(plugin_in, 'uptime', shortdesc='Print the bot\'s uptime', devcommand=True)
    hostinfo_command   = command.Command(plugin_in, 'hostinfo', shortdesc='Prints information about the bots home', devcommand=True)
    cpuinfo_command    = command.Command(plugin_in, 'cpuinfo', shortdesc='Prints info about the system CPUs', devcommand=True)
    setprefix_command  = command.Command(plugin_in, 'setprefix', shortdesc='Set the server prefix', devcommand=True)
    getprefix_command  = command.Command(plugin_in, 'getprefix', shortdesc='Get the server prefix', devcommand=True)
    speedtest_command  = command.Command(plugin_in, 'speedtest', shortdesc='Run a speedtest', devcommand=True)
    addowner_command   = command.Command(plugin_in, 'addowner', shortdesc='Add a bot owner', devcommand=True)
    owners_command     = command.Command(plugin_in, 'owners', shortdesc='Print the bot owners', devcommand=True)
    messages_command   = command.Command(plugin_in, 'messages', shortdesc="Show how many messages the bot has seen since start")
    servers_command    = command.Command(plugin_in, 'servers', shortdesc="Show how many servers the bot is on")
    invite_command     = command.Command(plugin_in, 'invite', shortdesc="Invite the bot to your server!")
    nickname_command   = command.Command(plugin_in, 'nickname', shortdesc="Change the bot's nickname")
    ping_command       = command.Command(plugin_in, 'ping', shortdesc='Pong!')
    return plugin.Plugin(plugin_in, 'botutils', [plugins_command, commands_command, help_command, info_command, plugintree_command, uptime_command,
                                                 hostinfo_command, cpuinfo_command, setprefix_command, getprefix_command, speedtest_command, addowner_command,
                                                 owners_command, messages_command, servers_command, invite_command, nickname_command, ping_command])

async def onCommand(message):
    return