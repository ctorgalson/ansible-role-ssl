pipeline {
  agent {
    node {
      label 'master'
    }

  }
  stages {
    stage('error') {
      steps {
        sh 'ls -hal $WORKSPACE'
      }
    }
  }
}