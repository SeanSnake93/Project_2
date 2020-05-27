#!/usr/bin/env bash

echo EXECUTING: git add .

git add .

echo " "

echo '... {successful}'

echo " "

echo ---------------------------------------------------------

echo EXECUTING: git status

echo ---------------------------------------------------------

git status

echo ---------------------------------------------------------

echo " "

echo EXECUTING: git commit -m

echo " "

git commit -m "Shebang git push"

echo " "

echo '... git commit {successful}'

echo " "

echo ---------------------------------------------------------

echo EXECUTING: git status

echo ---------------------------------------------------------

git status

echo ---------------------------------------------------------

echo " "

echo EXECUTING: git push...

echo " "

git push

echo " "

echo 'repo upload {successful}'

echo " "

# Sean-David-McCann@15:38-on-27-05-2020