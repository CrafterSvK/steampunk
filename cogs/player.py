from discord.ext import commands

from core import basecog


class Player(basecog.Basecog):
    def __init__(self, bot: commands.Bot):
        super().__init__(bot)

    @commands.command()
    async def me(self, ctx):
        await ctx.send("This is you:")

    @commands.command()
    async def inv(self, ctx):
        await ctx.send("Inventory contents of {0.name}:\n".format(ctx.author))

    @commands.command()
    async def inventory(self, ctx):
        await self.inv(ctx)


def setup(bot):
    bot.add_cog(Player(bot))
