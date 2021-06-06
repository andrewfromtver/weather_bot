#! /bin/bash

echo ''
echo 'Collecting data from log file...'

echo '[' > /weather_bot/tmp/json/bot_users.js
cat /weather_bot/tmp/log/weather_bot.log | grep -E "New user: " | sed -E  's/(.*)New user: {1}(.*)/\2/' | sort -u | while read line; do echo ${line}', '; done >> /weather_bot/tmp/json/bot_users.js
echo ']' >> /weather_bot/tmp/json/bot_users.js

echo '[' > /weather_bot/tmp/json/users_geoloc.js
cat /weather_bot/tmp/log/weather_bot.log | grep -E "Button pressed: Geolocation " | sed -E  's/(.*)Button pressed: Geolocation {1}(.*)/\2/' | sort -u | while read line; do echo ${line}', '; done >> /weather_bot/tmp/json/users_geoloc.js
echo ']' >> /weather_bot/tmp/json/users_geoloc.js

echo 'Data collected in:'
echo '     1. /weather_bot/tmp/json/bot_users.js'
echo '     2. /weather_bot/tmp/json/users_geoloc.js'
echo ''
