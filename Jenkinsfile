pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/txhanh/jenkins', branch: 'main')
      }
    }

    stage('Logs') {
      steps {
        sh 'ls -la'
      }
    }

    stage('Build') {
      steps {
        sh 'docker build . -t flask:1.0 -f cicd/Dockerfile'
      }
    }

    stage('Login to DockerHub') {
      environment {
        DOCKERHUB_USER = 'hankxyzt'
        DOCKERHUB_PASSWORD = 'XuanHanh99%'
      }
      steps {
        sh 'docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASSWORD'
      }
    }

  }
}