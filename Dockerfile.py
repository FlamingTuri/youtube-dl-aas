FROM python:3.10-bullseye

SHELL ["/bin/bash", "-c"]


RUN mkdir /home/docker-user
RUN groupadd -g 984 docker-user
RUN useradd -r -u 984 -g docker-user -d /home/docker-user docker-user
RUN chown docker-user:docker-user /home/docker-user


USER docker-user

WORKDIR /home/docker-user

COPY --chown=docker-user .github .github
COPY --chown=docker-user server/requirements.txt server/requirements.txt
COPY --chown=docker-user server/src server/src
COPY --chown=docker-user web-gui web-gui

ENV NVM_DIR /home/docker-user/nvm
ENV NODE_VERSION 16.15.0

RUN mkdir $NVM_DIR

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash \
  && source $NVM_DIR/nvm.sh \
  && nvm install $NODE_VERSION \
  && nvm alias default $NODE_VERSION \
  && nvm use default

# add nvm installed node to path
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH


# creates a python virtualenv and adds it to the path
ENV VIRTUAL_ENV=/home/docker-user/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


RUN [ "node", ".github/script/create-artifacts.mjs", "docker-app", "main_web.py", "requirements", "false" ]

WORKDIR /home/docker-user/server

ENTRYPOINT [ "python3", "-m", "src.main_web", "--port=${PORT}" ]
