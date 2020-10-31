import sh
from discord.ext import commands

import rarbgapi
from config import *

tremote = sh.Command('transmission-remote').bake(transmission_url)
if transmission_auth is not None:
	tremote = tremote.bake('--auth', transmission_auth)

class Command(commands.Cog, name='dl'):
	def __init__(self, bot):
		self.bot = bot


	@commands.command(name='dl', help='Download a torrent')
	async def dl(self, ctx, torrent):
		rarbg = rarbgapi.RarbgAPI()
		i = rarbg.search(search_string=torrent, sort='last')[0]
		await ctx.send(f'{i.filename} ({i.category}) has been scheduled for download')
		tremote('-a', i.download)
