# awesome-pegle-bot
awesome pegle bot

## HEY DINGUS

---

- if youre gonna use this bot for yourself, you need to make a `token.txt` file
- and, you need to make your own **discord bot** with your own **token**
- then, copy the token into the file
- also you can set the bot up with the `properties.json` file

### Setting up a bot / general instructions

- Go to discord developer portal and sign in
- On the left, go to `Applications`
- On the top right next to your pfp, click "New Application" and name it whatever
- Set whatever you want in the General Information tab on the left, but importantly go to the Bot tab
- ""Build-a-bot"" 🤓   click "Add Bot" on the right
- In the "OAuth2", go to URL Generator. This is where you will give the bot permissions and invite it
- In the scopes section, mark the `bot` box
- When you do that, you will se a permissions section. Make sure you at least have:
    - Read Messages/View Channels (General Permissions)
    - Send Messages (Text Permisisons)
    - Read message history (Text Permissions)
- OPTIONAL: When you finish getting your permissions, you will see a link. I suggest you copy it, then go to the General tab of OAuth2 to store it in a "Redirect" (make a new one). THIS IS OPTIONAL
- Use that link that was generated to add the bot to the server
- Before you exit, go back to the "Bot" tab on the left, and get a **token**. Paste it somehwere safe later so when you download the files from github, you can paste the **token** into `token.txt`
- You have now invited the bot. All you need to do is run `main.py` after editing `properties.json` and it will work
- kill greather

### Properties of `properties.json`

---

- user: Your discord ID so that you can toggle when the others can control the game or not
- rng: A value between 0 and 100. This will determine the chance that if someone puts in a command it will go through.
- delay: A value in seconds Global delay in so that your computer isn't bombarded with 30 people trying to do something at once (bobjeff's idea not mine)
- doRNG: `true` or `false`. Determines if rng will be used (if `false` rng will be set to 100)
- doDelay: `true` or `false`. Determines if delay will be used (if `false` delay will be set to 0)

### Dependencies

--- 

- discord.py (latest version)
- pyautogui
- i think it should go without saying but python 3 (i suggest 3.7 or newer)