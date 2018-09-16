import discord
from discord.ext.commands import Bot # <--- this line
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(commands_prefix = "!")

@client.event #Console Message
async def on_ready():
    print("Bot is online")

    @client.event #!say
    async def on_message(message):
        if message.content.startswith('!ping'):
            userID = message.author.id
            await client.send_message(message.channel, "<@%s) Pong!" %  (userID))
            if message.content.upper().startswith('!SAY'):
                if message.content.upper().startswith('!SAY'):
                    if message.author.id == "370000651352014850":
                args = message.content.split("")
                #args[0] = !say
                #args[1] = Hey
                #args[2] = There
                #args[1:] = Hey There
                await client.send_message(message.channel, "%s" % ("".join(args[1:])))
            else:
                @client.event #Bot Moderator Check
                await client.send_message(message.channel, "You Can not perfrom this command!" )
                if message.content.upper().startswith('!whois'):
                    if "370000651352014850" in [role.id for role in message.author.roles]:
                        await client.send_message(message.channel "You are a bot moderator")
                    else:
                    await client.send_message(message.channel "You are not a bot moderator")

                    @client.event #Chat filter
                    async def on_message(message):
                            contents = message.content.split("Nigger ")  # contents is a list type
                            for word in contents:
                                if word.upper() in chat_filter:
                                    if not message.author.id in bypass_list:
                                        try:
                                            await client.delete_message(message)
                                            await client.send_message(message.channel,
                                                                      "**Hey!** You're not allowed to use that word here!")
                                        except discord.errors.NotFound:
                                                return

                        @bot.command(pass_context=True)

                        @commands.has_permissions(kick_members=True)
                        async def kick(ctx, user: discord.Member):

                            if ctx.message.author.server_permissions.kick_members:
                                await bot.delete_message(ctx.message)

                            try:
                                await bot.kick(user)
                                await bot.say(user.name + ' was kicked✅  Good bye ' + user.name + '!')

                            except discord.Forbidden:
                                await bot.say(embed=Forbidden)
                                return
                            except discord.HTTPException:
                                await bot.say('kick failed.')
                                return

                                # clear command

                        @bot.command(pass_context=True)
                        @commands.has_permissions(manage_messages=True)
                        async def clear(ctx, number):

                            if ctx.message.author.server_permissions.ban_members:
                                mgs = []  # Empty list to put all the messages in the log
                                number = int(number)  # Converting the amount of messages to delete to an integer
                            async for x in bot.logs_from(ctx.message.channel, limit=number + 1):
                                mgs.append(x)

                            try:
                                await bot.delete_messages(mgs)
                                await bot.say(str(number) + ' messages deleted')

                            except discord.Forbidden:
                                await bot.say(embed=Forbidden)
                                return
                            except discord.HTTPException:
                                await bot.say('clear failed.')
                                return

                            await bot.delete_messages(mgs)

                            # mute command

                        @bot.command(pass_context=True)
                        @commands.has_permissions(mute_members=True)
                        async def mute(ctx, user: discord.Member):
                            if ctx.message.author.server_permissions.mute_members:
                                role = discord.utils.get(ctx.message.server.roles, name='Muted')
                                await bot.delete_message(ctx.message)
                            try:
                                await bot.add_roles(ctx.message.mentions[0], role)
                                await bot.say('Muted ✅ ' + user.name + ' 🔇')


                            except discord.Forbidden:
                                await bot.say(embed=Forbidden)
                                return
                            except discord.HTTPException:
                                await bot.say('mute failed.')
                                return

                                # unmute command

                        @bot.command(pass_context=True)
                        @commands.has_permissions(mute_members=True)
                        async def vocal(ctx, user: discord.Member):
                            if ctx.message.author.server_permissions.mute_members:
                                role = discord.utils.get(ctx.message.server.roles, name='Muted')
                                await bot.delete_message(ctx.message)
                            try:
                                await bot.remove_roles(ctx.message.mentions[0], role)
                                await bot.say(' ✅ ' + user.name + ' 🔉 is now Vocal')

                            except discord.Forbidden:
                                await bot.say(embed=Forbidden)
                                return
                            except discord.HTTPException:
                                await bot.say('Failed to make Vocal.')
                                return

                                # ban command

                        @bot.command(pass_context=True)
                        @commands.has_permissions(ban_members=True)
                        async def ban(ctx, user: discord.Member):

                            if ctx.message.author.server_permissions.ban_members:
                                await bot.delete_message(ctx.message)

                            try:
                                await bot.ban(user)
                                await bot.say(user.name + ' was banned ✅  Good bye ' + user.name + '!')

                            except discord.Forbidden:
                                await bot.say(embed=Forbidden)
                                return
                            except discord.HTTPException:
                                await bot.say('ban failed.')
                                return

                            # unban command

                            @bot.command(pass_context=True)
                            @commands.has_permissions(ban_members=True)
                            async def unban(ctx):
                                ban_list = await bot.get_bans(ctx.message.server)

                                # Show banned users
                                await bot.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

                                #Anti Raid Stuff










                          client.run(os.environ['BOT_TOKEN'])



