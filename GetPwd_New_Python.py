import re
import asyncio
import telnetlib3
import aiohttp
import logging
from typing import Optional, Tuple

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

class ATClient:
    # 常量定义
    TELNET_PROMPT = b"Config\\factorydir#"
    
    def __init__(
        self,
        host: str = "192.168.1.1",
        port: int = 23,
        # 你的 mac 字符串
        mac_address: str = "94D5053F7340"
        # mac_address: str = "xxxxxxxxxxxx"
    ):
        self.host = host
        self.port = port
        self.username = "admin"
        self.mac_address = mac_address
        self.password = f"Fh@{mac_address[-6:]}"
        self.session: Optional[aiohttp.ClientSession] = None

    async def _create_session(self):
        if not self.session or self.session.closed:
            self.session = aiohttp.ClientSession()

    """异步启用Telnet服务"""
    async def enable_telnet(self) -> bool:
        
        await self._create_session()
        url = f"http://{self.host}/cgi-bin/telnetenable.cgi?telnetenable=1&key={self.mac_address}"
        try:
            async with self.session.get(url) as response:
                text = await response.text()
                if "telnet开启" in text:
                    logging.info("Telnet enabled successfully")
                    return True
                logging.error("Failed to enable Telnet: %s", text)
                return False
        except Exception as e:
            logging.exception("Enable telnet failed: %s", str(e))
            return False
    
    """异步禁用Telnet服务"""
    async def disable_telnet(self) -> bool:
        await self._create_session()
        url = f"http://{self.host}/cgi-bin/telnetenable.cgi?telnetenable=0&key={self.mac_address}"
        try:
            async with self.session.get(url) as response:
                text = await response.text()
                if "telnet关闭" in text:
                    logging.info("Telnet disabled successfully")
                    return True
                logging.error("Failed to disable Telnet: %s", text)
                return False
        except Exception as e:
            logging.exception("Disable telnet failed: %s", str(e))
            return False
        finally:
            if self.session:
                await self.session.close()

    async def get_credentials(self) -> Optional[Tuple[str, str]]:
        try:
            reader, writer = await telnetlib3.open_connection(
                host=self.host,
                port=self.port
            )

            # 登录流程
            await reader.readuntil(b"(none) login:")
            writer.write(f"{self.username}\n")
            await reader.readuntil(b"Password: ")
            writer.write(f"{self.password}\n")
            
            # 验证登录
            try:
                await asyncio.wait_for(reader.readuntil(b"#"), timeout=3)
            except asyncio.TimeoutError:
                logging.error("Login authentication failed")
                return None

            # 进入工厂模式
            writer.write("load_cli factory\n")

            await reader.readuntil(self.TELNET_PROMPT)

            writer.write("show admin_name\n")
            admin_name_output = await reader.readuntil(b"\r\nCon")
            admin_name = re.search(rb'admin_name=(.*)', admin_name_output).group(1).decode().split()[0]
            writer.write("show admin_pwd\n")
            admin_pwd_output = await reader.readuntil(b"\r\nCon")
            admin_pwd = re.search(rb'admin_pwd=(.*)', admin_pwd_output).group(1).decode().split()[0]
            if admin_name and admin_pwd:
                print("\n")
                logging.info(f"====>> Admin Username: {admin_name}\n")
                logging.info(f"====>> Admin Password: {admin_pwd}\n")
                print("\n")
            return None
        except Exception as e:
            logging.exception("Get credentials failed: %s", str(e))
            return None
        finally:
            if writer:
                writer.close()
                await self.disable_telnet()

# 使用示例
async def main():
    client = ATClient()
    if await client.enable_telnet():
        await client.get_credentials()
        

if __name__ == "__main__":
    asyncio.run(main())