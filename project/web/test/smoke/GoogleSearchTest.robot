*** Settings ***
Documentation   Google search test
Resource        .${/}resource.robot
Test Timeout    1 min
Test Setup      setup driver
Test Teardown   destroy driver

*** Test Cases ***
Type in search query field
    [Documentation]    Put Testrail link here
    [Tags]             testrailid=111
    Given navigate to main page
    And main page is opened
    When type in query field    @test_data.search.python_query
#    And click search
    Then result page is opened
    And search query is displayed    @test_data.search.python_query
