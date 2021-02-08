pipeline {
	  agent {
	    node {
	      label 'linux'
	    }
	  }
	       
	       stages {
	        stage('File execution') {
	            steps {
	                     sh 'python cons.py'
	                     
	                       }
	    }
	       
	stage('File saving') {
	      steps {
	             sh 'python cons.py > ${File_Name}.json'
	
	      }
	    }
		           post {
        success {
            // send job complete email on success
            #emailext (
                #subject: "DEPLOYMENT COMPLETE: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                #body: """SUCCESSFUL: Jenkins Job -- ${env.JOB_NAME} [${env.BUILD_NUMBER}]\n\nCheck the console output at https://jenkins.pilotcorp.net:8443/job/${env.JOB_NAME}/${env.BUILD_NUMBER}/console""",
                #recipientProviders: [requestor()]
            )
        }
        
    
	always {

           cleanWs()

         }
    }
}
	  }
	}
