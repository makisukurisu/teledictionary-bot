# TeleDictionary - Get definitions of words from Telegram

## Description

This bot uses different sources to get definitions of words. Here are the ones planned:
- [ ] [Oxford Dictionary](https://developer.oxforddictionaries.com/)
- [ ] [Urban Dictionary](https://api.urbandictionary.com) (Unofficial API)
- [ ] [Google Gemini (former Bard)](https://ai.google.dev/) (By means of sending a prompt asking for a definition, experimental)

## Usage

This section will be updated later on.

Bot should work in different modes:
- [ ] Inline (primary)
- [ ] Chat (secondary, perhaps for settings and other stuff)

## Installation

This project uses [PDM](https://pdm-project.org/), to install the dependencies, run:

```bash
pdm install
```

## Configuration

To configure the bot, you need to create a `.env` file in the root of the project.
Take a look at [`example.env`](./example.env) for the required environment variables.

## Running

To run the bot, simply run:

```bash
pdm start_bot
```

## Contributing

This project is open to contributions. If you want to contribute, please take a look at the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

Use the [issues](/issues) page to report bugs or suggest new features.

## License

This project is licensed under the [MIT License](./LICENSE).
