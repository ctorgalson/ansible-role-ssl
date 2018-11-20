pipeline {
  agent {
    node {
      label 'master'
    }

  }
  stages {
    stage('Script') {
      steps {
        input 'Git branch'
      }
    }
  }
}