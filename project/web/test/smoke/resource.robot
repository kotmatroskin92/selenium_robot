*** Settings ***
Resource          ..${/}..${/}resource${/}resource.robot


*** Keywords ***
setup driver
    [Timeout]    1 min
    CommonSteps.Setup driver steps

destroy driver
    CommonSteps.Destroy driver steps
