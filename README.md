# Template Python project
Skeleton directory structure for DDD-inspired Python ML project.

General features:
- Domain-driven design concepts (entrypoints, adapters services, domain model).
- Pip-installable project module.
- Test framework based on pytest & DDD concepts.
- Fully containerized and docker-compose'd application.
- Makefile as a main entrypoint, which can be exploited by any CICD executor.
- **Coming soon™:** Sample Jenkinsfile for basic image creation.
- **Coming soon™:** Fetch script (usable with wget/curl).

### Notes
- Logging config does not have a file handler because the app is designed to run inside Docker, and docker already saves its logs to disk.
- Dependencies are specified in `requirements.txt` instead of `pyproject.toml`, because it allows for more efficient caching of Docker images during development.