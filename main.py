import discord
import json

import sentiment

client = None

def handle_response(message) -> str:

    botID = client.user.id
    new_message = message.lower().replace(f'<@{botID}>','').strip()


    if new_message == 'hello':
        return 'Hey there!'
    
    if new_message == 'hi':
        return 'meow'
    
    if new_message == '!help':
        return 'This is a help message.'
    

    # Joy/Surprise/Neutral/Fear/Disgust/Sadness/Anger
    # :heart_eyes_cat: :scream_cat: :crying_cat_face: :pouting_cat: :smiley_cat:

    result = sentiment.perform_sentiment_analysis(new_message).lower()

    # if result == 'joy':
    #     return 'meow :heart_eyes_cat:'

    # elif result == 'neutral':
    #     return 'meow :smiley_cat:'
    
    # elif result == 'surprise':
    #     return 'meow :scream_cat:'

    # elif result == 'fear':
    #     return 'meow :scream_cat:'

    # elif result == 'disgust':
    #     return 'meow :pouting_cat:'

    # elif result == 'anger':
    #     return 'meow :pouting_cat:'
    
    # elif result == 'sadness':
    #     return 'meow :crying_cat_face:'

    if result == 'joy':
        return 'meow :heart_eyes_cat:'

    elif result == 'neutral':
        return 'meow :smiley_cat:'
    
    elif result in ['surprise', 'fear']:
        return 'meow :scream_cat:'
    
    elif result in ['disgust', 'anger']:
        return 'meow :pouting_cat:'
    
    elif result == 'sadness':
        return 'meow :crying_cat_face:'


    return 'Amog'




async def send_message(message, user_message):

    

    try:
        response = handle_response(user_message)

        if response != None:
            await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():

    # API Token Security
    with open('api_tokens.json') as f:
        data = json.load(f)

    TOKEN = data["DISC_API_TOKEN"]
    
    
    intents = discord.Intents.default()  # This sets up the default intents
    intents.message_content = True  # Enable the Message Content intent
    global client
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        #print(f'{client.user} is now running!')
        print('Irthe h wra na xysw')


    @client.event
    async def on_message(message):

        self = client.user
        channel = message.channel
        isDM:bool = isinstance(channel, discord.channel.DMChannel)

        if message.author == self or (self not in message.mentions and not isDM):
            return
        

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")


        await send_message(message, user_message)

    client.run(TOKEN)





if __name__ == '__main__':
    run_discord_bot()