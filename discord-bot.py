#!/usr/bin/python3

import importlib

import glob
from os.path import dirname, basename

from discord.ext import commands
from config import TOKEN

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
	print(f'{bot.user.name} connected to Discord!')

modules = glob.glob(dirname(__file__) + "/commands/*")
packages = [basename(f) for f in modules]
packages = [f for f in packages if not f.endswith('__')]
packages = [i.rstrip('.py') for i in packages]
for i in packages:
	mod = importlib.import_module(f'commands.{i}')
	bot.add_cog(mod.Command(bot))

bot.run(TOKEN)
