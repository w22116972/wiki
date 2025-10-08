# CI/CD Pipeline

## Feature branch

- when push commit, then
    1. Test Stage
        - unit test
        - lint test
        - static test
        - volunerability test

## Develop branch

- when pull request from feature branch, then 
    1. Test Stage
        - unit test
        - lint test
        - static test
        - volunerability test
        - **integration test**
- when merged, then 
    1. Build Stage
    2. Deploy to dev env

## Main branch

- when pull request from develop branh, then
    1. Test Stage
        - unit test
        - lint test
        - static test
        - volunerability test
        - integration test
        - end-to-end test
- when merged, then 
    1. Build Stage
    2. Deploy to production env