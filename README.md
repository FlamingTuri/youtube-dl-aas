# youtube-dl-aas

This project is a wrapper which exposes [youtube-dl](https://github.com/ytdl-org/youtube-dl) functionalities via REST API. It also comes with a simple GUI that allows to any device connected to the network to download videos from youtube-dl the supported sites. 

![homescreen](readme-resources/home.png)

## Install

The app is distributed for Windows, Mac and Ubuntu based systems in two versions:
- standard, that ships as a simple tray application
- headless, ideal to be run as a deamon when a system starts up

Download and run the [latest release](https://github.com/FlamingTuri/youtube-dl-aas/releases/latest).

The application is exposed at http://127.0.0.1:5000/home

## Development

### Requirements

- node 14+
- python 3.9+

### Install dependencies

```bash
# server
cd server
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install -r requirements.gui.txt
pip3 install -r requirements.dev.txt
```

```bash
# client
cd client
npm install
```

### Run

```bash
# server
cd server
source venv/bin/activate
python3 -m src.main
```

```bash
# client
cd web-gui
npx ng serve --open
```

### Swagger

A swagger page is exposed at http://127.0.0.1:5000/swagger

## Create executable for an unsupported system

Unfortunately `pyinstaller` creates an executable only compatible with the system on which it is run on. Thus the supported operating systems will be limited by the [hosted runners provided by GitHub](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners).

However, you can create your own executable running the script used inside the the [release-artifacts](.github/workflows/release-artifacts.yml) action:

For the standard version run:
```bash
node .github/script/create-artifacts.mjs \
    youtubeDlaas \
    main_qt.py \
    requirements,requirements.gui,requirements.dev
```

For the headless version run:
```bash
node .github/script/create-artifacts.mjs \
    youtubeDlaas-headless \
    main.py \
    requirements,requirements.dev
```
