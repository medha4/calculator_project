# Feel free to code your definitions here in order to separate your concerns.
import requests 
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

state = input ("What state/territory do you live in?"+"\n")
newState = ""
state = state.lower()
if len(state)>2:
    newState+=state[0].upper()
    for i in range (1,len(state)):
        if state[i-1] == " ":
            newState += str(state[i]).upper()
        else:
            newState += state[i]
    state = us_state_abbrev[newState].lower()


print (state)


data = requests.get ("https://covidtracking.com/api/v1/states/{}/current.json".format(state))

def getTotalPosCases():
    posCases = int(data.json()["positive"])
    if (posCases > 200000):
        return ("Your state is in the burgundy zone. The total number of positive cases is " + "{:,}".format (posCases)+ ". Be careful, wear a mask, your state has one of the highest positive cases")
    elif (posCases > 100000):
        return ("Your state is in the crimson zone. The total number of positive cases is " + "{:,}".format (posCases)+ ". Be careful, wear a mask, your state has a high number of positive cases")
    elif (posCases > 50000):
        return ("Your state is in the red zone. The total number of positive cases is " + "{:,}".format (posCases)+ ". Be careful, wear a mask, your state has a high number of positive cases")
    elif (posCases > 20000):
        return ("Your state is in the orange zone. The total number of positive cases is " + "{:,}".format (posCases)+ ". Be careful, wear a mask, your state has a moderate number of positive cases")
    elif (posCases > 10000):
        return ("Your state is in the yellow zone. The total number of positive cases is " + "{:,}".format (posCases)+ ". Be careful, wear a mask, your state has a moderate number of positive cases")
    else:
        return ("Your state is in the green zone. The total number of positive cases is " + "{:,}".format (posCases)+ ". Be careful, wear a mask, your state has a low number of positive cases")

def getDeath():
    return "Total Deaths: " + "{:,}".format (data.json()["death"])


def getHosp():
    hospitalizations = data.json()["hospitalizedCurrently"]
    if (hospitalizations == None):
        return "There is currently no data for current hospitalizations"
    else:
        return "Currently Hospitalized: " + "{:,}".format(hospitalizations)

def getResources ():
    resource = requests.get ("https://covidtracking.com/api/v1/states/{}/info.json".format(state)).json()
    return "Notes: "+resource["notes"] +"\n"+"State Website: "+ resource["covid19Site"]