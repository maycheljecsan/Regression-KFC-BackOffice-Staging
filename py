id: 00rGCqPX60yPg4fhXw8gaA
projectId: gHMXNt1U0kShPfRxnEWcng
projectName: Maychel KFCStaging-BackOffice
created: 2022-10-04T04:28:43.3880973Z
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
  modificationDate: 2022-09-22T08:45:20.0000000
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
  - id: CDngsAyUFE-BWyWSPxjNFA
    enabled: true
    invertResult: false
    order: 2
    repeat: 1
    type: Action
    elementId: ROww24ab8EyKpYCyJ8K6Yw
    settings:
      sleepTime: -1
      timeout: -1
      sleepTiming: Inherit
      failureBehaviorType: Inherit
      takeScreenshotConditionType: Inherit
    action:
      id: 02d572b2-d610-4700-9ad3-40076ddb9807
      source: System
    parameterMaps: []
    conditions: []
    validations: []
    contexts: []
  - id: pGv_Kbem0Ea9WCre0ZgOdQ
    enabled: true
    invertResult: false
    order: 3
    repeat: 1
    type: Action
    elementId: ROww24ab8EyKpYCyJ8K6Yw
    settings:
      sleepTime: -1
      timeout: -1
      sleepTiming: Inherit
      failureBehaviorType: Inherit
      takeScreenshotConditionType: Inherit
    action:
      id: 6f94fdaa-0041-4265-b73b-ecfcbe702d66
      source: System
    parameterMaps:
    - name: keys
      value: admin@dana.ffi.co.id
      direction: Input
    conditions: []
    validations: []
    contexts: []
  - id: jk7ZhMlCW0OnIioRBU5e4w
    enabled: true
    invertResult: false
    order: 4
    repeat: 1
    type: Action
    elementId: oRq8cfJgg0qjVnAjMWISFg
    settings:
      sleepTime: -1
      timeout: -1
      sleepTiming: Inherit
      failureBehaviorType: Inherit
      takeScreenshotConditionType: Inherit
    action:
      id: 02d572b2-d610-4700-9ad3-40076ddb9807
      source: System
    parameterMaps: []
    conditions: []
    validations: []
    contexts: []
  - id: MM7WKjyCWkWYiWk4mp2EzA
    enabled: true
    invertResult: false
    order: 5
    repeat: 1
    type: Action
    elementId: oRq8cfJgg0qjVnAjMWISFg
    settings:
      sleepTime: -1
      timeout: -1
      sleepTiming: Inherit
      failureBehaviorType: Inherit
      takeScreenshotConditionType: Inherit
    action:
      id: 6f94fdaa-0041-4265-b73b-ecfcbe702d66
      source: System
    parameterMaps:
    - name: keys
      value: 12345678
      direction: Input
    conditions: []
    validations: []
    contexts: []
  - id: fX74cNRDNEyfN98Da1DK4g
    enabled: true
    invertResult: false
    order: 6
    repeat: 1
    type: Action
    elementId: e9-Kq9bGykew-9HS4B1WcQ
    settings:
      sleepTime: -1
      timeout: -1
      sleepTiming: Inherit
      failureBehaviorType: Inherit
      takeScreenshotConditionType: Inherit
    action:
      id: 02d572b2-d610-4700-9ad3-40076ddb9807
      source: System
    parameterMaps: []
    conditions: []
    validations: []
    contexts: []
  - id: aId9lw0ElE6RbiJn08HoXg
    comments: ''
    enabled: true
    invertResult: false
    order: 7
    repeat: 1
    type: Action
    elementId: aT3HWuoElUC4Mk6LP6P8dA
    settings:
      sleepTime: -1
      timeout: -1
      sleepTiming: Inherit
      failureBehaviorType: Inherit
      takeScreenshotConditionType: Inherit
    action:
      id: 02d572b2-d610-4700-9ad3-40076ddb9807
      source: System
    parameterMaps: []
    conditions: []
    validations: []
    contexts: []
  - id: t1ENLbvvBUSacuw0YHxXAw
    enabled: true
    invertResult: false
    order: 8
    repeat: 1
    type: Action
    elementId: 0uLR5zHfeEqGQpyHtIIDyw
    settings:
      sleepTime: -1
      timeout: -1
      sleepTiming: Inherit
      failureBehaviorType: Inherit
      takeScreenshotConditionType: Inherit
    action:
      id: 02d572b2-d610-4700-9ad3-40076ddb9807
      source: System
    parameterMaps: []
    conditions: []
    validations: []
    contexts: []
  parameters:
  - name: ApplicationURL
    description: Auto generated application URL parameter
    value: https://kfcjv-staging-3f3f4.firebaseapp.com/
    type: Input
auxTests: []
elements:
- id: oRq8cfJgg0qjVnAjMWISFg
  name: Login Password Field
  type:
    id: jUwODgyNjAyNzk2NTk1NDY
    name: Textbox
    source: System
  locators:
  - name: CSSSELECTOR
    value: '#password'
    priority: 0
  - name: XPATH
    value: /html/body/div/div/div/form/input[2]
    priority: 3
  - name: XPATH
    value: //input[2]
    priority: 2
  - name: XPATH
    value: //input[@placeholder = 'Password']
    priority: 1
- id: e9-Kq9bGykew-9HS4B1WcQ
  name: Login Sign In Button
  type:
    id: jUwODgyNjAyNzk2NTk1NDc
    name: Button
    source: System
  locators:
  - name: XPATH
    value: >-
      //button[. = '
                  Sign In
                ']
    priority: 1
  - name: XPATH
    value: //button
    priority: 0
  - name: XPATH
    value: /html/body/div/div/div/form/div/div[2]/button
    priority: 2
- id: ROww24ab8EyKpYCyJ8K6Yw
  name: Login Email Field
  type:
    id: jUwODgyNjAyNzk2NTk1NDY
    name: Textbox
    source: System
  locators:
  - name: CSSSELECTOR
    value: '#email'
    priority: 0
  - name: XPATH
    value: //input[@placeholder = 'Email']
    priority: 1
  - name: XPATH
    value: //form/input[1]
    priority: 2
  - name: XPATH
    value: /html/body/div/div/div/form/input[1]
    priority: 3
- id: aT3HWuoElUC4Mk6LP6P8dA
  name: Dashboard
  type:
    id: jUwODgyNjAyNzk2NTk1NjU
    name: span
    source: System
  locators:
  - name: XPATH
    value: //ul/li//span[. = 'Dashboard']
    priority: 0
  - name: XPATH
    value: //div/div/ul[1]/li//span
    priority: 1
  - name: XPATH
    value: /html/body/div/div[1]/div[2]/div/div[1]/div/ul[1]/li/div[1]/span
    priority: 2
- id: 0uLR5zHfeEqGQpyHtIIDyw
  name: Dashboard1
  type:
    id: jUwODgyNjAyNzk2NTk1NjU
    name: span
    source: System
  locators:
  - name: XPATH
    value: //a//span[. = 'Dashboard']
    priority: 0
  - name: XPATH
    value: //div/div/ul[1]/div/ul[1]//span
    priority: 1
  - name: XPATH
    value: /html/body/div/div[1]/div[2]/div/div[1]/div/ul[1]/div/ul[1]/a/li/div/span
    priority: 2
projectParameters: []
addons: []
