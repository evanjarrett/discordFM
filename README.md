# DiscordFM

Sets your Discord Status to what you are currently playing on LastFM

### Windows Users:

I now have a single executable version under [releases](https://github.com/00firestar00/discordFM/releases)

This does not require python to be installed in order to use. Just unzip, edit the config, and use the `run.bat` file.

Eventually the `run.bat` won't be necessary, but it fixes errors when using non-english characters.

### Basic Setup:

 * Edit `config.ini` and replace XXX with your information
   * You can either use your username and password OR your localStorage.token
   * Go [here](https://www.last.fm/api/account/create) to get your lastFM API key

 * Open the command prompt and type:
    ```
    python -m pip install -r requirements.txt 
    ```
 * Windows running earlier than python 3.6: Run `run.bat` file.
   * Prior to 3.6, the console would cause an error when trying to print non-english characters.
 
 * Linux & Mac run from the commandline: `python3 discordFM.py`

### FAQ:

 * The console is printing gibberish. What gives?
   * Blame Windows, it doesn't like UTF-8 chars. Discord should still show them correctly.
 * How come I can't see what song I'm playing on Discord?
   * Blame Discord, for some reason you can't view it yourself. Get a friend to help test.

 
###### Shoutout to @noname on discord for giving me the idea and for helping me test things.
