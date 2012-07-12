from rivescript import RiveScript

bot = RiveScript()
bot.load_directory("./recursos")
bot.sort_replies()

print bot._freeze
while True:
    persona = raw_input()
    print bot.reply("user", persona )
