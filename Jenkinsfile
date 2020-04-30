pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        echo '"Testing"'
      }
    }

    stage('build') {
      steps {
        sh 'docker build .'
      }
    }

  }
}