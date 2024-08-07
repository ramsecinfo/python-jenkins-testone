pipeline {

    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: '9d2b9d98-759e-43b1-a298-20d04737cded', url: 'https://github.com/ramsecinfo/python-jenkins-testone.git'
            }
        }

        stage('Prepare') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

		stage('Test') {
            steps {
                sh 'pytest testRoutes.py'
            }
        }
	    
         stage('Static Code Analysis - SAST') {
            steps {
                script {
                    // Run Bandit for SAST
                    def banditResults = sh(script: 'bandit -r .', returnStatus: true)
                    if (banditResults != 0) {
                        currentBuild.result = 'UNSTABLE'
                                           }
                }
            }
        }

        stage('OWASP SCA') {
            steps {
                dependencyCheck additionalArguments: '', odcInstallation: 'OWASP-Dependency-Scan'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }
	    

        stage('Build') {
            steps {
                script {
                    sh 'docker build -t rupokify/python-jenkins-testone .'
                }
            }
        }

		stage('Trivy DAST') {
            steps {
                script {
                    sh 'trivy image rupokify/python-jenkins-testone:latest'
                }
            }
        }

    }

}
