def onInit(plugin_in):
    wikipedia_command = command.Command(plugin_in, 'wikipedia', shortdesc='Search Wikipedia, The Free Encyclopedia')
    return plugin.Plugin(plugin_in, 'wikipedia', [wikipedia_command])