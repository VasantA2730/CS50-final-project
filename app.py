from flask import Flask, redirect, render_template, request, session
import sqlite3 
from helpers import apology
from operator import itemgetter

app = Flask(__name__)
conn=sqlite3.connect('players.db', check_same_thread=False)
db=conn.cursor()

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        top1id = request.form.get("top1")
        top2id = request.form.get("top2")
        jg1id = request.form.get("jg1")
        jg2id = request.form.get("jg2")
        mid1id = request.form.get("mid1")
        mid2id = request.form.get("mid2")
        bot1id = request.form.get("bot1")
        bot2id = request.form.get("bot2")
        sup1id = request.form.get("sup1")
        sup2id = request.form.get("sup2")

        if not top1id or not top2id or not jg1id or not jg2id or not mid1id or not mid2id or not bot1id or not bot2id or not sup1id or not sup2id:
            return apology("Make sure all id's are filled in")
        
        
        try:
            top1= Player(db.execute("SELECT name FROM players WHERE id=:id",{"id":top1id}).fetchall()[0][0],db.execute("SELECT mmr FROM players WHERE id=:id",{"id":top1id}).fetchall()[0][0],db.execute("SELECT id FROM players WHERE id=:id",{"id":top1id}).fetchall()[0][0])
            top2=Player(db.execute("SELECT name FROM players WHERE id=:id",{"id":top2id}).fetchall()[0][0],db.execute("SELECT mmr FROM players WHERE id=:id",{"id":top2id}).fetchall()[0][0],db.execute("SELECT id FROM players WHERE id=:id",{"id":top2id}).fetchall()[0][0])

            jg1=Player(db.execute("SELECT name FROM players WHERE id=:id",{"id":jg1id}).fetchall()[0][0],db.execute("SELECT mmr FROM players WHERE id=:id",{"id":jg1id}).fetchall()[0][0],db.execute("SELECT id FROM players WHERE id=:id",{"id":jg1id}).fetchall()[0][0])
            jg2=Player(db.execute("SELECT name FROM players WHERE id=:id",{"id":jg2id}).fetchall()[0][0],db.execute("SELECT mmr FROM players WHERE id=:id",{"id":jg2id}).fetchall()[0][0],db.execute("SELECT id FROM players WHERE id=:id",{"id":jg2id}).fetchall()[0][0])

            mid1=Player(db.execute("SELECT name FROM players WHERE id=:id",{"id":mid1id}).fetchall()[0][0],db.execute("SELECT mmr FROM players WHERE id=:id",{"id":mid1id}).fetchall()[0][0],db.execute("SELECT id FROM players WHERE id=:id",{"id":mid1id}).fetchall()[0][0])
            mid2=Player(db.execute("SELECT name FROM players WHERE id=:id",{"id":mid2id}).fetchall()[0][0],db.execute("SELECT mmr FROM players WHERE id=:id",{"id":mid2id}).fetchall()[0][0],db.execute("SELECT id FROM players WHERE id=:id",{"id":mid2id}).fetchall()[0][0])

            bot1=Player(db.execute("SELECT name FROM players WHERE id=:id",{"id":bot1id}).fetchall()[0][0],db.execute("SELECT mmr FROM players WHERE id=:id",{"id":bot1id}).fetchall()[0][0],db.execute("SELECT id FROM players WHERE id=:id",{"id":bot1id}).fetchall()[0][0])
            bot2=Player(db.execute("SELECT name FROM players WHERE id=:id",{"id":bot2id}).fetchall()[0][0],db.execute("SELECT mmr FROM players WHERE id=:id",{"id":bot2id}).fetchall()[0][0],db.execute("SELECT id FROM players WHERE id=:id",{"id":bot2id}).fetchall()[0][0])

            sup1=Player(db.execute("SELECT name FROM players WHERE id=:id",{"id":sup1id}).fetchall()[0][0],db.execute("SELECT mmr FROM players WHERE id=:id",{"id":sup1id}).fetchall()[0][0],db.execute("SELECT id FROM players WHERE id=:id",{"id":sup1id}).fetchall()[0][0])
            sup2=Player(db.execute("SELECT name FROM players WHERE id=:id",{"id":sup2id}).fetchall()[0][0],db.execute("SELECT mmr FROM players WHERE id=:id",{"id":sup2id}).fetchall()[0][0],db.execute("SELECT id FROM players WHERE id=:id",{"id":sup2id}).fetchall()[0][0])
        except:
            return apology("Make sure all your ids are valid")

        if not top1 or not top2 or not jg1 or not jg2 or not mid1 or not mid2 or not bot1 or not bot2 or not sup1 or not sup2:
            return apology("Please make sure all your ids are valid")
        teams = []
        #1
        teams.append({"teams":top1.name+" "+jg1.name+" "+mid1.name+" "+bot1.name+" "+sup1.name+" vs "+" "+top2.name+" "+jg2.name+" "+mid2.name+" "+bot2.name+" "+sup2.name, "diff":abs(top1.mmr+jg1.mmr+mid1.mmr+bot1.mmr+sup1.mmr - (top2.mmr+jg2.mmr+mid2.mmr+bot2.mmr+sup2.mmr))})
        #2
        teams.append({"teams":top2.name+" "+jg1.name+" "+mid1.name+" "+bot1.name+" "+sup1.name+" vs "+" "+top1.name+" "+jg2.name+" "+mid2.name+" "+bot2.name+" "+sup2.name, "diff":abs(top2.mmr+jg1.mmr+mid1.mmr+bot1.mmr+sup1.mmr - (top1.mmr+jg2.mmr+mid2.mmr+bot2.mmr+sup2.mmr))})
        #3
        teams.append({"teams":top2.name+" "+jg2.name+" "+mid1.name+" "+bot1.name+" "+sup1.name+" vs "+" "+top1.name+" "+jg1.name+" "+mid2.name+" "+bot2.name+" "+sup2.name, "diff":abs(top2.mmr+jg2.mmr+mid1.mmr+bot1.mmr+sup1.mmr - (top1.mmr+jg1.mmr+mid2.mmr+bot2.mmr+sup2.mmr))})
        #4
        teams.append({"teams":top2.name+" "+jg2.name+" "+mid2.name+" "+bot1.name+" "+sup1.name+" vs "+" "+top1.name+" "+jg1.name+" "+mid1.name+" "+bot2.name+" "+sup2.name, "diff":abs(top2.mmr+jg2.mmr+mid2.mmr+bot1.mmr+sup1.mmr - (top1.mmr+jg1.mmr+mid1.mmr+bot2.mmr+sup2.mmr))})
        #5
        teams.append({"teams":top2.name+" "+jg2.name+" "+mid2.name+" "+bot2.name+" "+sup1.name+" vs "+" "+top1.name+" "+jg1.name+" "+mid1.name+" "+bot1.name+" "+sup2.name, "diff":abs(top2.mmr+jg2.mmr+mid2.mmr+bot2.mmr+sup1.mmr - (top1.mmr+jg1.mmr+mid1.mmr+bot1.mmr+sup2.mmr))})
        #6
        teams.append({"teams":top1.name+" "+jg2.name+" "+mid1.name+" "+bot1.name+" "+sup1.name+" vs "+" "+top2.name+" "+jg1.name+" "+mid2.name+" "+bot2.name+" "+sup2.name,
        "diff":abs(top1.mmr+jg2.mmr+mid1.mmr+bot1.mmr+sup1.mmr - (top2.mmr+jg1.mmr+mid2.mmr+bot2.mmr+sup2.mmr))})
        #7
        teams.append({"teams":top1.name+" "+jg2.name+" "+mid2.name+" "+bot1.name+" "+sup1.name+" vs "+" "+top2.name+" "+jg1.name+" "+mid1.name+" "+bot2.name+" "+sup2.name, "diff":abs(top1.mmr+jg2.mmr+mid2.mmr+bot1.mmr+sup1.mmr - (top2.mmr+jg1.mmr+mid1.mmr+bot2.mmr+sup2.mmr))})
        #8
        teams.append({"teams":top1.name+" "+jg2.name+" "+mid2.name+" "+bot2.name+" "+sup1.name+" vs "+" "+top2.name+" "+jg1.name+" "+mid1.name+" "+bot1.name+" "+sup2.name, "diff":abs(top1.mmr+jg2.mmr+mid2.mmr+bot2.mmr+sup1.mmr - (top2.mmr+jg1.mmr+mid1.mmr+bot1.mmr+sup2.mmr))})
        #9
        teams.append({"teams":top1.name+" "+jg2.name+" "+mid2.name+" "+bot2.name+" "+sup2.name+" vs "+" "+top2.name+" "+jg1.name+" "+mid1.name+" "+bot1.name+" "+sup1.name, "diff":abs(top1.mmr+jg2.mmr+mid2.mmr+bot2.mmr+sup2.mmr - (top2.mmr+jg1.mmr+mid1.mmr+bot1.mmr+sup1.mmr))})
        #10
        teams.append({"teams":top1.name+" "+jg1.name+" "+mid2.name+" "+bot1.name+" "+sup1.name+" vs "+" "+top2.name+" "+jg2.name+" "+mid1.name+" "+bot2.name+" "+sup2.name, "diff":abs(top1.mmr+jg1.mmr+mid2.mmr+bot1.mmr+sup1.mmr - (top2.mmr+jg2.mmr+mid1.mmr+bot2.mmr+sup2.mmr))}) 
        #11
        teams.append({"teams":top1.name+" "+jg1.name+" "+mid2.name+" "+bot2.name+" "+sup1.name+" vs "+" "+top2.name+" "+jg2.name+" "+mid1.name+" "+bot1.name+" "+sup2.name, "diff":abs(top1.mmr+jg1.mmr+mid2.mmr+bot2.mmr+sup1.mmr - (top2.mmr+jg2.mmr+mid1.mmr+bot1.mmr+sup2.mmr))})
        #12
        teams.append({"teams":top1.name+" "+jg1.name+" "+mid2.name+" "+bot2.name+" "+sup2.name+" vs "+" "+top2.name+" "+jg2.name+" "+mid1.name+" "+bot1.name+" "+sup1.name, "diff":abs(top1.mmr+jg1.mmr+mid2.mmr+bot2.mmr+sup2.mmr - (top2.mmr+jg2.mmr+mid1.mmr+bot1.mmr+sup1.mmr))})
        #13
        teams.append({"teams":top1.name+" "+jg1.name+" "+mid1.name+" "+bot2.name+" "+sup1.name+" vs "+" "+top2.name+" "+jg2.name+" "+mid2.name+" "+bot1.name+" "+sup2.name, "diff":abs(top1.mmr+jg1.mmr+mid1.mmr+bot2.mmr+sup1.mmr - (top2.mmr+jg2.mmr+mid2.mmr+bot1.mmr+sup2.mmr))})
        #14
        teams.append({"teams":top1.name+" "+jg1.name+" "+mid1.name+" "+bot2.name+" "+sup2.name+" vs "+" "+top2.name+" "+jg2.name+" "+mid2.name+" "+bot1.name+" "+sup1.name, "diff":abs(top1.mmr+jg1.mmr+mid1.mmr+bot2.mmr+sup2.mmr - (top2.mmr+jg2.mmr+mid2.mmr+bot1.mmr+sup1.mmr))})
        #15
        teams.append({"teams":top1.name+" "+jg1.name+" "+mid1.name+" "+bot1.name+" "+sup2.name+" vs "+" "+top2.name+" "+jg2.name+" "+mid2.name+" "+bot2.name+" "+sup1.name, "diff":abs(top1.mmr+jg1.mmr+mid1.mmr+bot1.mmr+sup2.mmr - (top2.mmr+jg2.mmr+mid2.mmr+bot2.mmr+sup1.mmr))})

        t = min(teams, key=lambda x: x["diff"])

        return render_template("teams.html",teams=t["teams"])

@app.route("/search", methods=["GET","POST"])
def search():
    if request.method == "GET":
        return render_template("search.html")
    else:
        ids = request.form.get("id").split(",")
        if not ids:
            return apology("Please input at least one valid id")
        results=[]
        for id in ids:
            player=db.execute("SELECT * FROM players WHERE id=:id",{"id":id}).fetchall()
            if not player:
                return apology("Make sure you are entering valid ids")
            name = player[0][1]
            mmr= player[0][2]
            results.append({name:mmr})
        return render_template("searched.html",results=results)

@app.route("/update", methods=["GET","POST"])
def update():
    if request.method == "GET":
        return render_template("update.html")
    else:
        id = request.form.get("id")
        value = request.form.get("value")

        if not id or not value:
            return apology("Please enter a value and id")

        player=db.execute("SELECT * FROM players WHERE id=:id",{"id":id}).fetchall()
        if not player:
            return apology("Please enter a valid id")
        
        db.execute("UPDATE players SET mmr=:mmr WHERE id=:id",{"mmr":value,"id":id})
        conn.commit()
        return redirect("/")

class Player:
    def __init__(self,name,mmr,id):
        self.name=name
        self.mmr=int(mmr)
        self.id=int(id)
        