from instabot import Bot

bot = Bot()

# Login - apne Instagram credentials yahan daal
bot.login(username="your_username", password="your_password")

# 1. Follow a user
bot.follow("leomessi")

# 2. Like last 5 posts of that user
bot.like_user("leomessi", amount=5)

# 3. Comment on last 2 posts of that user
media_ids = bot.get_user_medias("leomessi", filtration=False)
for media_id in media_ids[:2]:
    bot.comment(media_id, "Amazing post! 🔥")

# 4. Send a Direct Message (DM)
bot.send_message("Hey! This is an automated message from InstaBot.", ["leomessi"])

# 5. Unfollow users who don't follow back
bot.unfollow_non_followers()

# 6. Get list of followers of a user and print them
followers = bot.get_user_followers("leomessi")
print(f"Followers of leomessi: {followers}")

# 7. Upload a photo with caption (Make sure photo.jpg is in your script directory)
bot.upload_photo("photo.jpg", caption="Automated post via InstaBot! #python")

# Logout (optional)
bot.logout()
