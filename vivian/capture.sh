#Activate the env
source  /home/ubuntu/.venvs/tangibleai/bin/activate
echo "Env activated..............."
# we start grabbing the data
/home/ubuntu/.venvs/tangibleai/bin/python   /home/ubuntu/.code/django_arduino/vivian/insert_data_to_database.py