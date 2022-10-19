pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                checkout([$class           : 'GitSCM',
                          branches         : [[name: 'master']],
                          extensions       : [[$class            : 'RelativeTargetDirectory',
                                               relativeTargewtDir: 'multibranch-sample-app/']],
                          userRemoteConfigs: [[url: 'https://github.com/lancherbai/multibranch-sample-app.git']]])
            }
        }

        stage('Install Package') {
            steps {
                dir("./") {
                    sh 'pip install --user -r requirements.txt'
                }
            }
        }
        stage('Integration Test') {
            steps {
                dir("./") {
                    sh 'pytest --junitxml report.xml'
                }
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
            }
        }
    }
}
