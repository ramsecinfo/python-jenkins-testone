pipeline {

    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: '9d2b9d98-759e-43b1-a298-20d04737cded', url: 'https://github.com/rupokify/python-jenkins-testone.git'
            }
        }

        stage('Prepare') {
            steps {
                sh '${BRBIN}pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '${BRBIN}pytest testRoutes.py'
            }
        }

        stage('SAST') {
            steps {
                sh '${BRBIN}safety check'
            }
        }

        stage('Build') {
            steps {
                script {
                    sh '${ULBIN}docker build -t rupokify/python-jenkins-testone .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dhpass', usernameVariable: 'dhuser')]) {
                        sh '${ULBIN}docker login -u ${dhuser} -p ${dhpass}'
                        sh '${ULBIN}docker push rupokify/python-jenkins-testone'
                    }
                }
            }
        }

    }

}