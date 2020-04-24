# Microsoft Rewards BOT 

## How to run it

First, install ```requirements.txt``` and Google Chrome.

```
pip install -r requirements.txt
sudo apt-get install google-chrome
```

- Run ```app.py``` to start the bot

> Important: Before running the bot make sure you have enter your microsoft account informations in a file called ```passwd.json```:

```json
{
    "accounts":[
        {
            "id":1,
            "name":<name>,
            "email":"example@example.org",
            "passwd":"mypassword"
        },
        {
            "id":2,
            "name":<name>,
            "email":"example@example.org",
            "passwd": "mypassword"
        }
    ]
}
```
