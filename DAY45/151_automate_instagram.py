from instabot import Bot
bot = Bot()
bot.login(username="adalovelace2003", password="donttrythispass") # do not try to login haha
# bot.follow('wscubetechindia')
bot.upload_photo("picture.jpg", caption = "test")
# bot.unfollow('wscubetechindia')
bot.send_message("sent from python instabot",["person1","person2"] )

followers = bot.get_user_followers("adalovelace2003")
for follower in followers:
    print(bot.get_user_info(follower))
following = bot.get_user_following("adalovelace2003")
for Following in following:
    print(bot.get_user_info(Following))
