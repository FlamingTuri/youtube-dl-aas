# youtube-dl-aas

## Install

```bash
cd server
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

```bash
cd client
npm install
```

## Run

```bash
source server/venv/bin/activate
export FLASK_APP=server/src/main.py
python3 -m flask run --host=0.0.0.0
```

```bash
cd web-gui
npx ng serve --open
```
