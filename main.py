import os
from openai import OpenAI
from dotenv import load_dotenv
import subprocess

# 加载环境变量
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
)
model = os.getenv("OPENAI_MODEL", "gpt-4o")

def get_git_diff():
    """获取本地代码差异"""
    try:
        # 确保已 add
        subprocess.run(["git", "add", "."], check=True)
        result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error getting diff: {e}"

def generate_commit_message(diff_text):
    """利用 OpenAI 生成语义化的提交信息"""
    if not diff_text.strip():
        return "Minor updates"
    
    prompt = f"Analyze the following git diff and generate a concise, professional commit message in English (following Conventional Commits, e.g., feat:, fix:, docs:):\n\n{diff_text}"
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip().replace('"', '')
    except Exception as e:
        print(f"AI Message Generation failed: {e}")
        return f"Update at {subprocess.check_output(['date']).decode().strip()}"

def sync_to_github():
    """执行同步流程"""
    print("🔍 Analyzing changes...")
    diff = get_git_diff()
    
    message = generate_commit_message(diff)
    print(f"📝 AI Generated Message: {message}")
    
    try:
        # 提交
        subprocess.run(["git", "commit", "-m", message], check=True)
        # 推送
        branch = subprocess.check_output(["git", "branch", "--show-current"]).decode().strip()
        print(f"🚀 Pushing to origin {branch}...")
        subprocess.run(["git", "push", "origin", branch], check=True)
        print("✅ Sync complete!")
    except subprocess.CalledProcessError as e:
        if "nothing to commit" in str(e) or e.returncode == 1:
            print("✨ Nothing to sync, working tree clean.")
        else:
            print(f"❌ Error during sync: {e}")

if __name__ == "__main__":
    sync_to_github()
