pipeline {
    options {
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '3', artifactNumToKeepStr: '3'))
    }

    agent {
        node {
            label '<provide a label>'
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
                            sh 'virtualenv venv && source venv/bin/activate && pip install -r test_requirements.txt && cd tests && python -m pytest tests/'
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
                branch 'master'
            }

            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'JENKINS_TEST_SOLUTION',
                secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    sh '$(aws ecr get-login --region ap-south-1 --no-include-email )'
                    script {
            sh 'docker build -t 728937462937.dkr.ecr.ap-south-1.amazonaws.com/${DOMAIN}/${SERVICE_NAME}:dev -f Dockerfile .'
            sh 'docker push 728937462937.dkr.ecr.ap-south-1.amazonaws.com/${DOMAIN}/${SERVICE_NAME}:dev'
            sh 'aws ecs register-task-definition --cli-input-json file://create-ecs-task-dev.json
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