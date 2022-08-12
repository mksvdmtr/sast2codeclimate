# Gitlab SAST to Codeclimate report converter

### SAST example:
```
include:
  - template: Security/SAST.gitlab-ci.yml

sast:
  stage: test
  after_script:
    - mv gl-sast-report.json $CI_JOB_NAME.json
  artifacts:
    paths:
      - $CI_JOB_NAME.json
  allow_failure: true
```
