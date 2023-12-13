-------------------------------------KONSTRUCTOR
BAY--------------------------------------------------------------------------
Konstructor Bay is a Platform where a person can find or advertise Construction
materials.


AUTHORS
------
NAME                   EMAIL                   GITHUB

Moses Gitonga  infosec947@gmail.com  <https://github.com/mosesgitonga>

Joseph Kimuchu kimuchukim@gmail.com <https://github.com/KimuchuJr>

Sean Riley Hawkins rileyhawk249@gmail.com <https://github.com/rileyhawk1417>
                        #USAGE:
    #CREATE DATABASE WITH TABLES IN YOUR LOCALHOST
    #RUN
    cat mysql_dev_setup.sql | sudo mysql -u root -h localhost -p  #password=NULL

    #INSERTING DATA INTO CLOUMNS
    #RUN
    python3 -m db_connection_testing.py
            #OR  for python3.10 RUN 
    python3.10 -m db_connection_testing
        

To run the web app
  0. clone the repository
  1. go to the root directory /konstructor_Bay and run "flask run"
  2. On another terminal go to /konstructor_bay frontend and run "pnpm dev"
  3. visit the site on browser on http://localhost:3000
