import json
import urllib.request
from random import *
import discord
import praw
import xkcd as xk
from discord import *
from discord.ext.commands import Bot
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import pyimgur

CLIENT_ID = "client_id_here"
PATH = "tvp_out.png"
im = pyimgur.Imgur(CLIENT_ID)

q = lambda z: u''.join(
    [v + u''.join(choice(u''.join(map(chr, range(768, 815)))) for i in range(int(normalvariate(10, 5)))), v][
        v.isalpha() - 1] for v in z)

BOT_PREFIX = ("%")

TOKEN = "token_here"

reddit = praw.Reddit(client_id='client_id_here',
                     client_secret='secret_here',
                     user_agent='Discord bot for memes')

client = Bot(command_prefix=BOT_PREFIX)

tvp_list = ["tvp.png", "tvp2.png", "tvp3.png"]

sound_board = ["scream.mp3", "hello.mp3"]

jill_quotes = ["Time to mix drinks and change lives.",
               "He wants a Gut Punch. I wanna give him a gut punch, alright.",
               "She wants a Brandt-... sorry, a Mar-... AGH! A BRANDTINI! Yeah, that.",
               "Pizza with double cheese and... wait, no. This is a bar.",
               "Wait, wait... If only I could remember that song's lyrics...",
               "...I'm such a piece of shit.",
               "When will you admit you have a John face, Gil?",
               "...",
               "Tuxedo-clad talking Corgis, *yeah*.",
               "...I wish I was shitting you, trust me.",
               "We all did a cute student teacher at some point in college.",
               "I don't trust you. You could fit a bottle between those tits of yours, and nobody would know.",
               "\*pffffft\*",
               "I'm guessing if some authority on alcohol came in here, "
               "he'd stab me for crimes against beverages or something.",
               "I... um... brought my cat.",
               "Boss... what the fuck?",
               "That I'm realizing I made a fuss about serving drinks to someone underaged, but here I am.",
               "\*sigh\*",
               "Lilim are *soft*... and warm.",
               "Welcome to Valhalla."]

anna_ascii = """```
    .                             .      .
   .                             . .    ..
  .       . ...        . .        ...   ..  .
  .         . .  .    .. .         ..    .
  .       ,       ,       ..         .    .
                  ,        .         .
          ,       ,        ,
         ,,..,.  .,,  ,,,.,,,,.
              .(#((((((/
         .%,   ,&&&&&&&,**,.                     .
        .,@*   ,&&&&&&&@@&                       .
         (&@%../&&&&&&&&@@@%.. ,                 .
         (&&&&&&&&&&&&&&&&&@@@(*                 .
         ,&&&&&&&&&&&&&&&&&&&@(*
          (&&&&&&&&&&&&&&&&&&&*.
           #&&&&&&&&&&&&&&&&&&*.
            ,%&&&&&&&&&&&&&&/.
              .(&&&&&&&&&&&,,
                 /#&&&&&%/,,*,,
                      .,*****,.
                       *****/*.
                      ,**(##(/.
                    .*/(####/*
                   ,///(####*.
                   ..... .*(,
                                                  
                                                  .,,.
                                                ......
      .                                       ........
      ...                                    ........,
       ....                     ..         .....  ...,
 ......                .....,,..          ...    ....,.
.........     ...        ...             .      .....,.
          ..,   .,.         ..........        .......,.
       ...,,.  ...,    ...............       ........,.
      ..,,.,.  .....      ............    ...........,.
     .,,....  .....,                      ...........,.
    .,,....    ...., .                      .........,.
                .....                     ..  .   .,,,.
                    .                       .......,,,.
                                         .    .......,
             .       .       .            ..   ......,
             .       ..      ..           ...   ......
```
"""

miki_ascii = """```
#######(((#(,#(,*/,.,./,.(/,,....... ..    .     
#######((##.#%#//(..,.,,,(,,,..........     .    
#######(#(#%*#(#*,,.,..,,,.,............. .. .   
####%(##(#.%*((#.,......,..................      
##(####(((#/(*#(.*,,....,.................%/     
(#((###(((#(#*(*.,,,,.....................%%(.   
(##(###(.##/(**,.,.*.,,..................(%%%(.  
(##(###.(/#,**/*.,,*..,.......,........,#%%%%%/. 
(##((#,.(.#...,,.,,.,,,,*%&&&&&&&&&&&&%%%%(**(*,.
#####,.,(,/.....,.......*#*(&&&&&&&%%*/.........,
###(...*.*,.....,..,&&%,,.,#&&&&&&&*&*,*.%,..#%
###,..,,./.......,..,**/%&&&&&&&&&&&&&%%#(,/*,%*%
#*...,,.,*............&&&&&&&&&&&&&&&&&&&%%%*%/%#
....,...,.............#&&&&&&&&&&&&&&&&&&&%(%*%%%
..................../&&&&&&&&&&&%&%&&&&&&&%/(%%..
#...(................/&&&&&&&&&(*(&&&&%&&&/,,....
..(...................,%&&&&&&/...*&&&%%.........
(........................%&&&&&&/&&&&%(......... 
............................%&&&&&&&*..........  
......(........................*%*............. .
 ...*(.........................................  
 . ./...............................,.......     
* / ................................,...*( /,    
/..  . .............................,..........  ```                  
"""

