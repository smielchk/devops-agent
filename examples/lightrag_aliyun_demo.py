import os
import asyncio
import numpy as np
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import openai_complete_if_cache, openai_embed
from lightrag.utils import setup_logger, wrap_embedding_func_with_attrs

setup_logger("lightrag", level="INFO")

WORKING_DIR = "./bailian_test_storage"
if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

# 配置阿里云百炼 (OpenAI 兼容模式)
API_KEY = os.getenv("ALIYUN_BAILIAN_API_KEY")
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

async def llm_model_func(
    prompt, system_prompt=None, history_messages=[], keyword_extraction=False, **kwargs
) -> str:
    return await openai_complete_if_cache(
        "qwen-plus",
        prompt,
        system_prompt=system_prompt,
        history_messages=history_messages,
        api_key=API_KEY,
        base_url=BASE_URL,
        **kwargs
    )

@wrap_embedding_func_with_attrs(embedding_dim=1536, max_token_size=2048, model_name="text-embedding-v2")
async def embedding_func(texts: list[str]) -> np.ndarray:
    return await openai_embed.func(
        texts,
        model="text-embedding-v2",
        api_key=API_KEY,
        base_url=BASE_URL
    )

async def main():
    rag = LightRAG(
        working_dir=WORKING_DIR,
        llm_model_func=llm_model_func,
        embedding_func=embedding_func
    )
    
    await rag.initialize_storages()

    print("\n--- 正在注入测试数据 ---")
    await rag.ainsert("杰青是一个基于 OpenClaw 的 DevOps 智能助手。他拥有 README 优先的思维，能够自动配置环境并管理 GitHub 仓库。")
    
    print("\n--- 执行混合查询 (Hybrid Query) ---")
    query_text = "杰青是谁？他有什么特点？"
    response = await rag.aquery(query_text, param=QueryParam(mode="hybrid"))
    print(f"\n查询结果:\n{response}")

if __name__ == "__main__":
    asyncio.run(main())
