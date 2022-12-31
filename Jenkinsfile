pipeline{
    agent any
    stages{
        stage('clone repo'){
            steps{
                git branch: 'main', credentialsId: '7e147454-fec4-42bb-8daf-8741c8e837d0', url: 'git@github.com:Ravi-Shahi/network-automation.git'
            }
        }
        stage('verify'){
            steps{
              sh '''ansible --version
                echo "cloned successfully"'''
            }
        }
    }
}