crypto_list = ["ETH", "BTC", "LTC", "BCH", "XMR", "DASH"]


@client.command()
async def meme():
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await client.say(submission.url + "\n**" + submission.title + "**")


@client.command()
async def meirl():
    memes_submissions = reddit.subreddit('me_irl').hot()
    post_to_pick = randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await client.say(submission.url + "\n**" + submission.title + "**")


@client.command()
async def dankmeme():
    memes_submissions = reddit.subreddit('dankmemes').hot()
    post_to_pick = randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await client.say(submission.url + "\n**" + submission.title + "**")


@client.command()
async def prequel():
    memes_submissions = reddit.subreddit('prequelmemes').hot()
    post_to_pick = randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await client.say(submission.url + "\n**" + submission.title + "**")


@client.command()
async def redd(subred):
    memes_submissions = reddit.subreddit(subred).hot()
    post_to_pick = randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await client.say(submission.url + "\n**" + submission.title + "**")


@client.command()
async def quote():
    await client.say(choice(jill_quotes))


@client.command()
async def test():
    await client.say("test")


@client.command()
async def cmd():
    await client.say("Commands, I guess... Use **%**\n\n```python\n"
                     "meme                      'Posts a meme'\n"
                     "meirl                     'Posts a me_irl post'\n"
                     "prequel                   'Posts a prequel meme'\n"
                     "dankmeme                  'Posts a dankmeme'\n"
                     "quote                     'One of Jill’s quotes'\n"
                     "redd <subreddit>          'Post from a subreddit'\n"
                     "catfact                   'Random cat fact'\n"
                     "dice <number>             'Rolls a number-sided dice'\n"
                     "zalgo <text>              'Changes input to zalgo'\n"
                     "bob <text>                'Changes input to SpongeBob'\n"
                     "gdziejestgrzegorz         'Posts Grzegorz’s location'\n"
                     "xkcd                      'Random xkcd comic'\n"
                     "crypto <currency>         'Current price of cryptos'\n"
                     "anna                      'Anna Graem'\n"
                     "kira                      '*Kira* Miki'\n"
                     "vote <options>            'Starts a reaction vote'\n"
                     "results                   'Shows %vote results'\n"
                     "goodboy                   'Who’s a good boy?'\n"
                     "s <sound>                 'Plays a sound'\n"
                     "soundboard                'Lists available sounds'\n"
                     "tvp <text>                'Generates a tvp headline'\n"
                     "play                      'Literally invokes RythmBot'\n"
                     "ktomaracje <people>       'Who is right and who is not'\n"
                     "fakeartist <players>      'Fake Artist from NY Game'\n"
                     "setword <word>            'Set Game word (only use in DM)'\n"
                     "```")


@client.command()
async def catfact():
    with urllib.request.urlopen("https://catfact.ninja/fact") as url:
        data = json.loads(url.read().decode())
        await client.say("Your cat fact:\n" + data['fact'])


@client.command()
async def dice(number):
    await client.say("It's: " + str(randint(1, int(number))))


@client.command()
async def zalgo(*args):
    temp = " ".join(args)
    await client.say(q(temp))


@client.command()
async def bob(*args):
    temp = " ".join(args)
    temp = "".join(choice([k.upper(), k]) for k in temp)
    await client.say(temp)


@client.command()
async def gdziejestgrzegorz():
    longitude = round(uniform(12.961088, 27.532269), 6)
    latitude = round(uniform(53.863098, 42.094664), 6)

    url = 'https://maps.google.com/?q=' + str(latitude) + ',' + str(longitude)

    await client.say(url)


@client.command()
async def xkcd():
    await client.say(xk.getRandomComic().getImageLink())


@client.command()
async def crypto(currency):
    currency = currency.upper()

    if currency in crypto_list:
        if currency == "BTC":
            with urllib.request.urlopen("https://min-api.cryptoco"
                                        "mpare.com/data/price?fsym=" + currency + "&tsyms=USD,EUR") as url:
                data = json.loads(url.read().decode())
                await client.say("Price of " + currency + ": ```css\n" + "\nUSD: " + str(
                    data['USD']) + "\nEUR: " + str(data['EUR']) + "```")
        else:
            with urllib.request.urlopen("https://min-api.cryptoco"
                                        "mpare.com/data/price?fsym=" + currency + "&tsyms=BTC,USD,EUR") as url:
                data = json.loads(url.read().decode())
                await client.say("Price of " + currency + ": ```css\n" + "BTC: " + str(data['BT'
                                                                                            'C']) + "\nUSD: " + str(
                    data['USD']) + "\nEUR: " + str(data['EUR']) + "```")
    else:
        await client.say("Please use short codes (ex. ETH, BTC...).")


