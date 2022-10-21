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
                    sh 'python3 -m pip install --user -r requirements.txt'
                }
            }
        }
        stage('Integration Test') {
            steps {
                dir("./") {
                    sh 'python3 -m pytest --junitxml ./reports/report_$(date "+%Y%m%d-%H%M%S").xml'
                }
            }
            post {
                always {
                    junit './reports/*.xml'
                }
            }
        }
    }
}
