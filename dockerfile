FROM python:3

# Prepare env.
RUN pip install --no-cache-dir pyowm==3.2.0 pyTelegramBotAPI
RUN mkdir /weather_bot; \
    mkdir /weather_bot/src; \
    mkdir /weather_bot/tmp; \
    mkdir /weather_bot/tmp/json; \
    mkdir /weather_bot/tmp/log; \
    touch /weather_bot/tmp/json/bot_users.js; \
    touch /weather_bot/tmp/json/users_geoloc.js; \
    touch /weather_bot/tmp/log/weather_bot.log

# Copy files
COPY /src/* /weather_bot/src/
COPY /src/start_bot.sh /weather_bot/start_bot.sh
COPY /src/collect_stat.sh /weather_bot/collect_stat.sh

# Chmod scripts
RUN chmod +x /weather_bot/*.sh

CMD [ "/weather_bot/start_bot.sh" ]
