import requests
import jenkins
import json
import os
from datetime import datetime

username = "prasanna"
password = "Cts++2014"
jenkins_url = "http://172.31.43.33:9999"

type = os.getenv("type")
#("Enter the Type (job/view/pipeline): ")
if type == "job":

    jenkins_url = jenkins_url
   # username = "prasanna"
   # password = "Cts++2014"
    job_name = raw_input('Enter Job name: ')
    Limit= raw_input('Limit: ')
    #stop_date = datetime.strptime("01.02.2021 0:30", "%d.%m.%Y %H:%M")
    #start_date = datetime.strptime("01.12.2020 17:30", "%d.%m.%Y %H:%M")

    request_url = "{0:s}/job/{1:s}/api/json{2:s}".format(
    jenkins_url,
    job_name,
    "?tree=builds[fullDisplayName,id,number,timestamp]{0," + Limit + "}"
    )

    response = requests.get(request_url, auth=(username, password)).json()
   # builds = []

    #for build in response["builds"]:
    # Convert build timestamp to datetime
 #  build_date = datetime.utcfromtimestamp(build["timestamp"]/1000)
    # Compare build datetime with provided dates range
       # if build_date > start_date and build_date < stop_date:
        # Do stuff with builds which fits dates range
         #builds.append(build)

    print(response)

elif type == "view":
        view_name = raw_input("Enter the View name: ")
        request_url = jenkins_url + "/view/" + view_name + "/api/json?tree=jobs[name]"

        response = requests.get(request_url, auth=(username, password))
        data = response.json()
        #jobs = server.get_jobs(view_name=view_name)
        print ((data['jobs']))


elif type == "pipeline":
        job_name = raw_input('Enter Job name: ')
        build_number=raw_input("Enter build number: ")
        url=jenkins_url + "/job/" + job_name +"/" + build_number + "/wfapi/"
       # username='prasanna'
       # password='Cts++2014'
        response = requests.get(url, auth=(username, password))
        data = response.json()
        print (data['stages'])
        print (data['id'])
        print (data['status'])
