pipeline {
  agent {
    node {
      label 'master'
    }

  }
  stages {
    stage('Script') {
      steps {
        sh 'ls -hal "$WORKSPACE" && cat "$WORKSPACE"/Jenkinsfile'
      }
    }
    stage('Archive') {
      steps {
        archiveArtifacts(artifacts: '$WORKSPACE/*', defaultExcludes: true)
      }
    }
  }
}