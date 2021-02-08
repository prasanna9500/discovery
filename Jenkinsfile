pipeline {
   agent { label 'linux' }

  
    }
	
	stages {
        stage('Echo Environment Variables') {
            steps {
			sh echo "Hello"
			
			  }
    }
	
stage('Python execution') {
      steps {
        sh 'python cons.py'

      }
    }
	stage('Saving output file') {
      steps {
        sh 'python cons.py > groovy.json'

      }
    }
  }
}