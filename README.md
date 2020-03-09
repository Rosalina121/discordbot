# Discord Bot (Python)
A Variety Discord Bot in Python based on Jill Stingray from Va-11 HALL-A.

# Setup
1. You need a Discord app. [Create one here](https://discordapp.com/developers/applications). Then you just put the token in, well, a token variable.
2. If you want the full functionality (eg. reddit) you'd need to create apps for them respectively and put tokens in designated spaces (like `"client_id_here"`).  If not, then you can just remove the code/commands from the source, so you don't get any errors.

# Commands and functionality
All commands start with `%`. To see the command list just use `%cmd`.
* meme, meirl, dankmeme and prequel - posts a submission from the respective subreddit. It's chosen randomly from top 10 posts in hot.
* quote - posts a quote from the `jill_quotes` list.
* redd <subreddit> - posts a submission in similar manner as earlier commands, but from a subreddit provided by user.
* catfact - gets a random cat fact
* dice <number> - "throws" a number-sided dice.
* zalgo <text> - turns your text into ť̪̥ē̘̫x̨̞̗t̗̓̕
* bob <text> - turns your text into TeXt like in a Spongebob meme.
* gdziejestgrzegorz - posts a link to a random location on Google Maps.
* xkcd - posts a random xkcd comic.
* crypto <currency> - gets current price of a coin. Input has to be like BTC, ETH etc.
* anna, kira - post ascii art.
* vote <options> - starts a reaction vote. User provides several options, and the bot counts reaction under their maessage. Reactions can be adjusted in `emoji_list`.
* results - posts results of the vote.
* goodboy - posts a message with Rad Shiba.
* s <sound> - plays a sound.
* soundboard - lists available sounds.
* tvp <text> - generates an image with custom text in the likes of various tvp generators.
* play <song/link> - just wakes up RythmBot and makes it play audio (requires RythmBot on server).
* ktomaracje <people> - randomly chooses a person who's right.
* fakeartist <players> - a Discord implementation of a party game called "Fake Artist from New York". The command posts all players and their respective roles using spoiler tags, so you have to manually unveil them.
* setword <word> - sets the word players have to draw around. You use this command only in a direct message to the bot, so others won't see it.

# Other stuff
This bot was written as an exercise to help me understand Python more. Most commands are basic and borderline useless, but each one touches a different subject when it comes to programming. APIs, image creation, sound playback, even board game implemetations. 

Feel free to use it as you wish and make changes suited for your server.
