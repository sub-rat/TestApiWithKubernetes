pipeline {
    agent {
    kubernetes {
      label 'jenkins-slave'
      defaultContainer 'jnlp'
      yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: dind
    image: docker:18.09-dind
    securityContext:
      privileged: true
  - name: docker
    env:
    - name: DOCKER_HOST
      value: 127.0.0.1
    image: docker:18.09
    command:
    - cat
    tty: true
  - name: tools
    image: bitnami/git:latest
    command:
    - cat
    tty: true
"""
    }
  }
    environment {
        registry = "subratgyawali/pyproj"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
    stages {
        stage('Cloning our Git') {
            steps {
                container('tools') {
                  sh "git clone https://github.com/sub-rat/TestApiWithKubernetes.git ."
                }
            }
        }
        stage('Building our image') {
            steps{
                container('docker'){
                            sh "until docker ps; do sleep 3; done && docker build -t " + registry + ":$BUILD_NUMBER ."
                        }
                        
            }
        }
        stage('Deploy our image') {
            environment {
                 DOCKERHUB_CREDS = credentials('dockerhub')
            }
            steps{
                container('docker'){
                      sh "docker login --username $DOCKERHUB_CREDS_USR --password $DOCKERHUB_CREDS_PSW && docker push "+ registry + ":$BUILD_NUMBER"
                    }
           }
            
        }
    }
}