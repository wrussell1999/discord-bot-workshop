# Reddit + Discord Meme Bot Workshop

The presentation can be found [here]().

The following libraries were used:
- [discord.py](https://discordpy.readthedocs.io/en/latest/)
- [PRAW](https://praw.readthedocs.io/en/latest/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [requests](https://realpython.com/python-requests/)

## Setup

You'll need some tokens/unique IDs/secrets to get started. Follow the guides below to get these. These will all belong inside of `creds.json`. See `creds_template.json` for a template. There's a command below to create a new `creds.json`.

- Get Setup with the [Discord API here](discord.md)

- Get Setup with the [Reddit API here](reddit.md)

## Development

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ (.venv) pip install -r requirements.txt
$ (.venv) cat creds_template.json > creds.json
```

## Run

```bash
(.venv) $ python -m discord_bot
```
