from typing import overload
import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        # Create Embed to send into channel
        embed = discord.Embed()
        embed.add_field(name='Member Banned', value=f'{member.display_name}', inline=False)
        embed.add_field(name='Reason', value=f'{reason}', inline=False)
        # Sends into the channel where the command was ran
        await ctx.send(embed=embed)
        # Create Embed to send to kicked member
        memberEmbed = discord.Embed()
        memberEmbed.title('Kicked')
        memberEmbed.add_field('Staff Member', value=f'{ctx.author}', inline=False)
        memberEmbed.add_field('Reason', value=f'{reason}', inline=False)
        memberEmbed.add_field('Guild', value=f'{ctx.guild.name}', inline=False)
        # Send the embed to the members dms
        await member.send(embed=memberEmbed)
        # Kick the member for the reason provided.
        await member.kick(reason=reason)
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        # Create embed to send into channel
        embed = discord.Embed()
        embed.add_field(name='Member Kicked', value=f'{member.display_name}', inline=False)
        embed.add_field(name='Reason', value=f'{reason}', inline=False)
        # Send embed into channel where the command was ran.
        await ctx.send(embed=embed)
        # Create member embed to send into members dms
        memberEmbed = discord.Embed()
        memberEmbed.title('Banned')
        memberEmbed.add_field(name='Staff Member', value=f'{ctx.author}', inline=False)
        memberEmbed.add_field(name='Reason', value=f'{reason}', inline=False)
        memberEmbed.add_field(name='Guild', value=f'{ctx.guild.name}', inline=False)
        # Send embed into members dms
        await member.send(embed = memberEmbed)
        # Ban the member for the reason provided
        await member.ban(reason=reason)

    @commands.command()
    async def mute(self, ctx, member : discord.Member, *, reason=None):
        # Get role muted from guild
        role = discord.utils.find(lambda r: r.name == 'muted', ctx.guild.roles)
        # If the role is not found.
        if role == None:
            # It creates the role called muted
            await ctx.guild.create_role(name="muted")
            # Create embed to send in to channel
            embed = discord.Embed()
            embed.add_field(name='Member Muted', value=f'{member.display_name}', inline=False)
            embed.add_field(name='Reason', value=f'{reason}', inline=False)
            # Send embed into the channel where the command was executed
            await ctx.send(embed=embed)
            # Create memberEmbed to send into members dms
            memberEmbed = discord.Embed(title="Muted")
            memberEmbed.add_field(name='Staff Member', value=f'{ctx.author}', inline=False)
            memberEmbed.add_field(name='Reason', value=f'{reason}', inline=False)
            memberEmbed.add_field(name='Guild', value=f'{ctx.guild.name}', inline=False)
            # Send Embed into members dms
            await member.send(embed=memberEmbed)
            # Add muted role to the member
            await member.add_roles(role)
            # Find all text channels
            text_channel_list = []
            for server in ctx.guilds:
                for channel in server.channels:
                    if str(channel.type) == 'text':
                        text_channel_list.append(channel)
            # Overwrite all channels permissions for muted role.
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = False
            overwrite.read_messages = True
            # Set the permission to all channels
            await channel.set_permissions(role, overwrite)
        # Else if the role is already created
        else:
            # Create embed to send into channel
            embed = discord.Embed()
            embed.add_field(name='Member Muted', value=f'{member.display_name}', inline=False)
            embed.add_field(name='Reason', value=f'{reason}', inline=False)
            # Send embed into the channel where the command was ran
            await ctx.send(embed=embed)
            # Create memberEmbed to send into members dms
            memberEmbed = discord.Embed(title="Muted")
            memberEmbed.add_field(name='Staff Member', value=f'{ctx.author}', inline=False)
            memberEmbed.add_field(name='Reason', value=f'{reason}', inline=False)
            memberEmbed.add_field(name='Guild', value=f'{ctx.guild.name}', inline=False)
            # Send the embed into the memebrs dms
            await member.send(embed=memberEmbed)
            # Add the muted role to the member
            await member.add_roles(role)

def setup(bot):
    bot.add_cog(moderation(bot))