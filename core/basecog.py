import discord
from discord.ext import commands


class Basecog(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    def create_embed(self, author=None, **kwargs):
        author_name = author.name

        embed = discord.Embed(**kwargs)
        embed.set_footer(
            text=author_name,
            icon_url=author.avatar_url,
        )

        return embed
