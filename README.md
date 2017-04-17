# DiscordFM

Sets your Discord Status to what you are currently playing on LastFM


### basic setup:

 * Edit `config.ini` and replace XXX with your information
    * You can either use your username and password OR your localStorage.token
    * Go [here](https://www.last.fm/api/account/create) to get your lastFM API key

 * Open the command prompt and type:
    ```
    python -m pip install -r requirements.txt 
    ```
 * Windows running earlier than python 3.6: Run `run.bat` file.
    * Windows console can't handle special characters which causes errors in the python script. This is fixed in python 3.6+ 
 
 * Linx & Mac: `python3 discordFM.py`
