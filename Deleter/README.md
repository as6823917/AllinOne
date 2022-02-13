# Auto-Delete
Simple Telegram UserBot To Delete Group Messages After Specific Time.
Based on Pyrogram

## Deploy on Heroku
 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
- DON'T FORGET TO TURN ON DYNOS IN HEROKU
## Deploy in your VPS

```sh
git clone https://github.com/Arun-TG/AutoDelete
cd AutoDelete
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 sam.py
```


### Variables:
1. `API_ID` : Get From [my.telegram.org](https://my.telegram.org/)
2. `API_HASH` : Get from [my.telegram.org](https://my.telegram.org)
3. `ADMINS` : ID of Admins (Userbot will not delete Messages of Admins)
4. `SESSION` : Generate From here [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://repl.it/@subinps/getStringName)
5. `GROUPS` : ID of Groups where the userbot works.
6. `TIME` : Time Duration for deletion

#
- In [Main](https://github.com/Arun-TG/AutoDelete/tree/main) Branch UserBot will delete all message of Users & Bots.
- If you want to delete Messages Sent By Users Only Deploy [Second](https://github.com/Arun-TG/AutoDelete/tree/Second) Branch 

# Credits
- [Pyrogram](https://github.com/pyrogram/pyrogram)
- [Abir Hasan](https://github.com/AbirHasan2005)
- [SUBIN](https://github.com/subinps)
- [Me](https://t.me/Arun_TG)

* Inspiration➔ [Ten Seconds Delete](https://t.me/TenSecBot)
