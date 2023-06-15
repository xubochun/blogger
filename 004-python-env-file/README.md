## Jenkins Pipeline

####  1. 如果你希望隱藏敏感的環境變數值，可以在 Jenkins 中使用 Credential 插件來管理這些敏感資訊。Credential 插件可以將敏感資訊加密並儲存起來，只有授權的使用者可以解密和存取這些資訊。
```Jenkinsfile
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'my-credentials', usernameVariable: 'USER_NAME', passwordVariable: 'USER_PASSWORD')]) {
                    sh 'echo $USER_NAME'
                    sh 'echo $USER_PASSWORD'
                }
            }
        }
    }
}
```
此時，`.env.bate`需要修改如下:
```
USER_NAME=${USER_NAME}
USER_PASSWORD=${USER_PASSWORD}
```
最後，以下是 Jenkins pipeline:
```
pipeline {
    agent {
        label 'jenkins_agent1'
    }
    
    environment {
        USER_NAME = credentials('my-credentials')
        USER_PASSWORD = credentials('my-credentials')
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Xubochun/blogger'
            }
        }
        
        stage('Run example.py') {
            steps {
                dir('004-python-env-file') {
                    bat "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310\\python.exe example.py ${USER_NAME} ${USER_PASSWORD}"
                }
            }
        }
    }
}
```

#### 2. 設定 parameters 的方式來存取 API_KEY，缺點是每次執行 Jenkins Pipeline 時都得要重新輸入一次 API_KEY。
```jenkinsfile
pipeline {
    agent {
        label 'jenkins_agent1'
    }
    
    parameters {
        string(defaultValue: '123456', description: 'Enter the API key', name: 'api_key')
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Xubochun/blogger'
            }
        }
        
        stage('Move to 004-python-env-file') {
            steps {
                // 使用 dir 步驟移動到指定資料夾
                dir('004-python-env-file') {
                    // 使用 bat 步驟以命令的方式獲取當前路徑
                    bat 'echo %CD%'
                    bat 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310\\python.exe example.py %api_key%'
                }
            }
        }
    }
}
```
