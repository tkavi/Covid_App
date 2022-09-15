from flask import Flask,render_template,request
import requests,json,os

app = Flask(__name__)

@app.route('/covid',methods=["GET","POST"])
def covid_info():
    if request.method=='GET':
        return render_template("covid.html")

    if request.method == 'POST':
        country = request.form["country"]
        print(country)

        url = "https://api.covid19api.com/summary"
        print(url)

        response = requests.get(url).json()
        print(response)

        countries_list=response.get("Countries")
        print(countries_list)

        for i in countries_list:
            if i["Country"] == country:
                print(i["Country"])
                data = {"country":country,
                        "TotalConfirmed":i['TotalConfirmed'],
                        "TotalDeaths":i['TotalDeaths']}

                return render_template("covid.html", data=data)
        else:
            return render_template("covid.html", msg="Invalid Entry")

port = int(os.environ.get("PORT",5000))

if __name__=="__main__":
    app.run(port=port)

# https://api.covid19api.com/summary