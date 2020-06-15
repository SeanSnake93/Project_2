pipeline{
    agent any
    enviroment {
        app_version = "1.01"
        rollback = "false"
    }
    stages{
        stage("Make scripts executable"){
            steps{
                sh 'chmod +x ./script/*'
            }
        }
        stage("Deploy Docker Swarm Stack"){
            steps{
                sh './script/docker.sh'
            }
        }
    }
}