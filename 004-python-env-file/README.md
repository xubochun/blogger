## Jenkins Pipeline

```
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
