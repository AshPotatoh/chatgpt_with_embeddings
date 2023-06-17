## GPT With Embeddings

##### A set of basic scripts that let you create embeddings, store them in json, and retrieve them 

To get started clone the repo and run 

```
pip install -r requirements.txt
```

To install the necessary pip requirements. 

I have commented the code so it should be fairly simple.  

##### Scraping

scraper.py is a selenium scraper, feel free to use it and input your own URL and disallowed words to filter it.  Currently it is set to grab the id 'main'. If you want to change that, the code for writing to the text files starts on line 67. This is fully commented in the code as well.

##### Get your embeddings

Now that you got a bunch of  text files, if they're not already in a folder labled 'data', move them into a data folder. At the same time create a folder named storage. This folder will hold your embeddings.

run `python3 get_embeddings.py` and it should grab them. These are really cheap. If you get an error, this is likely either 

- You didn't set you ENV variables (name should be OPENAI_API_KEY)
- You don't have a paid OpenAI account. 

##### Lets talk to the bot

It is time! 

run `streamlit run app.py` and the site should start running. The terminal should also give you a link for the webapp.

If the results seem weird, try playing with the `temperature` and the `overlap` settings in chatbot.py

If you find the results slow, it could be for a LOT of reasons. This was just created to explore how embeddings and GPT work.
