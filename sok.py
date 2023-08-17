import requests
import json

def sok_busstopp(sokestreng):
    busstopp= sokestreng
    sted_url= f'https://api.entur.io/geocoder/v1/autocomplete?text={busstopp}&size=10&lang=no'
    sted_r= requests.get(sted_url)
    if sted_r.status_code != 200:
        return None
    else:


        sted= sted_r.json()
        data= sted['features']

        valg=[]

        for d in data:
            p= d['properties']
            pi= p['id']
            if 'NSR:StopPlace' in pi:
                pik= pi.split(':')
                nr=pik[-1]
                v={
                    'navn':p['name'],
                    'sted': p['locality'],
                    'fylke':p['county'],
                    'NRS_id': nr
                }
                valg.append(v)
        return valg

def sok_avgang(id):
    url= 'https://api.entur.io/journey-planner/v3/graphql'
    header= {
        'Content-Type': 'application/json',
        'ET-Client-Name': 'stian-app'
    }
    idd= id
    body= r'{"query":"\n\n{\n  stopPlace(id: \"NSR:StopPlace:'+idd+r'\") {\n    id\n    name\n    estimatedCalls(timeRange: 72100, numberOfDepartures: 10) {     \n      realtime\n      aimedArrivalTime\n      aimedDepartureTime\n      expectedArrivalTime\n      expectedDepartureTime\n      date\n      destinationDisplay {\n        frontText\n      }\n      quay {\n        id\n      }\n      serviceJourney {\n        journeyPattern {\n          line {\n            id\n            name\n            transportMode\n          }\n        }\n      }\n    }\n  }\n}\n","variables":null}'

    test= requests.post(url, headers=header, data=body)
    if test.status_code !=200:
        return None
    else:    
        noe=test.json()
        data= noe['data']['stopPlace']
        return data