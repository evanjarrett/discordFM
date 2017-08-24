import asyncio
import configparser
import os
import signal
import sys

import discord
import pylast
from discord import Client, Status
from pylast import Track


class DiscordFM(Client):
    _current_track = ""

    def __init__(self, conf, **options):
        super().__init__(**options)

        self.config = conf
        self.status = Status.online

        if not sys.platform.startswith('win'):  # pragma: no cover
            self.loop.add_signal_handler(getattr(signal, "SIGTERM"), self.exit)

    async def on_ready(self):
        print("-" * 48)
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("-" * 48)

        lastfm_user = self.get_lasfm_user()

        str_status = self.config.get("Options", "status", fallback="online")
        self.status = Status[str_status]

        while True:
            try:
                current_track = lastfm_user.get_now_playing()
                await self.set_now_playing(current_track, self.status)
                await asyncio.sleep(5)
            except pylast.WSError as e:
                print("Error: " + e.details)
                self.exit()

    async def set_now_playing(self, track: Track, status: Status):
        if track is None:
            await self.now_playing("DiscordFM", status)
            return

        new_track = "{} - {}".format(track.get_artist().get_name(), track.get_name())
        if new_track != self._current_track:
            self._current_track = new_track
            print("Now playing: {}".format(self._current_track))
            await self.now_playing(self._current_track, status)

    async def now_playing(self, song: str = None, status: Status = Status.online):
        if song is None:
            await self.change_presence(game=None)
            return

        await self.change_presence(game=discord.Game(name=song), status=status)

    async def close(self):
        print("Closing...")
        await self.now_playing(None, status=self.status)
        await super().close()

    def get_lasfm_user(self):
        apikey = self.config.get("LastFM", "apikey", fallback=None)
        user = self.config.get("LastFM", "user", fallback=None)

        if not apikey:
            print("Error: No LastFM API Key specified")
            return

        if not user:
            print("Error: No LastFM user specified")
            return

        lastfm = pylast.LastFMNetwork(
            api_key=apikey
        )

        return lastfm.get_user(user)

    @staticmethod
    def exit():
        # This gets handled in the run() method
        raise KeyboardInterrupt


if __name__ == "__main__":
    config = configparser.RawConfigParser()
    config_file = os.path.dirname(os.path.realpath(__file__)) + "/config.ini"
    config.read(config_file)

    if not config.has_section("Discord") or not config.has_section("LastFM"):
        print("Error: Config file is invalid.")
        quit()

    token = config.get("Discord", "token", fallback=None)

    if not token or "XXXXX" in token:
        username = config.get("Discord", "user", fallback=None)
        password = config.get("Discord", "pass", fallback=None)
        if not username or not password:
            print("Error: You need to specify a token, or username and password")
            quit()

        DiscordFM(config).run(username, password)
    else:
        DiscordFM(config).run(token, bot=False)
