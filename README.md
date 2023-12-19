# Discord_Bot_Intergration
Creating a Discord bot by using python and mysql integration

1.) Create discord application from **https://discord.com/developers/applications** 

2.) After creating application go to **Bot section** and generate a token by clicking on **reset token** and save that token to use it later in python program.

3.) After this go to **URL generator** section and generate a URl by giving required permission to the bot which will be used later to invite bot to your server.
**note:** Give atleast read and send message permission.

4.) Now run the Database creation file code in the MySQL terminal to create database and table which will store the **server id** and **auth token**.

5.) After this go to your IDE and follow the next steps.

**note:** Before running the flask_server.py file update this **mysql://Your Username:Your Password@localhost/discord_bot'** string with your username and password of MySQL DBMS.

6.) Now run the **flask_server.py** file which will create a server and connect database to your bot.

**note:** Before running the test_bot.py add your token which you saved earlier in the TOKEN variable **TOKEN = 'YOUR Discord Bot Token'**

7.) Now run the **test_bot.py** in command shell in your IDE file which will successfully create and connect your bot to the flask server and discord.

8.) Now go to the browser and take the **URL** which you saved while creating the bot and with the help of that **invite bot** to your server.

9.) After all the above steps you can see that when bot was joined it gave the default message as **hello world! your server name**.

10.) Now to interact with bot in the server you can create multiple commands but for now I have only created one command which is **!hello** to which bot will respond **hello world, your server name**.
