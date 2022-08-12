# Gitlab SAST to Codeclimate report converter

### SAST example:
```
sast:
  stage: test
  after_script:
    - mv gl-sast-report.json $CI_JOB_NAME.json
  artifacts:
    paths:
      - $CI_JOB_NAME.json
  allow_failure: true
```
