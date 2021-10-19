from typing import overload
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
        memberEmbed.title('Kicked')
        memberEmbed.add_field('Staff Member', value=f'{ctx.author}', inline=False)
        memberEmbed.add_field('Reason', value=f'{reason}', inline=False)
        memberEmbed.add_field('Guild', value=f'{ctx.guild.name}', inline=False)
        await member.send(memberEmbed)
        await member.kick(reason=reason)
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed()
        embed.add_field(name='Member Kicked', value=f'{member.display_name}', inline=False)
        embed.add_field(name='Reason', value=f'{reason}', inline=False)
        await ctx.send(embed)
        memberEmbed = discord.Embed()
        memberEmbed.title('Banned')
        memberEmbed.add_field(name='Staff Member', value=f'{ctx.author}', inline=False)
        memberEmbed.add_field(name='Reason', value=f'{reason}', inline=False)
        memberEmbed.add_field(name='Guild', value=f'{ctx.guild.name}', inline=False)
        await member.send(memberEmbed)
        await member.kick(reason=reason)

    @commands.command()
    async def mute(self, ctx, member : discord.Member, *, reason=None):
        role = discord.utils.find(lambda r: r.name == 'muted', ctx.guild.roles)
        if role == None:
            await ctx.guild.create_role(name="muted")
            embed = discord.Embed()
            embed.add_field(name='Member Muted', value=f'{member.display_name}', inline=False)
            embed.add_field(name='Reason', value=f'{reason}', inline=False)
            await ctx.send(embed=embed)
            memberEmbed = discord.Embed(title="Muted")
            memberEmbed.add_field(name='Staff Member', value=f'{ctx.author}', inline=False)
            memberEmbed.add_field(name='Reason', value=f'{reason}', inline=False)
            memberEmbed.add_field(name='Guild', value=f'{ctx.guild.name}', inline=False)
            await member.send(embed=memberEmbed)
            await member.add_roles(role)
            text_channel_list = []
            for server in ctx.guilds:
                for channel in server.channels:
                    if str(channel.type) == 'text':
                        text_channel_list.append(channel)
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = False
            overwrite.read_messages = True
            await channel.set_permissions(role, overwrite)
        else:
            embed = discord.Embed()
            embed.add_field(name='Member Muted', value=f'{member.display_name}', inline=False)
            embed.add_field(name='Reason', value=f'{reason}', inline=False)
            await ctx.send(embed=embed)
            memberEmbed = discord.Embed(title="Muted")
            memberEmbed.add_field(name='Staff Member', value=f'{ctx.author}', inline=False)
            memberEmbed.add_field(name='Reason', value=f'{reason}', inline=False)
            memberEmbed.add_field(name='Guild', value=f'{ctx.guild.name}', inline=False)
            await member.send(embed=memberEmbed)
            await member.add_roles(role)

def setup(bot):
    bot.add_cog(moderation(bot))