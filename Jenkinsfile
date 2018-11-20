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
        archiveArtifacts(artifacts: '**/*', defaultExcludes: true)
      }
    }
    stage('Report') {
      steps {
        slackSend(message: 'Test of Blue Ocean task', botUser: true, teamDomain: 'chromatic')
      }
    }
  }
}