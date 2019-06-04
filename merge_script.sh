#!/usr/bin/env bash
if [ "$TRAVIS_BRANCH" != "dev" ]; then
    exit 0;
fi

export GIT_COMMITTER_EMAIL="giusepper11@gmail.com"
export GIT_COMMITTER_NAME="Giuseppe Rosa"

mkdir deploy
cd deploy
git clone https://github.com/prefeiturasp/SME-Indice_IDEP-API.git
git merge "$TRAVIS_COMMIT" || exit
git push origin