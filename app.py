from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from stories import Story, story, stories

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretpassword"
debug = DebugToolbarExtension(app)

# story_data = {
#     {story_name: "Story string"}
#     "" : ""
# }

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
    words = request.args
    html = story.generate(words)
    return render_template("story.html", html=html)


@app.route("/form_2")
def show_form_2():
    """
    uses the story.prompts from the instantiated story 
    """

    words = story.prompts

    return render_template("form_2.html", words=words)


# !
# ?
# *
# //
# todo

@app.route("/story_2")
def generate_story_2():
    """
    generates string story from request arguments
    """

    select_story = request.args.get("select_story")

    selected_story = stories[select_story]

    # todo html = story.generate()

    return render_template("story_2.html", selected_story=select_story)
