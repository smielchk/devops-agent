import os
from openai import OpenAI
from dotenv import load_dotenv
import subprocess
import yaml

# 加载环境变量
load_dotenv()

# 尝试加载 config.yaml (DevOps 智能体现：优先读取配置文件)
config = {}
if os.path.exists("config.yaml"):
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY") or config.get("api_key"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
)
model = os.getenv("OPENAI_MODEL", "gpt-4o")

def test_sync_logic():
    """简单的单元测试：验证环境加载"""
    assert client.api_key is not None
    print("✅ Config check passed.")

def get_git_diff():
    subprocess.run(["git", "add", "."], check=True)
    result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)
    return result.stdout

def generate_commit_message(diff_text):
    if not diff_text.strip(): return "docs: maintenance update"
    prompt = f"Analyze diff and generate semantic commit message:\n\n{diff_text}"
    try:
        response = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}])
        return response.choices[0].message.content.strip()
    except:
        return "chore: update project"

def sync():
    diff = get_git_diff()
    msg = generate_commit_message(diff)
    subprocess.run(["git", "commit", "-m", msg], check=True)
    subprocess.run(["git", "push", "origin", "master"], check=True)

if __name__ == "__main__":
    # 如果带了 --test 参数则运行测试
    import sys
    if "--test" in sys.argv:
        test_sync_logic()
    else:
        sync()
