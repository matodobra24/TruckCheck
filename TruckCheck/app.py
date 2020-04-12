from flask import Flask, render_template, request, redirect, url_for
import datetime
import time

from TruckChecker import *

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def hello_world():

    if request.method == "POST":
        email = request.form["emailInput"]
        password = request.form["passwordInput"]
        vehicleNumber = request.form["vehicleNumber"]
        unitDesignator = request.form["unitDesignator"]
        mileage = request.form["mileage"]
        logisPhone = request.form['logisPhone']
        portable1 = request.form['portable1']
        portable2 = request.form['portable2']
        portableOxygen = request.form['portableOxygen']
        medicalAir = request.form["medicalAir"]
        mainO2 = request.form["mainO2"]
        lifepack = request.form["lifepack"]
        ivpump = request.form["ivpump"]
        apackLocation = request.form["apackLocation"]
        apack = request.form["apack"]
        apackexp = request.form["apackexp"]
        apackexp = datetime.datetime.strptime(apackexp,"%m/%d/%Y").strftime("%d/%m/%Y")
        drugboxLocation = request.form["drugboxLocation"]
        drugbox = request.form["drugbox"]
        drugboxexp = request.form["drugboxexp"]
        drugboxexp = datetime.datetime.strptime(drugboxexp,"%m/%d/%Y").strftime("%d/%m/%Y")
        rsi = request.form["rsi"]
        rsiexp = request.form["rsiexp"]
        rsiexp = datetime.datetime.strptime(rsiexp,"%m/%d/%Y").strftime("%d/%m/%Y")
        stjoeCards = request.form["stjoeCards"]
        fuelcard = request.form["fuelCard"]
        umCards = request.form["umCards"]


        CheckBot(email,password,vehicleNumber,unitDesignator,mileage,logisPhone,portable1,portable2,portableOxygen,medicalAir,mainO2,lifepack,ivpump,apackLocation,apack,apackexp,drugboxLocation,drugbox,drugboxexp,rsi,rsiexp,stjoeCards,fuelcard,umCards)
        return redirect(url_for("submittedForm"))
    else:
        return render_template('index.html')

@app.route('/submittedForm')
def submittedForm():
    return f"Items have been submitted"


if __name__ == '__main__':
    app.run(debug=True)
