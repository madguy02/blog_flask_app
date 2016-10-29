from flask import Flask, render_template_string, redirect
from sqlalchemy import create_engine, MetaData
from flask.ext.login import UserMixin, LoginManager, \
    login_user, logout_user
from flask.ext.blogging import SQLAStorage, BloggingEngine

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"  
app.config["BLOGGING_URL_PREFIX"] = "/blog"
app.config["BLOGGING_DISQUS_SITENAME"] = "test"
app.config["BLOGGING_SITEURL"] = "http://0.0.0.0:8000"

# extensions
engine = create_engine('sqlite:////tmp/blog.db')
meta = MetaData()
sql_storage = SQLAStorage(engine, metadata=meta)
blog_engine = BloggingEngine(app, sql_storage)
login_manager = LoginManager(app)
meta.create_all(bind=engine)


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

    def get_name(self):
        return "Manish(madguy02)"  # typically the user's name

@login_manager.user_loader
@blog_engine.user_loader
def load_user(user_id):
    return User(user_id)



@app.route("/")
def index():
    #return render_template_string(index_template)
    return redirect("/blog")

#@app.route("/login/")
#def login():
    #user = User("testuser")
    #login_user(user)
    #return redirect("/blog")

#@app.route("/logout/")
#def logout():
    #logout_user()
    #return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=8000, use_reloader=True)
    
