### Moonlight Solutions ###

# you can edit this as you like and use this for your server, i dont care for credits either. #

### If your api has a api key, and you cannot edit this to work for an api with a api key, messsage me on discord and i will help you within 24 hours : pvtzd ###

import discord
from discord.ext import commands
import requests
import os 
import time 
import random 
import json 

# dev notes #
# create prefix changer #
# dev notes end #

def read_json(fn, val):
    with open(fn, "r") as f:
        nibblet = json.load(f)
        spedval = nibblet.get(val)
        return spedval

bot = commands.Bot(command_prefix=read_json("config.json", "prefix"), intents=discord.Intents.all())

bot.help_command = None
file_name = "accounts.txt"

def create_embed(t, d, f):
    embed = discord.Embed(title=t, description=d, color=discord.Color.purple())
    embed.set_footer(text=f)
    return embed



def create_moonlight_embed(t, d, f):
    embed = discord.Embed(title=t, description=d, color=discord.Color.purple())
    embed.set_footer(text=f)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1293799930845986906/1294690102559248406/Untitled.jpg?ex=670bed9e&is=670a9c1e&hm=8fc0f327bea4314693b3f8bd46dcb02962170b75d7bbfe432992775ce3dbea29&")
    return embed


def has_role(rol):
    async def doyou(ctx):
        role = discord.utils.get(ctx.guild.roles, name=rol)
        return role in ctx.author.roles
    return commands.check(doyou)
    


def read_whitelist():
    with open(file_name, 'r') as f: return [line.strip() for line in f.readlines()]



def write_whitelist(lines):
    with open(file_name, "w") as f: return f.writelines(lines)



@bot.event
async def on_member_ban(g, u):
   async for entry in g.audit_logs(action=discord.AuditLogAction.ban, limit=1):
       
       ban_author = entry.user
       if ban_author.bot:
           return
       a = read_json("ml/modlog.json", "ban_logs")
       m = create_embed("moonlight", f"{u} has been banned by {ban_author}", "-moonlight.solutions-")
       
       if a == "yes":
            f = read_json("ml/modlog.json", "ban_log_id")
            banlog_channelid = int(f)
            banlog_channel = bot.get_channel(banlog_channelid)
            await banlog_channel.send(embed=m)

@bot.event
async def on_member_kick(g, u):
   async for entry in g.audit_logs(action=discord.AuditLogAction.kick, limit=1):
       
       kick_author = entry.user
       if kick_author.bot:
           return
       a = read_json("ml/modlog.json", "kick_logs")
       m = create_embed("moonlight", f"{u} has been banned by {kick_author}", "-moonlight.solutions-")
       
       if a == "yes":
            f = read_json("ml/modlog.json", "ban_log_id")
            kicklog_channelid = int(f)
            kicklog_channel = bot.get_channel(kicklog_channelid)
            await kicklog_channel.send(embed=m)

@bot.event
async def on_ready():
    nab = read_json("config.json", "awaken_id")
    awakening_channelid = int(nab)
    awakening_channel = bot.get_channel(awakening_channelid)
    try:
        if awakening_channel is not None:
            bklu = create_moonlight_embed("awoken", "moonlight has awoken | start holdin these niggas", "-moonlight solutions-")   
            await awakening_channel.send(embed=bklu)
    except Exception as e:
         print(f"failed to send awakening message | {Exception}")
    await bot.change_presence(activity=discord.Game(name="-moonlight solutions-"))
    os.system("cls")
    print("""
o                     __...__     *               
              *   .--'    __.=-.             o
     |          ./     .-'     
    -O-        /      /   
     |        /    '"/               *
             |     (@)     
            |        \                         .
            |         \
 *          |       ___\                  |
             |  .   /  `                 -O-
              \  `~~\                     |
         o     \     \            *         
                `\    `-.__           .  
    .             `--._    `--'jgs
                       `---~~`                *
            *                   o
    moonlight solutions | bot online | hold these niggas
""")


@bot.command()
@has_role("hit perms")
async def hit(ctx, ip, time, method, port):
    ongang = read_json("config.json", "api_link")
    g = f"{ongang}"
    main_req = requests.post(g) # roblox is just a example clearly
    print(main_req.status_code)
    if main_req.status_code == read_json("config.json", "failure_status_code"): # set this to the status code your api sends when it fails
        nah = create_moonlight_embed("unsuccessful", "bot failed to connect to api", "this likely means your api is not being hosted or the request isnt arranged correctly | moonlight solutions")
        await ctx.send(embed=nah)
    else: # successful response
        yeaa = create_moonlight_embed("successful", f"fucked {ip}:{port} for {time} seconds with {method} | hold that bitch nigga")
        await ctx.send(embed=yeaa)


@bot.command()
async def methods(ctx):
    m = requests.get("https://pastebin.com/raw/uH5EX15F").text
    yessir = create_embed("Methods", f"{m}", "-moonlight solutions-")
    await ctx.send(embed=yessir)



