from flask import Flask, render_template, url_for, flash, redirect
from forms import PredictionForm
import pandas as pd
import sklearn
import pickle


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

model = pickle.load(open("flight_rf.pkl", "rb"))
posts = [
    {
        'heading': 'Flight Price Prediction',
        'title': 'Welcome!!',
        'content': 'You want to book your flight ticket at low price but dont know when to book??? '   ,
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/predicted", methods=['GET', 'POST'])
def predicted():
    error = None
    form = PredictionForm()
    if form.validate_on_submit():
        if form.validate_time():
            if form.validate_dest():
                if form.validate_curr_dep_time():
                    if form.validate_curr_arr_time():
                        flash(f'Great Job! Predicted Successfully!')
                        # Date_of_Journey
                        date_dep = form.Dep_Time.data
                        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
                        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
                        # print("Journey Date : ",Journey_day, Journey_month)

                        # Departure
                        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
                        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
                        # print("Departure : ",Dep_hour, Dep_min)

                        # Arrival
                        date_arr = form.Arrival_Time.data
                        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
                        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
                        # print("Arrival : ", Arrival_hour, Arrival_min)

                        # Duration
                        dur_hour = abs(Arrival_hour - Dep_hour)
                        dur_min = abs(Arrival_min - Dep_min)
                        # print("Duration : ", dur_hour, dur_min)

                        # Total Stops
                        Total_stops = int(form.Stops.data)
                        # print(Total_stops)

                        # Airline
                        # AIR ASIA = 0 (not in column)
                        airline=form.airline.data
                        if(airline=='Jet Airways'):
                            Jet_Airways = 1
                            IndiGo = 0
                            Air_India = 0
                            Multiple_carriers = 0
                            SpiceJet = 0
                            Vistara = 0
                            GoAir = 0
                            Multiple_carriers_Premium_economy = 0
                            Jet_Airways_Business = 0
                            Vistara_Premium_economy = 0
                            Trujet = 0 

                        elif (airline=='IndiGo'):
                            Jet_Airways = 0
                            IndiGo = 1
                            Air_India = 0
                            Multiple_carriers = 0
                            SpiceJet = 0
                            Vistara = 0
                            GoAir = 0
                            Multiple_carriers_Premium_economy = 0
                            Jet_Airways_Business = 0
                            Vistara_Premium_economy = 0
                            Trujet = 0 

                        elif (airline=='Air India'):
                            Jet_Airways = 0
                            IndiGo = 0
                            Air_India = 1
                            Multiple_carriers = 0
                            SpiceJet = 0
                            Vistara = 0
                            GoAir = 0
                            Multiple_carriers_Premium_economy = 0
                            Jet_Airways_Business = 0
                            Vistara_Premium_economy = 0
                            Trujet = 0 
                            
                        elif (airline=='Multiple carriers'):
                            Jet_Airways = 0
                            IndiGo = 0
                            Air_India = 0
                            Multiple_carriers = 1
                            SpiceJet = 0
                            Vistara = 0
                            GoAir = 0
                            Multiple_carriers_Premium_economy = 0
                            Jet_Airways_Business = 0
                            Vistara_Premium_economy = 0
                            Trujet = 0 
                            
                        elif (airline=='SpiceJet'):
                            Jet_Airways = 0
                            IndiGo = 0
                            Air_India = 0
                            Multiple_carriers = 0
                            SpiceJet = 1
                            Vistara = 0
                            GoAir = 0
                            Multiple_carriers_Premium_economy = 0
                            Jet_Airways_Business = 0
                            Vistara_Premium_economy = 0
                            Trujet = 0 
                            
                        elif (airline=='Vistara'):
                            Jet_Airways = 0
                            IndiGo = 0
                            Air_India = 0
                            Multiple_carriers = 0
                            SpiceJet = 0
                            Vistara = 1
                            GoAir = 0
                            Multiple_carriers_Premium_economy = 0
                            Jet_Airways_Business = 0
                            Vistara_Premium_economy = 0
                            Trujet = 0

                        elif (airline=='GoAir'):
                            Jet_Airways = 0
                            IndiGo = 0
                            Air_India = 0
                            Multiple_carriers = 0
                            SpiceJet = 0
                            Vistara = 0
                            GoAir = 1
                            Multiple_carriers_Premium_economy = 0
                            Jet_Airways_Business = 0
                            Vistara_Premium_economy = 0
                            Trujet = 0

                        elif (airline=='Multiple carriers Premium economy'):
                            Jet_Airways = 0
                            IndiGo = 0
                            Air_India = 0
                            Multiple_carriers = 0
                            SpiceJet = 0
                            Vistara = 0
                            GoAir = 0
                            Multiple_carriers_Premium_economy = 1
                            Jet_Airways_Business = 0
                            Vistara_Premium_economy = 0
                            Trujet = 0

                        elif (airline=='Jet Airways Business'):
                            Jet_Airways = 0
                            IndiGo = 0
                            Air_India = 0
                            Multiple_carriers = 0
                            SpiceJet = 0
                            Vistara = 0
                            GoAir = 0
                            Multiple_carriers_Premium_economy = 0
                            Jet_Airways_Business = 1
                            Vistara_Premium_economy = 0
                            Trujet = 0

                        elif (airline=='Vistara Premium economy'):
                            Jet_Airways = 0
                            IndiGo = 0
                            Air_India = 0
                            Multiple_carriers = 0
                            SpiceJet = 0
                            Vistara = 0
                            GoAir = 0
                            Multiple_carriers_Premium_economy = 0
                            Jet_Airways_Business = 0
                            Vistara_Premium_economy = 1
                            Trujet = 0
                            
                        elif (airline=='Trujet'):
                            Jet_Airways = 0
                            IndiGo = 0
                            Air_India = 0
                            Multiple_carriers = 0
                            SpiceJet = 0
                            Vistara = 0
                            GoAir = 0
                            Multiple_carriers_Premium_economy = 0
                            Jet_Airways_Business = 0
                            Vistara_Premium_economy = 0
                            Trujet = 1

                        else:
                            Jet_Airways = 0
                            IndiGo = 0
                            Air_India = 0
                            Multiple_carriers = 0
                            SpiceJet = 0
                            Vistara = 0
                            GoAir = 0
                            Multiple_carriers_Premium_economy = 0
                            Jet_Airways_Business = 0
                            Vistara_Premium_economy = 0
                            Trujet = 0

                        # print(Jet_Airways,
                        #     IndiGo,
                        #     Air_India,
                        #     Multiple_carriers,
                        #     SpiceJet,
                        #     Vistara,
                        #     GoAir,
                        #     Multiple_carriers_Premium_economy,
                        #     Jet_Airways_Business,
                        #     Vistara_Premium_economy,
                        #     Trujet)

                        # Source
                        # Banglore = 0 (not in column)
                        Source = form.Source.data
                        if (Source == 'Delhi'):
                            s_Delhi = 1
                            s_Kolkata = 0
                            s_Mumbai = 0
                            s_Chennai = 0

                        elif (Source == 'Kolkata'):
                            s_Delhi = 0
                            s_Kolkata = 1
                            s_Mumbai = 0
                            s_Chennai = 0

                        elif (Source == 'Mumbai'):
                            s_Delhi = 0
                            s_Kolkata = 0
                            s_Mumbai = 1
                            s_Chennai = 0

                        elif (Source == 'Chennai'):
                            s_Delhi = 0
                            s_Kolkata = 0
                            s_Mumbai = 0
                            s_Chennai = 1

                        else:
                            s_Delhi = 0
                            s_Kolkata = 0
                            s_Mumbai = 0
                            s_Chennai = 0

                        # print(s_Delhi,
                        #     s_Kolkata,
                        #     s_Mumbai,
                        #     s_Chennai)

                        # Destination
                        # Banglore = 0 (not in column)
                        Source = form.Destination.data
                        if (Source == 'Cochin'):
                            d_Cochin = 1
                            d_Delhi = 0
                            d_New_Delhi = 0
                            d_Hyderabad = 0
                            d_Kolkata = 0
                        
                        elif (Source == 'Delhi'):
                            d_Cochin = 0
                            d_Delhi = 1
                            d_New_Delhi = 0
                            d_Hyderabad = 0
                            d_Kolkata = 0

                        elif (Source == 'New_Delhi'):
                            d_Cochin = 0
                            d_Delhi = 0
                            d_New_Delhi = 1
                            d_Hyderabad = 0
                            d_Kolkata = 0

                        elif (Source == 'Hyderabad'):
                            d_Cochin = 0
                            d_Delhi = 0
                            d_New_Delhi = 0
                            d_Hyderabad = 1
                            d_Kolkata = 0

                        elif (Source == 'Kolkata'):
                            d_Cochin = 0
                            d_Delhi = 0
                            d_New_Delhi = 0
                            d_Hyderabad = 0
                            d_Kolkata = 1

                        else:
                            d_Cochin = 0
                            d_Delhi = 0
                            d_New_Delhi = 0
                            d_Hyderabad = 0
                            d_Kolkata = 0

                        # print(
                        #     d_Cochin,
                        #     d_Delhi,
                        #     d_New_Delhi,
                        #     d_Hyderabad,
                        #     d_Kolkata
                        # )
                    
                        

                    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
                    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
                    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
                    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
                    #    'Airline_Multiple carriers',
                    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
                    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
                    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
                    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
                    #    'Destination_Kolkata', 'Destination_New Delhi']
                        
                        prediction=model.predict([[
                            Total_stops,
                            Journey_day,
                            Journey_month,
                            Dep_hour,
                            Dep_min,
                            Arrival_hour,
                            Arrival_min,
                            dur_hour,
                            dur_min,
                            Air_India,
                            GoAir,
                            IndiGo,
                            Jet_Airways,
                            Jet_Airways_Business,
                            Multiple_carriers,
                            Multiple_carriers_Premium_economy,
                            SpiceJet,
                            Trujet,
                            Vistara,
                            Vistara_Premium_economy,
                            s_Chennai,
                            s_Delhi,
                            s_Kolkata,
                            s_Mumbai,
                            d_Cochin,
                            d_Delhi,
                            d_Hyderabad,
                            d_Kolkata,
                            d_New_Delhi
                        ]])

                        output=round(prediction[0],2)

                        flash(f'Yo! Your Flight Price is INR {output}', 'success')
                    else:
                        flash(f'Arrival time shoule be greater than current time')
                else:
                    flash(f'Departure time should be greater than current time')
            else:
                flash(f'Source and Destination cities must not be same')
        else:
            flash(f'Arrival Time should be greater than Dep Time')
    #else:
        #flash(f'Invalid input given please try again')

    return render_template('predicted.html', title='predicted', form=form, error=error)





if __name__ == '__main__':
    app.run(debug=True)
