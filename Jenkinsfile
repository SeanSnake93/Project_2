pipeline {
    agent any
    stages{
        stage('enable all scripts to be Exicutable'){
            steps{
                sh 'chmod +x ./script/*'
            }
        }
        stage('Run installastions'){
            steps{
                sh './script/before_installation.sh'
                sh './script/installation.sh'
            }
        }
        stage('Run Application'){
            steps{
                sh 'sudo systemctl restart flask.service'
            }
        }
    }
}
