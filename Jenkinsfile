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
        DOCKERHUB_PASSWORD = 'dckr_pat_F0G5l8Y9mlHm4o9D_xwrG89PQOk'
      }
      steps {
        sh 'docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASSWORD'
      }
    }

    stage('Docker Tag') {
      steps {
        sh 'docker tag flask:2.0 hankxyzt/app-flask:2.0'
      }
    }

    stage('Docker Push') {
      steps {
        sh 'docker push hankxyzt/app-flask:2.0'
      }
    }

  }
}