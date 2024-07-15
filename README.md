# CMModemPassword-HG6543C5
获取移动光猫 *HG6543C5* 的管理员密码

Get CMModem-HG6543C5 Admin Password
<br/>
# 步骤      
- 1.找到`光猫`背后的 **MAC** 地址并手动去除 '-' ，例如：`00-1A-79-00-00-00 ==> 001A79000000`，得到你的MAC字符串`001A79000000`;

- 2.记下`光猫`背后的 **默认终端地址** 格式为`192.168.x.x`，检查是否为 `192.168.1.1`。如果是，下一步；否则，记下你的`默认终端地址`;

- 3.脚本第8行 `(self, host="192.168.1.1", port=23, mac_address = "你的MAC地址")` ，替换上面得到的MAC字符串和默认终端地址（选填:host）；

- 4.运行脚本，搞定!! >_^

**注意：**  开始前请先自行安装 `Python` 运行环境，并且开启 `Telnet` 功能，然后将设备与光猫处在同一网段内。
 
<br/>

# 过程小发现 （个人探索，不对的话欢迎讨论）
> 1.在光猫-HG6543C5 reset后并且未完成注册时，可以通过网上流传的 `CMCCAdmin aDm8H%MdA`超级管理员进入后台，一旦OLT注册完成后就会自动重置密码，格式为 `CMCCAdmin+算法随机生成部分`；
> 2.光猫重置后需要注册才能正常使用，OLT密码一般就是光猫上面写着的宽带帐户密码（我的是），PPPOE拨号密码一般是手机后十位与这个密码不同，这应该是留着用户自己换猫时候用的吧。
> 3.改变使光猫桥接，用路由器PPPOE拨号时，可以关掉光猫的无线功能防止所谓的WIFI信号干扰，个人觉得最多算是同信道占用率高吧。不关闭光猫的DHCP服务，方便之后修改路由器为自动获取IP模式即可对光猫进行无线配置；切来切去的也不是很麻烦哈！当然你有线连接的话当我没说，嘿嘿！
<br/>

# 设计思路来源于

[Criogaid/CMModemPasswordRetrieval](https://github.com/Criogaid/CMModemPasswordRetrieval) && [B站 布束砥信](https://www.bilibili.com/read/cv21044770/)

# 许可证

![](https://camo.githubusercontent.com/a8cdaa01ff64ee6059cca8875037664c8f811e5954822ca6e0f112316d28d41a/687474703a2f2f6d6972726f72732e6372656174697665636f6d6d6f6e732e6f72672f70726573736b69742f627574746f6e732f38387833312f706e672f62792d6e632d73612e706e67)

> 本项目遵循互联网的开放、自由、共享的原则，采用CC BY-NC-SA 4.0 许可协议 进行授权。
> 如需转载或引用本项目，请务必遵守许可协议的条款。在您的文章或项目开头部分，必须注明原作者、标注原项目链接，并以同样的方式，即CC BY-NC-SA 4.0许可协议，分享您的作品。
> 任何不遵循 CC BY-NC-SA 4.0 许可协议进行分发的行为，将被视为侵权。
