import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed()
        embed.add_field(name='Member Banned', value=f'{member.display_name}', inline=False)
        embed.add_field(name='Reason', value=f'{reason}', inline=False)
        await ctx.send(embed)
        memberEmbed = discord.Embed()
        memberEmbed.add_field('Staff Member', value=f'{ctx.author}', inline=False)
        memberEmbed.add_field('Reason', value=f'{reason}', inline=False)
        memberEmbed.add_field('Guild', value=f'{ctx.guild.name}', inline=False)
        await member.send(memberEmbed)
        await member.ban(reason=reason)

def setup(bot):
    bot.add_cog(moderation(bot))