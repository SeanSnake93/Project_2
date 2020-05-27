#!/usr/bin/env bash

echo executeing: git add .

git add .

echo '... {successful}'

echo " "

echo ---------------------------------------------------------

echo git status

echo ---------------------------------------------------------

git status

echo ---------------------------------------------------------

echo " "

echo executeing: git commit -m

git commit -m "Shebang git push"

echo 'git commit {successful}'

echo " "

echo ---------------------------------------------------------

echo git status

echo ---------------------------------------------------------

git status

echo ---------------------------------------------------------

echo " "

echo executeing push...

git push

echo " "

echo 'repo upload {successful}'

echo " "
