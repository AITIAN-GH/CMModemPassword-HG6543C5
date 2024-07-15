import requests
import re
import time
import telnetlib
from loguru import logger

class ModemManager:
    def __init__(self, host="192.168.1.1", port=23, mac_address = "你的MAC地址"):
        self.host = host
        self.port = port
        self.mac_address = mac_address

    def enable_telnet(self):
        url = f"http://{self.host}/cgi-bin/telnetenable.cgi?telnetenable=1&key={self.mac_address}"
        response = requests.get(url)
        if "telnet开启" in response.text:
            logger.info("Telnet has been successfully enabled.")
            return True
        else:
            logger.error("Failed to enable Telnet.")
            return False
    
    def disable_telnet(self):
        url = f"http://{self.host}/cgi-bin/telnetenable.cgi?telnetenable=0&key={self.mac_address}"
        response = requests.get(url)
        if "telnet关闭" in response.text:
            logger.info("Telnet has been successfully disabled.")
            return True
        else:
            logger.error("Failed to disable Telnet.")
            return False

    def get_admin_password(self):
        username = "admin"
        password = f"Fh@{self.mac_address[-6:]}"
        logger.info(f"Using Username: {username}")
        logger.info(f"Using Password: {password}")
        tn = telnetlib.Telnet(self.host, self.port)
        tn.read_until(b"(none) login:")
        tn.write(username.encode('ascii') + b"\n")
        tn.read_until(b"Password:")
        tn.write(password.encode('ascii') + b"\n")
        tn.read_until(b"#")
        tn.write(b"load_cli factory\n")
        tn.read_until(b"Config\\factorydir#")
        tn.write(b"show admin_name\n")
        tn.read_until(b"Success")
        result1 = ''
        while True:
            data = tn.read_very_eager()
            if not data:
                break
            result1 += data.decode('ascii')
            time.sleep(1)
        tn.write(b"show admin_pwd\n")
        tn.read_until(b"Success")
        result2 = ''
        while True:
            data = tn.read_very_eager()
            if not data:
                break
            result2 += data.decode('ascii')
            time.sleep(1)
        tn.close()
        admin_username = re.search(r'admin_name=(.*)', result1).group(1).strip()
        admin_password = re.search(r'admin_pwd=(.*)', result2).group(1).strip()
        logger.debug(f"Admin Username: {admin_username}")
        logger.debug(f"Admin Password: {admin_password}")

    def manage_modem(self):
        if self.enable_telnet():
            return self.get_admin_password()
        else:
            return False


if __name__ == "__main__":
    manager = ModemManager()
    manager.manage_modem()
    manager.disable_telnet()