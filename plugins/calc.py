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

from __future__ import division

import math
import operator

from api import command, message, plugin

def calc(message_in):
	"""Do some math."""
	formula = message_in.body
	formula = formula.replace('x', '*')

	if formula == None:
		msg = 'Usage: `{}calc [formula]`'.format('!')
		return message.Message(body=msg)

	if '_' in formula or '\"' in formula or '\'' in formula or '\\' in formula:
		return message.Message(body="Not a valid math problem.")

	try:
		answer = eval(formula, {'__builtins__':{}, '__locals__':{}, '__globals__':{}})
	except Exception as e:
		return message.Message(body="Not a valid math problem.")

	if type(answer) != int and type(answer) != float:
		return message.Message(body="Not a valid math problem.")

	msg = '`{}` = `{}`'.format(formula, round(answer, 3))
	# Say message
	return message.Message(body=msg)

def init(plugin_in):
	commands_list = [
		calc_command = command.Command(plugin_in, 'calc', shortdesc='Calculate given input', alt_commands=['math','=','=='])
	]
	return plugin.Plugin(plugin_in, 'calc', commands_list)
