import requests
import jenkins
import json
import os
from datetime import datetime

username = "prasanna"
password = "Cts++2014"
jenkins_url = "http://172.31.43.33:9999"

Type = os.getenv("Type")
if Type == "Job":

    jenkins_url = jenkins_url
    job_name = os.getenv("Jobname")
    Limit= os.getenv("Limit")
    request_url = "{0:s}/job/{1:s}/api/json{2:s}".format(
    jenkins_url,
    job_name,
    "?tree=builds[fullDisplayName,id,number,timestamp]{0," + Limit + "}"
    )

    response = requests.get(request_url, auth=(username, password)).json()
    print(response)

elif Type == "View":
    jenkins_url = jenkins_url
    view_name = os.getenv("Jobname")
    Limit= os.getenv("Limit")
    request_url = "{0:s}/view/{1:s}/api/json{2:s}".format(
    jenkins_url,
    view_name,
    "?tree=jobs[name,url,builds[number,result,timestamp,duration]{0," + Limit + "}]"
    )
    response = requests.get(request_url, auth=(username, password)).json()
    print(response)


elif Type == "Pipeline":
        job_name = os.getenv("Jobname")
        build_number= os.getenv("Buildnumber")
        url=jenkins_url + "/job/" + job_name +"/" + build_number + "/wfapi/"
        response = requests.get(url, auth=(username, password))
        data = response.json()
        print (data['stages'])
        print (data['id'])
        print (data['status'])
