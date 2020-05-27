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


while true; do
    read -p "Do you wish to commit? (Y/n) " yn
    case $yn in
        [Yy]* ) 
        
        echo " "

        read -p "Enter commit message: " commit;

        echo " ";

        echo "EXECUTING: git commit -m";

        echo " ";

        git commit -m "${commit}";

        echo " ";

        echo '... git commit {successful}';

        echo " ";

        echo "---------------------------------------------------------";

        echo "EXECUTING: git status";

        echo "---------------------------------------------------------";

        git status;

        echo "---------------------------------------------------------";

        echo " ";
        
        while true; do
            read -p "Do you wish to push this git? (Y/n) " yn
            case $yn in
                [Yy]* ) 

                echo " ";

                echo "EXECUTING: git push...";

                echo " ";

                git push;

                echo " ";

                echo 'repo upload {successful}';

                echo " ";
                
                break;;

                [Nn]* ) exit;;

                * ) 
                
                echo "Please answer y/Y or n/N.";
                
                echo " ";;

            esac

        done

        break;;

        [Nn]* ) exit;;

        * ) 
             
            echo "Please answer y/Y or n/N.";
            
            echo " ";;

    esac

done

# Sean-David-McCann@16:39-on-27-05-2020