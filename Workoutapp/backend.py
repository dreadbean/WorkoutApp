from flask import Flask, redirect,url_for,render_template,request,session,flash
from datetime import time, timedelta


app= Flask(__name__)
app.secret_key= "hellow"
app.permanent_session_lifetime= timedelta(minutes=5)


    




@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Workoutplan")
def workoutplan():
    return render_template("workoutplan.html")



@app.route("/PlateCalculator",methods=["POST","GET"])
def platecalculator():
    if request.method == "POST":
        session.permanment = True
        inweight = int(request.form["weight"])
        remainder_45 = inweight % 45
        ib_45 = 0
        ib_35 = 0
        ib_25 = 0
        ib_15 = 0
        ib_10 = 0
        ib_5 = 0
        ib_2_5 = 0
        if remainder_45 == 0:
            ib_45=int(inweight/45)
        else:
            ib_45=int(inweight/45)
            inweight = remainder_45
            if inweight % 35 == 0:
                ib_35=inweight/35
            else:
                ib_35=int(inweight/35)
                inweight = inweight % 35
                if inweight % 25 ==0:
                    ib_25=inweight/25
                else:
                    ib_25=int(inweight/25)
                    inweight = inweight %25
                    if inweight % 15 ==0:
                        ib_15 = inweight/15 
                    else:
                        ib_15=int(inweight/15)
                        inweight = inweight %15
                        if inweight % 10 ==0:
                            ib_10 = inweight/10
                        else:
                            ib_10 = int(inweight/10)
                            inweight = inweight%10
        print(str(ib_45)+str(ib_35)+str(ib_25)+str(ib_15)+str(ib_10)) 
    return render_template("PlateCalculator.html",plates = ib_45,plate35=ib_35,plate25=ib_25,plate15=ib_15,plate10=ib_10)


                

    




























if __name__ == "__main__":
    app.run(debug=True)