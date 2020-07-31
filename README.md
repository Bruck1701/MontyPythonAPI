# MontyPythonAPI
#### A Flask Restful API with Gunicorn in Docker. 
 ...And now for a completely different API. <br> 
This is an API that returns dialogues from random episodes of Monty Pyhon and generate new material based on the content of the dialogues and political speeches.
 
To run the API locally, you need to set the $PORT environment (added to the Dockerfile to be able to run it on Heroku)
```
docker run -p 8000:8000 -e PORT=8000 bruck1701/montypython_api 
```
This API has two endpoints: 
```
/get/original
/get/new_material
```
The /get/original endpoint returns a dialogue from a random episode of the show.

Example of result:
```
/get/original 
```
```
{
    "episode": 10,
    "sketch": "Bank robber (lingerie shop)",
    "dialogue": [
        "Good morning, I am a bank robber. Er, please don't panic, just hand over all your money.",
        "This is a lingerie shop, sir.",
        "Fine, fine, fine.",
        "Adopt, adapt and improve. Motto of the round table. Well, um ... what have you got?",
        "Er, we've got corsets, stockings, suspender belts, tights, bras, slips, petticoats, knickers, socks and garters, sir.",
        "Fine, fine, fine, fine. No large piles of money in safes?",
        "No, sir.",
        "No deposit accounts?",
        "No sir.",
        "No piles of cash in easy to carry bags?",
        "None at all sir.",
        "No luncheon vouchers?",
        "Fine, fine. Well, um... adopt, adapt and improve. Just a pair of knickers then please."
    ]
}
```


The /get/new_material endpoint returns Markov chain generated political speech with a little twist: It mixes a random US president's speech with a random dialogue from Monty Python! To generate a random dialogue alone was a bit confusing, but as a political speech, it does sound like something you would hear in a Monty Python episode, or from a deranged politician. :)
Example:
```
/get/new_material
```
```
{
    "author": "harding",
    "date": "July 22, 1920",
    "title": "High Wages for High Production",
    "episode": "Lumberjack song",
    "new_speech": "... I am ready to acclaim the highest essential to human happiness. In conflict is disaster, in understanding there is a minimum production when our need is maximal. The destruction of one unavoidably involves the other. I cut down trees, He eats his lunch, He goes to the people and their obligation to the foundation on which industry is bigger than any element in its modern making. In bars??????? I chop down trees, I eat my lunch, I go shopping, And have buttered scones for tea. The suspicion or rebellion of one is the call of America. I am ready to acclaim the highest essential to human happiness. Well I object to all this sex on the necessity for understanding, particularly that understanding that concerns ourselves at home. He cuts down trees, I eat my lunch, I go shopping, And have buttered scones for tea. I wish to complain in the strongest possible terms about the lumberjack who wears women's clothes. The destruction of one is the call of America. I am speaking as one who has counted the contents of the millions of American wage earners. I want the wage earners of America that mounting wages and they abide...."
}
```

A copy of the API is running on: 
```
https://bk-montypython-api.herokuapp.com/
```

I hope this Repo does not get shut down for being too silly... :)
