from transmission_rpc import Client
from discord.ext import commands

import rarbgapi
from config import *

class Command(commands.Cog, name='dl'):
	def __init__(self, bot):
		self.bot = bot


	@commands.command(name='dl', help='Download a torrent')
	async def dl(self, ctx, torrent):
		rarbg = rarbgapi.RarbgAPI()
		i = rarbg.search(search_string=torrent, sort='last')[0]
		await ctx.send(f'{i.filename} ({i.category}) has been scheduled for download')
		if transmission_auth is not None:
			c = Client(path='/torrent', username=transmission_auth[0], password=transmission_auth[1])
		else:
			c = Client(path='/torrent')
		c.add_torrent(i.download)
