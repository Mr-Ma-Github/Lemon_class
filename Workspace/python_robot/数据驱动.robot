*** Settings ***
Test Template    两数求和

*** Keywords ***
两数求和
    [Arguments]    ${a}    ${b}    ${expected}
    ${sum}    Evaluate    ${a}+${b}
    Should Be Equal As Numbers    ${expected}    ${sum}
            
*** Test Cases ***    num1    num2    expected_sum
个位数求和    2    6    8
两位数求和    22    44    66
小数点求和    0.33    0.44    0.77