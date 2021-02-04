pipeline {
  agent {
    node {
      label 'linux'
    }
  }
	
	stages {
        stage('Echo Environment Variables') {
            steps {
			sh 'echo "Hello"'
			
			  }
    }
	
stage( 'JOB') {
	when {
                       expression { type == 'job'}
               } 
      steps {
	      sh 'curl -g -u prasanna:Cts++2014 "http://172.31.43.33:9999/job/Devproj/api/json?tree=builds[url,number,status,timestamp,id,result,duration]{0,4}"'

      }
    }
		
stage('View') {
	when {
                       expression { type == 'view'}
               } 
      steps {
	      //sh 'curl -g -u prasanna:Cts++2014 "http://172.31.43.33:9999/view/trips/api/json?tree=jobs[name,url,builds[number,result,timestamp,duration]{0,1}]"'
	      sh 'python cons1.py'

      }
    }	
		stage('Pipeline') {
	when {
                       expression { type == 'Pipeline'}
               } 
      steps {
	      sh 'curl -g -u prasanna:Cts++2014 "http://172.31.43.33:9999/job/Demo2/13/wfapi/"'
      }
    }
		
  }
}
