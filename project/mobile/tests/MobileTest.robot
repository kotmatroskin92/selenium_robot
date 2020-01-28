*** Settings ***
Documentation   Application autotests
Resource        .${/}resource.robot
Test Timeout    15 min
Test Setup      Test Setup
Test Teardown   Test Teardown


*** Test Cases ***
Application Test
    [Documentation]    Mobile test name
    [Tags]             testrailid=111    priority=high

    When Search Car    @test_data.car
    Then message is displayed    @locale.screen.start.not_found_err