@bot.command()
@commands.cooldown(1, 600, commands.BucketType.user)
async def suggest(ctx, *, sg: str):
    nib = create_embed("moonlight", sg, "moonlight suggestions")
    suggest_id = read_json("config.json", "suggestion_id")
    try:

        suggest_channel = bot.get_channel(suggest_id)
        await suggest_channel.send(embed=nib)
        g1shit = create_embed("success", "successfully sent anonyomous suggestion", "moonlight suggestions")
   
        await ctx.send(embed=g1shit)
    except Exception as e:
        print(f"Wrong channel id || {e}")
    




@bot.command()
@commands.cooldown(1, 600, commands.BucketType.user)
async def reportbug(ctx, *, br: str):
    imhim = create_embed("moonlight", br, "moonlight bug reports")
    br_id = read_json("config.json", "bugreport_id")
    try:
        br_channel = bot.get_channel(br_id)
        await br_channel.send(embed=imhim)
        gshit = create_embed("success", "successfully sent anonyomous bug report", "moonlight bug reports")
        await ctx.send(embed=gshit)
    except Exception as e:
        print(f"Wrong channel id || {e}")


        



@bot.command()
async def coinflip(ctx):
    g = random.randint(1, 2)
    if g == 2:
        n = create_embed("moonlight", "tails", "-moonlight coinflip-")
        await ctx.send(embed=n)
    else:
        b = create_embed("moonlight", "heads", "-moonlight coinflip-")
        await ctx.send(embed=b)


@bot.command()
@has_role("whitelist perms")
async def adduser(ctx, u, p):
    try:
        with open(file_name, "a") as f:
            existing_users = read_whitelist()
            if any(user.startswith(u) for user in existing_users):
                ggang = create_embed("moonlight", "user already exists", "-moonlight whitelist-")
                await ctx.send(embed=ggang)
            else:
                embed = create_embed("moonlight", "user has been added to moonlight botnet", "-moonlight whitelist-")
                f.write(f"{u}:{p}\n")
                await ctx.send(embed=embed)
    except:
        embd = create_embed("moonlight", "incorrect file location - use reportbug command to report this to the owner of server ex: !reportbug bug", "-moonlight whitelist-")
        await ctx.send(embed=embd)


@bot.command()
@has_role("whitelist perms")
async def removeuser(ctx, username):
    lines = read_whitelist()
    nl = [line for line in lines if not line.startswith(username + ':')]
    try:
        if any(line.startswith(username + ':') for line in lines):
            write_whitelist(nl)
            emb = create_embed("moonlight", f"successfully removed {username}", "-moonlight whitelist-")
            await ctx.send(embed=emb)
        else:
            bbc = create_embed("moonlight", f"user does not exist", "-moonlight whitelist-")
            await ctx.send(embed=bbc)
    except Exception as e:
        emb1 = create_embed("moonlight", f"command failed with the error being: {Exception} - please report this error using !reportbug if you cant get this command to work", "-moonlight whitelist-")



@bot.command()
async def help(ctx, category: str="none"):
    if category == "none":
        a = create_embed("moonlight", "!help booter\n!help adminstrative\n!help fun\n!help misc", "-moonlight help-")
        await ctx.send(embed=a)
    elif category == "booter":
        b = create_embed("moonlight", "!hit [ip] [time] [method] [port]", "-moonlight help-")
        await ctx.send(embed=b)
    elif category == "administrative":
        c = create_embed("moonlight", "!adduser [user:password]\n!removeuser [user]", "-moonlight help-")
        await ctx.send(embed=c)
    elif category == "fun":
        d = create_embed("moonlight", "!coinflip [heads or tails]", "-moonlight help-")
        await ctx.send(embed=d)
    elif category == "misc":
        e = create_embed("moonlight", "!suggest [suggestion]\n!reportbug [bug]", "-moonlight help-")
        await ctx.send(embed=e)
    else:
        f = create_embed("moonlight", "invalid category", "-moonlight errors-")
        await ctx.send(embed=f)


@bot.command()
@has_role("whitelist perms")
async def changeprefix(ctx, pre):
    with open('config.json', 'r') as f:
        config = json.load(f)
    config['prefix'] = pre

    with open("config.json", 'w') as file:
        json.dump(config, file, indent=4)
    
    bot.command_prefix = pre
    embed = create_embed("moonlight", f"prefix has been updated to: {pre}", "-moonlight prefix changer-")

    await ctx.send(embed=embed)


@bot.command()
async def whois(ctx, user: discord.Member):

    try:
        join_date = user.joined_at
        creation_date = user.created_at
        roles = user.roles
        role_mentions = [role.mention for role in roles if role.name != "@everyone"]
        role_message = ', '.join(role_mentions)
        perms = ctx.channel.permissions_for(user)
        permission_list = [perm for perm, value in perms if value]
        perms_message = ', '.join(permission_list)
        a = create_embed("moonlight", f"User joined at {join_date}\nUser created account at: {creation_date}\nUser Roles:\n{role_message}\nUser Permission List:\n{perms_message}", "-moonlight finder-")
        await ctx.send(embed=a)
        

    except:
        b = create_embed("moonlight", f"error occured: {Exception}", "-moonlight solutions-")
        await ctx.send(b)


