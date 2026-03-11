import os
import sys
import json

def generate_mcp_config():
    # 获取当前 Python 解释器的绝对路径
    python_exe = sys.executable
    
    # 获取当前脚本所在目录的父目录（即项目根目录）
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    server_script = os.path.join(project_root, "lanhu_mcp_server.py")
    
    # 模拟配置块
    config = {
        "mcpServers": {
            "lanhu": {
                "command": python_exe,
                "args": [server_script, "--stdio"],
                "env": {
                    "LANHU_COOKIE": "您的蓝湖Cookie (详见项目 README)",
                    "MCP_USER_NAME": "您的名字",
                    "MCP_USER_ROLE": "您的角色 (如: 前端工程师)"
                }
            }
        }
    }
    
    print("\n" + "="*50)
    print("Lanhu MCP Quick Setup Assistant")
    print("="*50)
    print("\nPlease copy and paste the following content into your mcp_config.json file:\n")
    print(json.dumps(config["mcpServers"]["lanhu"], indent=2, ensure_ascii=False))
    print("\n" + "="*50)
    print("Note:")
    print("1. Ensure you have installed dependencies in current environment: pip install -r requirements.txt")
    print("2. Don't forget to fill in LANHU_COOKIE and other environment variables.")
    print("="*50 + "\n")

if __name__ == "__main__":
    generate_mcp_config()
