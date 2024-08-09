<p align="center">
    <a href="https://github.com/pyrogram/pyrogram">
        <img src="https://docs.pyrogram.org/_static/pyrogram.png" alt="Pyrogram" width="128">
    </a>
    <br>
    <b>Telegram MTProto API Framework for Python</b>
    <br>
    <a href="https://pyrogram.org">
        Homepage
    </a>
    •
    <a href="https://docs.pyrogram.org">
        Documentation
    </a>
    •
    <a href="https://docs.pyrogram.org/releases">
        Releases
    </a>
    •
    <a href="https://t.me/pyrogram">
        News
    </a>
</p>

## SubOGram

> KurimuzonAkuma Repo Upgraded By SubLiquidX

``` python
from pyrogram import Client, filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")


app.run()
```
## New Add Members! (No Bulk!)

``` python
from pyrogram import Client
from pyrogram.errors import UserAlreadyParticipant, UsernameNotOccupied, PeerIdInvalid

async def add_member_to_chat(app, chat_username, user_id):
    try:
        # Try to add the user to the chat
        await app.sub_add_chat_members(chat_username, user_id)
        print(f"Successfully added user {user_id} to {chat_username}")
        return True
    except UserAlreadyParticipant:
        print(f"User {user_id} is already a participant in {chat_username}")
        return False
    except UsernameNotOccupied:
        print(f"The username {chat_username} does not exist")
        return False
    except PeerIdInvalid:
        print(f"Invalid user ID: {user_id}")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

async def main():
    # Replace these with your actual values
    api_id = "your_api_id"
    api_hash = "your_api_hash"
    bot_token = "your_bot_token"  # If you're using a bot. For user account, use phone number instead.

    chat_username = "target_chat_username"
    user_id_to_add = 123456789  # The user ID you want to add

    async with Client("my_bot", api_id, api_hash, bot_token=bot_token) as app:
        success = await add_member_to_chat(app, chat_username, user_id_to_add)
        if success:
            print("Operation completed successfully")
        else:
            print("Operation failed")

# Run the main function
import asyncio
asyncio.run(main())
```

**Pyrogram** is a modern, elegant and asynchronous [MTProto API](https://docs.pyrogram.org/topics/mtproto-vs-botapi)
framework. It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot
identity (bot API alternative) using Python.

### Support

If you'd like to support Pyrogram, you can consider:

- [Become a GitHub sponsor](https://github.com/sponsors/delivrance).
- [Become a LiberaPay patron](https://liberapay.com/delivrance).
- [Become an OpenCollective backer](https://opencollective.com/pyrogram).

### Key Features

- **Ready**: Install Pyrogram with pip and start building your applications right away.
- **Easy**: Makes the Telegram API simple and intuitive, while still allowing advanced usages.
- **Elegant**: Low-level details are abstracted and re-presented in a more convenient way.
- **Fast**: Boosted up by [TgCrypto](https://github.com/pyrogram/tgcrypto), a high-performance cryptography library written in C.  
- **Type-hinted**: Types and methods are all type-hinted, enabling excellent editor support.
- **Async**: Fully asynchronous (also usable synchronously if wanted, for convenience).
- **Powerful**: Full access to Telegram's API to execute any official client action and more.

### Installing

``` bash
pip3 install pyrogram
```

### Resources

- Check out the docs at https://docs.pyrogram.org to learn more about Pyrogram, get started right
away and discover more in-depth material for building your client applications.
- Join the official channel at https://t.me/pyrogram and stay tuned for news, updates and announcements.
