# DiscordFM

Sets your Discord Status to what you are currently playing on LastFM.


### Basic Setup For Windows:
 * Download the latest version under [releases](https://github.com/00firestar00/discordFM/releases)

 * Edit `config.ini` and replace XXX with your information
   * You can either use your username and password OR your localStorage.token
   * Go [here](https://www.last.fm/api/account/create) to get your lastFM API key

 * Double click `run.bat`. If you use the .exe, it will break when trying to play non-english song titles.


### Basic Setup For Linux & Mac:

 * Install Python 3.5 or higher

 * Edit `config.ini` and replace XXX with your information
   * You can either use your username and password OR your localStorage.token
   * Go [here](https://www.last.fm/api/account/create) to get your lastFM API key

 * Open the command prompt and type:
    ```
    python3 -m pip install -r requirements.txt 
    ```
 * To Run:
    ```
    python3 discordFM.py
    ```

### FAQ:

 * The console is printing gibberish. What gives?
   * Blame Windows, it doesn't like UTF-8 chars. Discord should still show them correctly.
 * How come I can't see what song I'm playing on Discord?
   * Blame Discord, for some reason you can't view it yourself. Get a friend to help test.

 
###### Shoutout to @noname on discord for giving me the idea and for helping me test things.
