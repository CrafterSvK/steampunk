from discord.ext import commands

from core import basecog
from game.player import Player as Character


class Player(basecog.Basecog):
    def __init__(self, bot: commands.Bot):
        super().__init__(bot)

    @commands.command()
    async def me(self, ctx):
        await ctx.send("This is you:")

    @commands.command()
    async def inv(self, ctx):
        player = Character(ctx.author)

        inventory = player.get_inventory_contents()

        string = f"Inventory contents of {ctx.author.name}:\n"

        for item in inventory:
            string += f"{item.name}\n"

        await ctx.send(string)

    @commands.command()
    async def inventory(self, ctx):
        await self.inv(ctx)


def setup(bot):
    bot.add_cog(Player(bot))
