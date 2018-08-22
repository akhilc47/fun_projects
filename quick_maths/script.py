import asyncio
import discord
import operator
from discord.ext.commands import Bot
from helper import QuickMathGame, get_token

COMMAND_PREFIX = 'qm '
TOKEN = get_token()
client = Bot(command_prefix=COMMAND_PREFIX)
game = {}


@client.event
async def on_ready():
    print('started!')


@client.command(name='start', description='type "qm start" to start the game', pass_context=True)
async def start_puzzle(context):
    global game
    channel = context.message.channel
    print(channel.name, channel.id)
    if channel.id not in game:
        game[channel.id] = QuickMathGame()
    print(channel.name, channel.id)
    if not game[channel.id].game_running:
        print(game[channel.id].question, game[channel.id].answer)
        await client.say(game[channel.id].question)
        game[channel.id].game_running = True
    else:
        await client.say('Game already started')


@client.command(name='stop', description='type "qm stop" to stop the game', pass_context=True)
async def stop_puzzle(context):
    global game
    channel = context.message.channel
    game[channel.id].game_running = False
    await client.say('Game has been stopped')
    return


@client.command(name='score', description='type "qm score" to display scores', pass_context=True)
async def show_score(context):
    global game
    channel = context.message.channel
    if not game[channel.id].players:
        return
    await client.say(embed=show_score_backend(channel.id))
    return


def show_score_backend(channel_id):
    global game
    if not game[channel_id].players:
        return
    sorted_scores = sorted(game[channel_id].players.items(), key=operator.itemgetter(1), reverse=True)
    embed = discord.Embed(title="Session Scoreboard", color=0x00ff00, inline=True)
    names, scores = '', ''
    for line in sorted_scores:
        names += str(line[0]) + '\n'
        scores += str(line[1]) + '\n'
    embed.add_field(name='players', value=names, inline=True)
    embed.add_field(name='scores', value=scores, inline=True)
    return embed


@client.event
async def on_message(message):
    global game
    channel = message.channel
    if message.author == client.user:
        return
    elif channel.id in game.keys() and game[channel.id].game_running:
        try:
            int(message.content)
            if message.content == str(game[channel.id].answer):
                game[channel.id].players[message.author] += 10
                await client.send_message(message.channel, '%s: %d is correct' %
                                          (message.author.mention, game[channel.id].answer))
                await client.send_message(message.channel, embed=show_score_backend(channel.id))
                await asyncio.sleep(3)
                game[channel.id].get_puzzle()
                print(game[channel.id].question, game[channel.id].answer)
                await client.send_message(message.channel, game[channel.id].question)
            else:
                await client.send_message(message.channel, '%s: %s is wrong' %
                                          (message.author.mention, message.content))
        except ValueError:
            print('input was not a number')
    await client.process_commands(message)

client.run(TOKEN)
