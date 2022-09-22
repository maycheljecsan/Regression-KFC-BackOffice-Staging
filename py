id: VxmiAiI9TkuNHZrufpERMQ
projectId: gHMXNt1U0kShPfRxnEWcng
projectName: Maychel KFCStaging-BackOffice
created: 2022-09-22T08:26:30.4460935Z
protocol: 1
tests:
- id: fcSUKkYHTUum80nVAb5L6A
  name: py
  description: ''
  platform: Web
  type: Web
  driverType: Chrome
  version: 0.1
  creationDate: 2022-09-22T08:26:30.0000000
  modificationDate: 2022-09-22T08:26:30.0000000
  settings:
    automationAssistant: true
    appId: jhoxZe3bH0CG9tjx3ikrgw
    stepSleepTime: 500
    stepTimeout: 15000
    stepSleepTiming: Before
    stepFailureBehaviorType: Abort
    stepTakeScreenshotConditionType: Failure
  application:
    id: jhoxZe3bH0CG9tjx3ikrgw
    name: KFC Staging Back Office v2.0
    url: https://kfcjv-staging-3f3f4.firebaseapp.com/
    platform: Web
  steps:
  - id: 0jMiXOJwZ027xDiUd6_txA
    comments: Navigates the specified URL (Auto-generated)
    enabled: true
    invertResult: false
    order: 1
    repeat: 1
    type: Action
    settings:
      sleepTime: -1
      timeout: -1
      sleepTiming: Inherit
      failureBehaviorType: Inherit
      takeScreenshotConditionType: Inherit
    action:
      id: 49c5d8d8-4ba8-42f0-823d-702e6acfb23a
      source: System
    parameterMaps:
    - name: url
      value: '{{ApplicationURL}}'
      direction: Input
    conditions: []
    validations: []
    contexts: []
  parameters:
  - name: ApplicationURL
    description: Auto generated application URL parameter
    value: https://kfcjv-staging-3f3f4.firebaseapp.com/
    type: Input
auxTests: []
elements: []
projectParameters: []
addons: []
