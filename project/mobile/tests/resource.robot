*** Settings ***
Resource          ..${/}resource${/}resource.robot

*** Keywords ***
Test Setup
    [Documentation]    Initial driver
    [Timeout]    10 min

    Given Init Driver

Test Teardown
    [Documentation]    Close app

    Close App
