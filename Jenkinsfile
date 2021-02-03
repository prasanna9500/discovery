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
	
stage('Curl stage') {
      steps {
	      sh 'curl -g -u {$username}:Cts++2014 "http://172.31.43.33:9999/job/Devproj/api/json?tree=builds[url,number,status,timestamp,id,result,duration]{0,4}"'

      }
    }
  }
}
