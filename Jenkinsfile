pipeline{
    agent any
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
        stage("Deploy Swarm Stack"){
            steps{
                sh './script/docker.sh'
            }
        }
    }
}