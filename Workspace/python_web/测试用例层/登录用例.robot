*** Settings ***
Resource    ../页面对象层/登录页面关键字.robot
Variables    ../测试数据层/登录数据.py
Variables    ../测试数据层/公共数据.py
Library    ../myExcelLibrary.py    

# Test Setup    Open Browser    ${web_login_url}    chrome 
Test Teardown    Close Browser    

# Default Tags    Demo    #默认标签，如果用例没有标签则使用Demo标签，如果有用自己的
Force Tags    smoke    #包含该设置的测试用例文件中所有用例都被指定打上这些标签

*** Test Cases ***
正常用例-登录成功
    [Tags]    smoke    hhh
    登录页面关键字.登录操作    ${success_data.username}    ${success_data.password}
    #断言
    # Should Be True    元素    #判断元素是否存在    
    
异常用例-用户名为空
    # Log    ${phone_data[0]}  
    # Log    ${phone_data[0]["check"]}    
    # Log    ${phone_data[0].check}    #报错，不能用
    登录页面关键字.登录操作    ${phone_data[2]["username"]}    ${phone_data[2]["password"]}
    ${msg}=    登录页面关键字.获取错误提示提示-来自登录区域    
    Should Be Equal    ${phone_data[2]["check"]}        ${msg}
    
用例3-读取-v参数传进来的全局变量
    [Tags]    VVV
    Log    ${web_url}
    #dos命令运行时传入web_url
    
用例4-使用自定义库的关键字
    [Tags]    my
    ${sum}=    Add Function    12    14
    
         
    
