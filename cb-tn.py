
import response as r
import discord

async def send_message(message, user_message):
    try:
        response = await r.get_reponse(message, user_message)
    
        await message.author.send(response)
       
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE5OTA1OTM0MzIxNjIxODEyMg.Gi8XA0.sSL8txoI5rwMBOQVLcQOM5MLxfZBnaWiUFr0ts'
    
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username=str(message.author)
        user_message=str(message.content)
        channel=str(message.channel)
        print(f'{username} said : {message.content} ({channel})')
        
       
        await send_message(message , user_message)
      

    client.run(TOKEN)

if __name__ == '__main__':
    run_discord_bot()

