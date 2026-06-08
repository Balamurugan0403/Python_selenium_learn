pipeline {
    agent any
    triggers {
        pollSCM('H/5 * * * *')
    }
    stages {
        stage('Clone Code') {
            steps {
                bat 'git config --global http.sslVerify false'
                bat 'if exist Python_selenium_learn (rmdir /s /q Python_selenium_learn)'
                bat 'git clone https://github.com/Balamurugan0403/Python_selenium_learn.git'
            }
        }
        stage('Setup Python') {
            steps {
                bat 'C:\\Users\\ksman\\AppData\\Local\\Programs\\Python\\Python314\\python.exe -m venv myselenium'
                bat 'myselenium\\Scripts\\pip.exe install selenium webdriver-manager'
            }
        }
        stage('Run Selenium Tests') {
            steps {
                bat 'myselenium\\Scripts\\python.exe Python_selenium_learn\\registerexistingemail.py'
            }
        }
    }
    post {
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}