@client.command()
async def anna():
    await client.say("<:anna:441287251432046593>\n" + anna_ascii)


kira_counter = 0


@client.command()
async def kira():
    global kira_counter
    if kira_counter > 3:
        await client.say("And don't you ever forget that!")
        kira_counter = 0
    else:
        await client.say("Miki!!! <:kira:441289270146367515>\n" + miki_ascii)
        kira_counter += 1


emoji_list = ['😃', '🍆', '💦', '💩', '💯', '💠', '🌚']
votes_list = [0, 0, 0, 0, 0, 0, 0]
options = []


@client.command()
async def vote(*args):
    global votes_list
    votes_list = [0, 0, 0, 0, 0, 0, 0]
    global options
    options = args
    new_string = ""
    for x, y, z in zip(options, emoji_list, votes_list):
        new_string = new_string + y + ": " + x + "\n"

    await client.say("\nVote with reactions under this message.\nAvailable choices:\n```" + new_string + "```")


@client.command()
async def ktomaracje(*args):
    await client.say("||" + choice(args) + "||")


@client.command()
async def results():
    new_string = ""
    for x, y, z in zip(options, emoji_list, votes_list):
        new_string = new_string + y + " with " + str(z) + " votes" + ": " + x + "\n"

    await client.say("Results:\n" + "```" + new_string + "```")


@client.command(pass_context=True)
async def s(ctx, dzwiek):
    sb = sound_board

    if dzwiek == "grzech":
        sound = sb[0]
    if dzwiek == "hello":
        sound = sb[1]

    author = ctx.message.author
    voice_channel = author.voice_channel
    voice = await client.join_voice_channel(voice_channel)

    player = voice.create_ffmpeg_player(sound)
    player.start()
    voice.disconnect()
    # TODO: Ogarnąć jak to działa


@client.command(pass_context=True)
async def play(ctx, song):
    author = ctx.message.author
    voice_channel = author.voice_channel
    voice = await client.join_voice_channel(voice_channel)
    await client.say("!play " + song)


@client.command()
async def soundboard():
    await client.say("Available sounds:\n"
                     "```python\n"
                     "grzech                    'No i grzech, przekleństwo'\n"
                     "hello                     'Hello!'\n"
                     "```")


@client.event
async def on_reaction_add(reaction, user):
    list_id = 0
    print("Reacted with: " + str(reaction.emoji))
    for x in emoji_list:
        if x == str(reaction.emoji):
            votes_list[list_id] += 1
            print("Increased " + str(reaction.emoji) + " value")
        list_id += 1


@client.command()
async def goodboy():
    await client.say("I am a good boy <:radshiba:441289270062219274>")


recipe_list = []


@client.command()
async def recipe(number):
    await client.say(recipe_list[number])


@client.command()
async def tvp(*args):
    await client.say("I'm on it boss...")
    temp = " ".join(args)

    font = ImageFont.truetype("font.ttf", 25)

    image_file = choice(tvp_list)
    im1 = Image.open(image_file)

    draw = ImageDraw.Draw(im1)
    draw.text((141, 328), temp, (255, 255, 255), font=font)
    draw = ImageDraw.Draw(im1)

    im1.save("tvp_out.png")
    uploaded_image = im.upload_image(PATH, title=temp)

    await client.say(uploaded_image.link)


@client.command()
async def spoilertest():
    await client.say("||test spoilertaga||")


def random_insert(lst, item):
    lst.insert(randrange(len(lst) + 1), item)


word = "placeholder"


@client.command()
async def setword(*args):
    global word
    word = args[0]
    await client.say("Word set!")
    print("A word has been set")


@client.command()
async def fakeartist(*args):
    global word
    gamestring = ""
    # file = open("fakeart.txt", "r")
    # word = file.read()
    wordlist = []
    fake = "fake"

    for i in range(len(args) - 1):
        wordlist.append(word)

    random_insert(wordlist, fake)

    # TODO: clean this up sometime ok?
    for i, k in zip(wordlist, range(len(wordlist))):
        l1 = [i]
        if i == "fake":
            for j in range(len(word) - 4 + randint(2, 4)):
                l1.append('  ')
        else:
            for j in range(randint(2, 4)):
                l1.append('  ')
        i = ''.join(l1)
        wordlist[k] = i

    for player, assigned in zip(args, wordlist):
        gamestring += "**" + player + "**: ||" + assigned + "||\n"
    await client.say(gamestring)

# types:
# 1 - playing
# 2 - listening
# 3 - watching


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="your commands - %cmd", type=2))
    print("Logged in as " + client.user.name)


client.run(TOKEN)
