import discord
import time
import operator
from collections import defaultdict
from discord.ext.commands import Bot
from helper import get_puzzle

COMMAND_PREFIX = 'qm '
TOKEN = 'token goes here'
client = Bot(command_prefix=COMMAND_PREFIX)

answer = 0
game_running = False
players = {}
players = defaultdict(lambda : 0, players)


@client.event
async def on_ready():
    print('started!')


@client.command(name='start', description='type "qm start" to start the game')
async def start_puzzle():

    global game_running, answer
    if not game_running:
        question, answer = get_puzzle()
        print(question, answer)
        await client.say(question)
        game_running = True
    else:
        await client.say('Game already started')


@client.command(name='stop', description='type "qm stop" to stop the game')
async def stop_puzzle():
    global game_running
    game_running= False
    await client.say('Game has been stopped')
    return


@client.command(name='score', description='type "qm score" to display scores')
async def show_score():
    global players
    if not players:
        return
    await client.say(embed=show_score_backend())
    return


def show_score_backend():
    global players
    if not players:
        return
    sorted_scores = sorted(players.items(), key=operator.itemgetter(1), reverse=True)
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

    global game_running, answer, players
    if message.author == client.user:
        return
    elif game_running:
        try:
            int(message.content)
            if message.content == str(answer):
                players[message.author] += 10
                await client.send_message(message.channel, '%s: %d is correct' % (message.author.mention, answer))
                await client.send_message(message.channel, embed=show_score_backend())
                time.sleep(3)
                question, answer = get_puzzle()
                print(question, answer)
                await client.send_message(message.channel, question)
            else:
                await client.send_message(message.channel, '%s: %s is wrong' % (message.author.mention, message.content))
        except ValueError:
            print('input was not a number')
    await client.process_commands(message)

client.run(TOKEN)
