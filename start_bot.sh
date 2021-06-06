#! /bin/bash

echo 'Starting Weather bot...'
python3 /weather_bot/src/weather_bot.py&
sleep 2
echo 'Weather bot staerted.........................[ OK ]'
echo 'Log file => /weather_bot/tmp/log/weather_bot.log'

tail -f /weather_bot/tmp/log/weather_bot.log