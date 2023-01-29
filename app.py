from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from stories import Story, story, stories, story1, story2

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretpassword"
debug = DebugToolbarExtension(app)

@app.route("/")
def home_page():
    """
    returns home page template 
    """
    return render_template("base.html")

@app.route("/form")
def show_form():
    """
    uses the story.prompts from the instantiated story 
    """
    words = story.prompts

    return render_template("form.html", words=words)

@app.route("/story")
def generate_story():
    """
    generates string story from request arguments
    """
    words = story.prompts
    html = story.generate(words)
    return render_template("story.html", html=html)

@app.route("/select")
def select_story():
    """
   Display options of stories to choose from 
    """
    return render_template("select.html")

@app.route("/form_2")
def show_form_2():
    """
    uses the story.prompts from the instantiated story 
    """
    storyID = request.args.get("select_story_id")
    #?  if blank == blank:
    #     words = story.prompts
    #     elif blank == blank
    #     words = story1.prompts
    #     elif blank == blank
    #     words = story2.prompts
    chosen_story = stories.get(f"{storyID}")
    words = chosen_story.prompts
    return render_template("form_2.html", words=words, chosen_story=chosen_story, storyID=storyID)


    """
    select page for story
    """


    words = story.prompts
    return render_template("select.html", words=words)

@app.route("/story_2")
def generate_story_2():
    """
    generates story string from request arguments
    """
    storyID = request.args.get("storyID")
    chosen_story = stories.get(f"{storyID}")
    words = request.args
    html = chosen_story.generate(words)

    return render_template("story_2.html", storyID=storyID, words=words, html=html)