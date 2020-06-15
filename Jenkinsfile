pipeline{
    agent any
    enviroment {
        app_version = "2.01"
        rollback = "false"
    }
    stages{
        stage("Make allk scripts executable"){
            steps{
                sh 'chmod +x ./script/*'
            }
        }
        stage("Source variables"){
            steps{
                sh './script/source.sh'
            }
        }
        stage("Deploy Docker Swarm Stack"){
            steps{
                sh './script/docker.sh'
            }
        }
    }
}