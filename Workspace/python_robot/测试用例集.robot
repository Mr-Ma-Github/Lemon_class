*** Settings ***
Library    DateTime    
Resource    用户关键字集.robot
Variables    外部变量.py

*** Keywords ***
# 两数求和
    # [Arguments]    ${a}    ${b}
    # [Documentation]    实现a+b。并输出结果
    # ...    
    # ...    a：数字1
    # ...    
    # ...    b：数字2
    # ...    
    # ...    作者：小简
    # ...    
    # ...    时间：2020-07-09 23:48
    # ${sum}    Evaluate    ${a}+${b}
    # [Return]    ${sum}
    
内层循环
    FOR    ${index}    IN RANGE   2    10    2 
        Log    ${index}
        Exit For Loop If    "${index}"=="RF"   
        END
        
*** Variables ***
${HH}    Hello,world
@{list_1}    12    34    55    78
${dict_2}    key=value    hello=world    you=me

*** Test Cases ***
用例1用RF输入hello-world
    log    Hello,world!    #Normal info message
    Log    warning,world!    #warning
    
用例2-RF当中的异常处理
    ${status}=    Run Keyword And Return Status    log    Hello,world!
    
用例3-获取当前时间
    ${date}=    Get Current Date    
    
用例4-两数求和
    ${sum}=    两数求和    2    12
    
用例5-RF变量
    #RF-Variable:变量
    #变量类型
    #每个变量都可以用   变量标识符{变量名}
    #1）scalar变量：${变量名}
    #表示一个数据。 作为参数传递时，表示一个参数
    #2）list变量：@{变量名}
    #表示一组数据，在作为参数传递时，有几个数据就是几个参数
    #3) dict变量：&{变量名}
    #表示一组键值对数据，在作为参数传递时，有几个键值对就是几个参数
    #变量声明
    #底层是python语言实现，所以跟python创建变量类似，
    #变量不需要特定声明，只要有初始化赋值即可使用
    #默认情况下RF里的变量都是字符型的   
    ${hi}=    Set Variable    Hello,RF!
    @{list}=    Create List    a    b    c    #列表
    &{dict}=    Create Dictionary    key=value    foo=bar    #字典
    &{dict1}=    Create Dictionary    key    value    foo    bar    #字典
    Log    ${dict1.foo}       
    Log    ${list}  
    Log    ${list[1]}    
    
    Log    ${HH}    
    Log    ${list_1[2]}    

用例6-从变量文件当中读取变量
    Log    ${var_1}    
    Log    ${mylist[3]}
    Log    ${mydict.world}    
    
用例7-if使用
    ${a}=    Set Variable    hello
    ${b}=    Set Variable    hello
    Run Keyword If    "${a}"=="${b}"    Log    true
    ...    ELSE    Log    false                   
    
    #for循环。    不支持双重for循环，但是可以通过调用一个for循环实现
    @{lista}=    Create List    hello    world    RF    py11
    FOR    ${item}    IN    @{lista} 
        Log    ${item}
        内层循环    #for循环
        Exit For Loop If    "${item}"=="RF"   
        END
    
用例8
    ${flag}=    Set Variable    True    
    ${a}=    Set Variable    0 
    ${a}=    Set Variable If    "${flag}"=="True"    12    ${a}
        

