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
             
        }
        
    
	always {

           cleanWs()

         }
    }
}
	  }
	}
