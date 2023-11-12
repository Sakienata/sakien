python
import telebot
import moviepy.editor as mp

# Встановлення токену вашого бота
TOKEN = '6439114775:AAEDsVXRMBiZ6GlIA4VgjIgi2kAuOc5zt_E'
bot = telebot.TeleBot(6439114775:AAEDsVXRMBiZ6GlIA4VgjIgi2kAuOc5zt_E)

@bot.message_handler(content_types=['video'])
def handle_video(message):
    try:
        video_id = message.video.file_id
        file_info = bot.get_file(video_id)
        downloaded_file = bot.download_file(file_info.file_path)

        with open("video.mp4", 'wb') as new_file:
            new_file.write(downloaded_file)

        video = mp.VideoFileClip("video.mp4")
        audio = video.audio
        video_without_audio = video.set_audio(None)
        video_without_audio.write_videofile("video_without_audio.mp4", codec="libx264", audio_codec="aac")

        with open("video_without_audio.mp4", 'rb') as video:
            bot.send_video(message.chat.id, video)

    except Exception as e:
        bot.reply_to(message, f"Помилка при видаленні аудіо: {e}")

bot.polling()