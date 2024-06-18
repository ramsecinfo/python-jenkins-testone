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

       stage('Deploy') {
            steps {
                // Deploy steps, if any (for example, pushing the Docker image to a registry)
                script {
                    sh '''
                        # Example: Push Docker image to registry
                        docker tag my-python-app my-registry/my-python-app:latest
                        docker push my-registry/my-python-app:latest
                    '''
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
