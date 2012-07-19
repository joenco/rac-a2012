from rivescript import RiveScript

bot = RiveScript()
bot.load_directory("./recursos")
bot.sort_replies()

while True:
    persona = raw_input()
    print bot.reply("user", persona )
