#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
social={
"facebook":"https://facebook.com/{}",
"youtube":"https://youtube.com/{}",
"instagram":"https://instagram.com/{}",
"vimeo":"https://vimeo.com/{}",
"github":"https://github.com/{}",
"plus":"https://plus.google.com/{}",
"pinterest":"https://pinterest.com/{}",
"flickr":"https://flickr.com/people/{}",
"vk":"https://vk.com/{}",
"about":"https://about.me/{}",
"disqus":"https://disqus.com/{}",
"bitbucket":"https://bitbucket.org/{}",
"flipboard":"https://flipboard.com/@{}",
"twitter":"https://twitter.com/{}",
"medium":"https://medium.com/@{}",
"hackerone":"https://hackerone.com/{}",
"keybase":"https://keybase.io/{}",
"buzzfeed":"https://buzzfeed.com/{}",
"slideshare":"https://slideshare.net/{}",
"mixcloud":"https://mixcloud.com/{}",
"soundcloud":"https://soundcloud.com/{}",
"badoo":"https://badoo.com/en/{}",
"imgur":"https://imgur.com/user/{}",
"spotify":"https://open.spotify.com/user/{}",
"pastebin":"https://pastebin.com/u/{}",
"wattpad":"https://wattpad.com/user/{}",
"canva":"https://canva.com/{}",
"codecademy":"https://codecademy.com/{}"
}
def start(update, context):
    update.message.reply_text('Hi!,i will search social media user names!')
    update.message.reply_text('NOTE: DATA MAY NOT BE COMPLEATLY ACCURATE!')
    update.message.reply_text("send a user name...(just the username)")
def help(update, context):
    update.message.reply_text('Hi!,i will search social media user names!')
    update.message.reply_text('NOTE: DATA MAY NOT BE COMPLETELY ACCURATE!')
    update.message.reply_text("send a user name...(just the username)")
def echo(update, context):
    k=update.message.text
    update.message.reply_text("fetching data of username : "+k)
    update.message.reply_text("please wait kindly!")
    for i,j in social.items():
        code=requests.get(j.format(k)).status_code
        if code ==200:
            update.message.reply_text(f"{i}  :  Found  :  status code {code}")
        elif code ==404:
            update.message.reply_text(f"{i}  :  NotFound  :  status code {code}")
        else:
            update.message.reply_text(f"{i}  :undefined status code:  status code {code}")
    update.message.reply_text("Done!")
    update.message.reply_text("More social meadias will be added soon!")
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("TOKEN", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
