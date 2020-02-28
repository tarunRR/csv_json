pipeline {

    options {
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '3', artifactNumToKeepStr: '3'))
    }

    agent {
        node {
            label 'csv_json'
        }
    }

    stages {
        stage('Unit and Integration Tests') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                 accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'JENKINS_TEST_SOLUTION',
                 secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    withDockerContainer(image: '728937462937.dkr.ecr.ap-south-1.amazonaws.com/python-3.7:latest') {
                        script {
                            sh 'virtualenv venv && source venv/bin/activate && cd tests && pip install -r test_requirements.txt && python -m pytest tests/'
                        }
                    }
                }
            }
        }
        stage('Deploy:dev') {
            environment{
                        DOMAIN='test'
                        SERVICE_NAME='csvtojson'
            }
            when {
                branch 'develop'
            }

            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'JENKINS_TEST_SOLUTION',
                secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    sh '$(aws ecr get-login --region ap-south-1 --no-include-email )'
                    script {

											
					    sh 'docker build -t 728937462937.dkr.ecr.ap-south-1.amazonaws.com/${DOMAIN}/${SERVICE_NAME}:dev -f envsetup/docker/Dockerfile .'
					    sh 'docker push 728937462937.dkr.ecr.ap-south-1.amazonaws.com/${DOMAIN}/${SERVICE_NAME}:dev'
						
					}
				}
			}
        }
		
		stage('CleanWorkspace') {
			steps {
					cleanWs()
			}
		}
    }
}
