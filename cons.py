import requests
import jenkins
import json
import os
from datetime import datetime

username = "prasanna"
password = "Cts++2014"
jenkins_url = "http://172.31.43.33:9999"
proj_list = []

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
    "?tree=jobs[name{0," + Limit + "}]"
    )
    response = requests.get(request_url, auth=(username, password)).json()
    print(response)
    job_list = response['jobs']
    for n in job_list:
       proj_list.append(n['name'])
    print(proj_list)
    for job_name in proj_list:
        j_name = job_name       
        url=jenkins_url + "/job/" + str(j_name) +"/" + "lastBuild" + "/wfapi/"
        #print(url)
        response1 = requests.get(url, auth=(username, password))
        data1 = response1.json()
        print (data1['stages'])


          
elif Type == "Pipeline":
        job_name = os.getenv("Jobname")
        build_number= os.getenv("Buildnumber")
        url=jenkins_url + "/job/" + job_name +"/" + build_number + "/wfapi/"
        response = requests.get(url, auth=(username, password))
        data = response.json()
        print (data['stages'])
        #print (data['id'])
       # print (data['status'])


