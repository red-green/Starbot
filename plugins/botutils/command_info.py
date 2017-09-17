from api import message, git
import discord

async def run(message_in):
	sha = git.git_commit()
	track = git.git_branch()
	remote = git.get_remote()

	if track == 'master':
		embed = discord.Embed(color=discord.Color.red())
	elif track == 'unstable':
		embed = discord.Embed(color=discord.Color.gold())
	elif track == 'stable':
		embed = discord.Embed(color=discord.Color.green())
	else:
		embed = discord.Embed(color=discord.Color.light_grey())
	embed.set_author(name='Project StarBot v0.2.0-{} on track {}'.format(sha[:7], track),
					url='https://github.com/1byte2bytes/Starbot/',
					icon_url='https://pbs.twimg.com/profile_images/616309728688238592/pBeeJQDQ.png')
	embed.add_field(name="Bot Team Alpha", value="CorpNewt\nSydney Erickson\nGoldfish64")
	embed.add_field(name="Source Code", value="Interested in poking around inside the bot?\nClick on the link above!")
	embed.set_footer(text="Pulled from {}".format(remote))
	return message.Message(embed=embed)