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
        sh 'docker build -f cicd/Dockerfile .'
      }
    }

  }
}