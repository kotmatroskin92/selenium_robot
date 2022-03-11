*** Settings ***
Resource          ..${/}..${/}resource${/}resource.robot


*** Keywords ***
setup driver
    [Timeout]    1 min
    Setup driver steps

destroy driver
    Destroy driver steps
