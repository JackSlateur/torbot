from discord.ext import commands
import rarbgapi


class Command(commands.Cog, name='Search'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='search', help='Search torrents')
	async def search(self, ctx, *truc):
		search = ' '.join(truc)
		rarbg = rarbgapi.RarbgAPI()
		found = rarbg.search(search_string=search, sort='last')
		result = f"Searching for {search} .. {len(found)} results found\n"
		for i in found:
			result += f"{i.filename} ({i.category})\n"

		await ctx.send(f'```\n{result}\n```')
