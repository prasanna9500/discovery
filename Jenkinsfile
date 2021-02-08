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
                     sh 'aws s3 cp /var/lib/jenkins/workspace/KKPI/${File_Name}.json s3://jenkins-kpi/'
	    }
		        
	       }
	
}
post {
        always {
           cleanWs()
        }
	}
}
