from redbot.core import commands
import discord as redbot

class Lockdown(commands.Cog):
    """Allows the moderator/admin to lock or unlock the channel mentioned/used in."""

    @commands.command()
    @commands.bot_has_permissions(manage_roles=True, manage_channels=True)
    @commands.has_permissions(manage_channels=True, administrator=True)
    async def lockit(self, ctx, channel : redbot.TextChannel = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send('Channel has been locked.')
    
    @commands.command()
    @commands.bot_has_permissions(manage_roles=True, manage_channels=True)
    @commands.has_permissions(manage_channels=True, administrator=True)
    async def unlockit(self, ctx, channel : redbot.TextChannel = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        if overwrite.send_messages == False:
            overwrite.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            await ctx.send('Channel has been unlocked.')
        else:
            await ctx.send('Hmmm, channel isn\'t locked. Did you try checking it?')
