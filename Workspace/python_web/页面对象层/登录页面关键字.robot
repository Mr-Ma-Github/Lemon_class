*** Settings ***
Library    SeleniumLibrary    
Resource    ../元素定位层/登录页面.robot

*** Keywords ***
登录操作
    [Arguments]    ${用户名}    ${密码}
    Wait Until Element Is Visible    ${用户名输入框}    20
    Input Text    ${用户名输入框}    ${用户名}    
    Input Text    ${密码输入框}    ${密码}    
    Click Element    ${登录按钮}     
    
获取错误提示提示-来自登录区域
    Wait Until Element Is Visible    ${错误提示-登陆表单区域}    20
    ${msg}=    Get Text    ${错误提示-登陆表单区域}
    [Return]    ${msg}
    
获取错误提示提示-页面正中间
    Wait Until Element Is Visible    ${页面正中间的提示框}    20
    ${msg}=    Get Text    ${页面正中间的提示框}
    [Return]    ${msg}