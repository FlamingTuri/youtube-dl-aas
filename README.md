# youtube-dl-aas

This project is a wrapper which exposes [youtube-dl](https://github.com/ytdl-org/youtube-dl) functionalities via REST API. It also comes with a simple GUI that allows to any device connected to the network to download videos from youtube-dl the supported sites. 

## Install

Download and run the [latest release](https://github.com/FlamingTuri/url-builder/releases).

Then visit http://127.0.0.1:5000/home

## Development

### Install dependencies

```bash
# server
cd server
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

```bash
# client
cd client
npm install
```

### Run

```bash
# server
source server/venv/bin/activate
export FLASK_APP=server/src/main.py
export FLASK_ENV=development
python3 -m flask run --host=0.0.0.0
```

```bash
# client
cd web-gui
npx ng serve --open
```

### Swagger

A swagger page is exposed at http://127.0.0.1:5000/swagger
