#!/bin/bash
cat *.sql | sudo mysql

flask run  &

#create dummy user
curl -X POST -H "Content-Type: application/json" -d '{"first_name":"John", "second_name":"doe", "username":"johnmaster", "email":"john@example.com", "password":"test123"}' http://127.0.0.1:5000/api/add_user

sleep 2

cd frontend

pnpm dev