@bot.command()
@has_role("mod perms")
async def ban(ctx, user: discord.Member):
    emb1 = create_embed("moonlight", f"{user} has been banned successfully", "-moonlight administration-")
    try:
        await user.ban()
        await ctx.send(embed=emb1)
        a = read_json("ml/modlog.json", "ban_logs")
        b = read_json("ml/modlog.json", "ban_log_id")
        c = create_embed("moonlight", f"{ctx.author} has banned {user}", "-moonlight solutions-")
        if a == "yes": 
            ban_channelid = int(b)
            ban_channel = bot.get_channel(ban_channelid)
            await ban_channel.send(embed=c)
    except Exception as e:
        emb2 = create_embed("moonlight", f"unknown exception has occured: {e}", "-moonlight administration-")
        await ctx.send(embed=emb2)



@bot.command()
@has_role("mod perms")
async def kick(ctx, user: discord.Member):
    emb1 = create_embed("moonlight", f"{user} has been kicked successfully", "-moonlight administration-")
    try:
        await user.kick()
        await ctx.send(embed=emb1)
        a = read_json("ml/modlog.json", "kick_logs")
        b = read_json("ml/modlog.json", "kick_log_id")
        c = create_embed("moonlight", f"{ctx.author} has kicked {user}", "-moonlight solutions-")
        if a == "yes": 
            kick_channelid = int(b)
            kick_channel = bot.get_channel(kick_channelid)
            await kick_channel.send(embed=c)
    except Exception as e:
        emb2 = create_embed("moonlight", f"unknown exception has occured: {e}", "-moonlight administration-")
        await ctx.send(embed=emb2)
        
def write_json(file_path, key, value):
    try:
        with open(file_path, 'r+') as file:
            data = json.load(file)
            data[key] = value  # Update the key with the new value
            file.seek(0)  # Move to the beginning of the file
            json.dump(data, file, indent=4)  # Write the updated data back to the file
            file.truncate()  # Remove any leftover data
    except Exception as e:
        print(f"Error writing JSON: {e}")

@bot.command()
@has_role("mod perms")
async def banlogs(ctx, a):
    blv = read_json("ml/modlog.json", "ban_logs")
    if a == "yes":
        if blv != "yes":
            try:
                write_json("ml/modlog.json", "ban_logs", "yes")
                h = create_embed("moonlight", f"ban logs are now on", "-moonlight administration-")
                await ctx.send(embed=h)
            except Exception as e:
                await ctx.send(e) 
        else:
            g = create_embed("moonlight", f"ban logs are already enabled", "-moonlight administration-")
            await ctx.send(embed=g)
    elif a == "no":
        if blv != "no":
            write_json("ml/modlog.json", "ban_logs", "no")
            t = create_embed("moonlight", "ban logs are now disabled", "-moonlight administration-")
            await ctx.send(embed=t)
    else:
        u = create_embed("moonlight", "this value is not valid", "-moonlight administration-")
        await ctx.send(embed=u)





@reportbug.error
async def rb_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        n = create_embed("moonlight", "this command is on cooldown for 10 minutes", "-moonlight bug reports-")
        await ctx.send(embed=n)

@suggest.error
async def sg_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        n = create_embed("moonlight", "this command is on cooldown for 10 minutes", "-moonlight suggestions-")
        await ctx.send(embed=n)

@hit.error
async def hit_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        n = create_embed("moonlight", "you do not have access to this command", "-moonlight solutions-")
        await ctx.send(n)

@adduser.error
async def adduser_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        n = create_embed("moonlight", "you do not have access to this command", "-moonlight solutions-")
        await ctx.send(n)

@removeuser.error
async def removeuser_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        n = create_embed("moonlight", "you do not have access to this command", "-moonlight solutions-")
        await ctx.send(n)

@changeprefix.error
async def changeprefix_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        n = create_embed("moonlight", "you do not have access to this command", "-moonlight solutions-")
        await ctx.send(n)

@whois.error
async def whois_error(ctx ,error):
    if isinstance(error, commands.MemberNotFound):
        n = create_embed("moonlight", "user does not exist", "-moonlight solutions-")
        await ctx.send(embed=n)

@ban.error
async def ban_error1(ctx, error):
    if isinstance(error, commands.CheckFailure):
        n = create_embed("moonlight", "you do not have access to this command", "-moonlight solutions-")
        await ctx.send(embed=n)
    elif isinstance(error, commands.MemberNotFound):
        n = create_embed("moonlight", "user does not exist", "-moonlight administration-")
        await ctx.send(embed=n)


@kick.error
async def kick_error1(ctx, error):
    if isinstance(error, commands.CheckFailure):
        n = create_embed("moonlight", "you do not have access to this command", "-moonlight solutions-")
        await ctx.send(n)
    elif isinstance(error, commands.MemberNotFound):
        n = create_embed("moonlight", "user does not exist", "-moonlight administration-")
        await ctx.send(embed=n)







#token
bot.run(read_json("config.json", "token"))
