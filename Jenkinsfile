pipeline {
  agent any
  stages {
    stage('test') {
      agent any
      steps {
        echo '"Testing"'
      }
    }

    stage('build') {
      agent any
      steps {
        sh 'docker build .'
      }
    }

  }
}