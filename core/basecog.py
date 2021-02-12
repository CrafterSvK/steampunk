from discord.ext import commands


class Basecog(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
