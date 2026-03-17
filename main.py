import discord
import os
from dotenv import load_dotenv
from aiohttp import web
import asyncio

# Load environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_IDS_STR = os.getenv("WELCOME_CHANNEL_IDS", "")
CHANNEL_IDS = [int(id.strip()) for id in CHANNEL_IDS_STR.split(",") if id.strip().isdigit()]
LOGO_URL = os.getenv("LOGO_URL", "https://webivus.com/Logo.png")
WEBSITE_URL = os.getenv("WEBSITE_URL", "https://webivus.com")

if not TOKEN:
    raise ValueError("DISCORD_TOKEN is missing in the environment or .env file.")

# Set up intense/intents
intents = discord.Intents.default()
intents.members = True  # Required for on_member_join

client = discord.Client(intents=intents)

# --- Koyeb Health Check Web Server ---
async def handle(request):
    return web.Response(text="Bot is alive 🚀")

async def start_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"✅ Health check web server started on port {port}")

@client.event
async def on_ready():
    print(f"🚀 Bot connected as {client.user.name} ({client.user.id})")
    print("Welcome channels configured:")
    for cid in CHANNEL_IDS:
        print(f" - {cid}")
        
    # Set status activity
    activity = discord.Activity(type=discord.ActivityType.watching, name="for new members 🌟 | webivus.com")
    await client.change_presence(activity=activity)

    # Start Health Check Server
    asyncio.create_task(start_server())

@client.event
async def on_member_join(member):
    print(f"👤 New member joined: {member.name} ({member.id})")
    
    # 1. Send DM
    try:
        dm_embed = discord.Embed(
            title="🚀 Welcome to Webivus AI!",
            description=f"Hey **{member.name}**! Welcome to the standalone community for Webivus AI.",
            color=0x990B4E  # Premium Dark Rose/Indigo style
        )
        dm_embed.set_thumbnail(url=LOGO_URL)
        dm_embed.add_field(
            name="🤖 What is Webivus?",
            value="Webivus is your **AI Co-Pilot for WordPress Management**. Manage your site, edit content, optimize SEO, and troubleshoot — all through natural conversation.",
            inline=False
        )
        dm_embed.add_field(
            name="⚙️ Smart Features",
            value="• **Multi-Agent System**: Admin, SEO, and QA agents working together.\n• **Human-Approved**: Safe execution with your consent.\n• **Easy Upgrade**: Start free with 5 daily credits.",
            inline=False
        )
        dm_embed.add_field(
            name="🔗 Get Started",
            value=f"[Visit our Website]({WEBSITE_URL}) | Ask in the server for help!",
            inline=False
        )
        dm_embed.set_footer(text="Webivus AI — Your WordPress Co-Pilot")
        
        await member.send(embed=dm_embed)
        print(f"✅ DM sent to {member.name}")
    except discord.Forbidden:
        print(f"⚠️ Could not send DM to {member.name} (user has DMs disabled)")
    except Exception as e:
        print(f"⚠️ Error sending DM to {member.name}: {e}")

    # 2. Send to Welcome Channels
    channel_embed = discord.Embed(
        title="✨ A New User Joined!",
        description=f"Welcome to the server, {member.mention}! We are glad to have you here.",
        color=0x990B4E
    )
    channel_embed.set_thumbnail(url=LOGO_URL)
    channel_embed.add_field(
        name="🚀 Meet Webivus AI",
        value="Manage your WordPress sites using natural chat. AI handles updates, SEO, and fixes while you relax.",
        inline=False
    )
    channel_embed.set_footer(text=f"Check out the channels or ask for a tour! | Total Members: {member.guild.member_count}")

    for channel_id in CHANNEL_IDS:
        channel = client.get_channel(channel_id)
        if channel:
            try:
                await channel.send(embed=channel_embed)
                print(f"✅ Welcome message sent to channel {channel_id}")
            except Exception as e:
                print(f"⚠️ Error sending message to channel {channel_id}: {e}")
        else:
            print(f"⚠️ Channel {channel_id} not found in cache. Verify bot is in server and has access.")

# Run the bot
if __name__ == "__main__":
    client.run(TOKEN)
