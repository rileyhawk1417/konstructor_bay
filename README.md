
-------------------------------------KONSTRUCTOR BAY--------------------------------------------------------------------------
Konstructor Bay is a Platform where a person can find or advirtise Construction materials. 

AUTHORS
------
NAME                   EMAIL                   GITHUB

Moses Gitonga  infosec947@gmail.com  <https://github.com/mosesgitonga>

For this project you will need to install flask, sqlalchemy and mysql.
      To install flask:
      pip install flask 

      To install sqlalchemy:
      pip install sqlalchemy 

      To install mysql:
      sudo apt install mysql-server -y
      sudo service mysql start




                        #USAGE:
    #CREATE DATABASE WITH TABLES IN YOUR LOCALHOST
    #RUN
    cat mysql_dev_setup.sql | sudo mysql -u root -h localhost -p  #password=NULL

    #INSERTING DATA INTO CLOUMNS
    #RUN
    python3 -m db_connection_testing.py
            #OR  for python3.10 RUN 
    python3.10 -m db_connection_testing
        
