# plugin by lejend @r4r4n4
"""Emoji

Available Commands:

.lucky"""

from telethon import events

import asyncio





@register(outgoing=True, pattern="^.lucky$")

async def lucky(lucky):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 17)

    input_str = event.pattern_match.group(1)

    if input_str == "lucky":

        await event.edit(input_str)

        animation_chars = [
        
            "⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/airpods69/oub-remix/)⬜",
            "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/airpods69/oub-remix/)⬜",
            "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/airpods69/oub-remix/)⬜",
            "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/airpods69/oub-remix/)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/airpods69/oub-remix/)⬜",    
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/airpods69/oub-remix/)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/airpods69/oub-remix/)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/airpods69/oub-remix/)⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/airpods69/oub-remix/)⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜[🎁](https://github.com/airpods69/oub-remix/)⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜[🎁](https://github.com/airpods69/oub-remix/)⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n[🎁](https://github.com/airpods69/oub-remix/)⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜",
            "⬜⬜⬜\n⬜⬜⬜\n⬜⬜⬜",
            "⬜⬜\n⬜⬜",
            "[🎁](https://github.com/airpods69/oub-remix/)"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 17])
