from flask import Flask, render_template

skills_app = Flask(__name__)

my_skills = [("Python (Flask & Numpy)", 80), ("HTML", 90), ("CSS", 90), ("Illustrator", 95), ("Photoshop", 95), ("Work Experiences & Ambition", 100)]



@skills_app.route("/")
def skills():
  return render_template("skills.html",
                          title="My Skills",
                          page_head="My Skills",
                          description="Welcome to My Skills Page",
                          skills=my_skills
                         )

if __name__ == "__main__":
  skills_app.run(debug=True, port=1989)