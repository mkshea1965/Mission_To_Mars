#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import Scraping


# In[3]:


app = Flask(__name__)


# In[4]:


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# In[5]:


@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


# In[6]:


@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)


# In[ ]:


if __name__ == "__main__":
   app.run()

