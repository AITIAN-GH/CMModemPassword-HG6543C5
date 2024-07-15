# CMModem-HG6543C5
获取移动光猫 *HG6543C5* 的管理员密码

Get CMModem-HG6543C5 Admin Password
<br/>
# 步骤      
- 1.找到光猫背后的 MAC 地址，手动去除'-'，得到例如：`00-1A-79-00-00-00 ==> 001A79000000`

- 2.在程序的第8行 `def __init__(self, host="192.168.1.1", port=23, mac_address = "你的MAC地址")` 处，替换上面得到的字符串

- 3.运行脚本 搞定

**注意：**  开始前请先自行安装 `Python` 运行环境，并且开启 `Telnet` 功能
 
<br/>

# 设计思路来源于

[Criogaid/CMModemPasswordRetrieval](https://github.com/Criogaid/CMModemPasswordRetrieval) && [B站 布束砥信](https://www.bilibili.com/read/cv21044770/)

# 许可证

![](https://camo.githubusercontent.com/a8cdaa01ff64ee6059cca8875037664c8f811e5954822ca6e0f112316d28d41a/687474703a2f2f6d6972726f72732e6372656174697665636f6d6d6f6e732e6f72672f70726573736b69742f627574746f6e732f38387833312f706e672f62792d6e632d73612e706e67)

> 本项目遵循互联网的开放、自由、共享的原则，采用CC BY-NC-SA 4.0 许可协议 进行授权。
> 如需转载或引用本项目，请务必遵守许可协议的条款。在您的文章或项目开头部分，必须注明原作者、标注原项目链接，并以同样的方式，即CC BY-NC-SA 4.0许可协议，分享您的作品。
> 任何不遵循 CC BY-NC-SA 4.0 许可协议进行分发的行为，将被视为侵权。
