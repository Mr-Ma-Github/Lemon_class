*** Keywords ***
两数求和
    [Arguments]    ${a}    ${b}
    [Documentation]    实现a+b。并输出结果
    ...    
    ...    a：数字1
    ...    
    ...    b：数字2
    ...    
    ...    作者：小简
    ...    
    ...    时间：2020-07-09 23:48
    ${sum}    Evaluate    ${a}+${b}
    [Return]    ${sum}
    
    #关键字当中-常用的RF标识
    #1.参数：[Arguments]
    #2.返回值：[Return]
    #3.关键字说明：[Documentation]