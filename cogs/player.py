from discord.ext import commands

from core import basecog
import game


class Player(basecog.Basecog):
    def __init__(self, bot: commands.Bot):
        super().__init__(bot)

    @commands.command(aliases=["char", "character"])
    async def me(self, ctx):
        player = game.Player(ctx.author)

        embed = self.create_embed(
            ctx.author,
            title="Character"
        )

        attributes = player.get_attributes()

        for attribute in attributes:
            embed.add_field(
                name=attribute,
                value=attributes[attribute]
            )

        await ctx.send(embed=embed)

    @commands.command(aliases=['equip'])
    async def equipment(self, ctx):
        player = game.Player(ctx.author)

        embed = self.create_embed(
            ctx.author,
            title="Equipment"
        )

        equipment_items = player.get_equipment()

        for part in equipment_items:
            embed.add_field(
                name=part,
                value=equipment_items[part].name
            )

        await ctx.send(embed=embed)

    async def equip(self, ctx):
        player = game.Player(ctx.author)

        player.equip()

        await ctx.send()

    @commands.command(aliases=["skillset"])
    async def skills(self, ctx):
        player = game.Player(ctx.author)

        embed = self.create_embed(
            ctx.author,
            title="Character skills"
        )

        skills = player.get_skills()

        for skill in skills:
            embed.add_field(
                name=skill,
                value=skills[skill]
            )

        await ctx.send(embed=embed)

    @commands.command(aliases=["inv"])
    async def inventory(self, ctx):
        player = game.Player(ctx.author)
        inventory = player.get_inventory_contents()

        embed = self.create_embed(
            ctx.author,
            title="Inventory",
        )

        for item in inventory:
            embed.add_field(
                name=f"{item.name} \"*{item.entity_id}*\"",
                value=item.desc
            )

        await ctx.send(embed=embed)

    @commands.command()
    async def punch(self, ctx):
        await ctx.send("*Punching*...")


def setup(bot: commands.Bot):
    bot.add_cog(Player(bot))
