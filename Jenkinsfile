// Need these outside of environment block or you can't modify them
def BUILD_TARGET = "development"
def BUILD_TAG = "latest"

pipeline {
  agent any

  environment {
    DOCKER_REGISTRY_DEV = ""
    DOCKER_REGISTRY_PROD = ""
    DOCKER_CREDENTIALS_DEV = ""
    DOCKER_CREDENTIALS_PROD = ""
  }

  stages {
    stage('Prep') {
      steps {
        script {
          AUTHOR_NAME = sh(returnStdout: true, script: "git --no-pager show -s --format='%an' ${env.GIT_COMMIT}").trim()
          AUTHOR_EMAIL = sh(returnStdout: true, script: "git --no-pager show -s --format='%ae' ${env.GIT_COMMIT}").trim()
          SHORT_COMMIT = env.GIT_COMMIT.take(7)

          // Build behaviour:
          // Upload images only for releases, release candidates, and dev branch.
          // Releases go in prod registry, the other two in dev.
          // Everything else still gets built and tested, but not uploaded.
          // Variable BUILD_TARGET = (external|internal|development) controls this.
          switch (env.BRANCH_NAME) {
            case ~'^\\d+\\.\\d+(\\.\\d+)?[a-z]?$': // This matches 1.2, 1.2a, 1.2.1, or 1.2.1a
              BUILD_TARGET = "external"
              BUILD_TAG = env.BRANCH_NAME
              break;
            case ~'^release-.*':
              BUILD_TARGET = "internal"
              BUILD_TAG = "${env.BRANCH_NAME.replace("release-", "")}-rc${env.BUILD_NUMBER}"
              break;
            case ~'^dev.*':
              BUILD_TARGET = "internal"
              BUILD_TAG="dev-${SHORT_COMMIT}"
              break;
            default:
              BUILD_TAG="${BRANCH_NAME}-${SHORT_COMMIT}"
              break;
          }

          echo "Author name: ${AUTHOR_NAME}"
          echo "Author email: ${AUTHOR_EMAIL}"
          echo "Branch: ${env.BRANCH_NAME}"
          echo "Build target: ${BUILD_TARGET}"
          echo "Build tag: ${BUILD_TAG}"
        }
      }
    }
    stage('Build image') {
      steps {
        script {
          docker.withRegistry("https://${env.DOCKER_REGISTRY_DEV}", "${env.DOCKER_CREDENTIALS_DEV}") {
            dir("modulename") {
              image = docker.build(
                "appname",
                "--build-arg BASE_IMAGE=${env.DOCKER_REGISTRY_DEV}/base-image:latest ."
              )
            }
          }
        }
      }
    }
    stage("Test") {
      steps {
        script {
          echo "Testing..."
        }
      }
    }
    stage("Publish image") {
      parallel {
        stage("Push to prod") {
          when { expression { BUILD_TARGET == "external" } }
          steps {
            script {
              docker.withRegistry("https://${env.DOCKER_REGISTRY_PROD}", "${env.DOCKER_CREDENTIALS_PROD}") {
                // Double-tag external releases
                image.push("${BUILD_TAG}")
                image.push("latest")
              }
            }
          }
        }
        stage("Push to dev") {
          when { expression { BUILD_TARGET == "internal" } }
          steps {
            script {
              docker.withRegistry("https://${env.DOCKER_REGISTRY_DEV}", "${env.DOCKER_CREDENTIALS_DEV}") {
                image.push("${BUILD_TAG}")
              }
            }
          }
        }
        stage("Don't push") {
          when { expression { BUILD_TARGET == "development" } }
          steps {
            script {
              echo "Development build -- no upload required"
            }
          }
        }
      }
    }
  }
}
