#!/bin/bash
#Activate the env
source  /home/ubuntu/.venvs/tangibleai/bin/activate
echo "Env activated..............."
# we start by converting database data into csv
/home/ubuntu/.venvs/tangibleai/bin/python   /home/ubuntu/.code/django_arduino/vivian/get_database_info_to_csv.py
echo "data has been changed......."
# we start updating the heroku by entering its root directory
cd /home/ubuntu/.code/django_arduino/vivian/visuals
echo "Entering visuals directory............"
# while there add changes to local repository 
/usr/bin/git  add .
echo "adding changes to local repo.........."
# commit those changes..
/usr/bin/git commit -m 'Add dashboard files'
echo "commiting changes to repo.............."
#push those changes to heroku
/usr/bin/git push heroku master
echo "pushing changes now...................."
#go back to root directory
cd ..
echo "back to root directory................."
#while there add changes to github
/usr/bin/git  add .
echo "adding changes to local linus repo.........."
#commit  
/usr/bin/git commit -m 'send it'
echo "commiting changes to linus repo.............."
#push those changes to linus
set user = "jakobwamani"
set pd = "headphone@1" 

#/usr/bin/git push origin master

/usr/bin/expect <<EOD
spawn /usr/bin/git push origin master
expect "Username for 'https://github.com':"
send "jakobwamani\n"
expect "Password for 'https://github.com':"
send "headphone@1\n"
expect eof
EOD
echo "pushing changes now to linus...................."

#after all that we start to collect the data
echo "starting to collect data now...................."
/home/ubuntu/.venvs/tangibleai/bin/python   /home/ubuntu/.code/django_arduino/vivian/insert_data_to_database.py











