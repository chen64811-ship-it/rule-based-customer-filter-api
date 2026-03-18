import sys
import os
import yaml
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

# 添加当前目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from matcher import filter_customers_tool

app = FastAPI()


# 请求体结构定义（升级🔥：只需要 customers）
class FilterRequest(BaseModel):
    customers: List[Dict]


@app.post("/filter")
def filter_api(request: FilterRequest):
    # 读取 YAML（核心升级🔥：系统内置规则）
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    with open(os.path.join(script_dir, "skill.yaml"), "r", encoding="utf-8") as f:
        skill = yaml.safe_load(f)
    
    conditions = skill.get("eligibility", {}).get("conditions", [])
    
    # 直接传入两个参数（修复调用方式）
    result = filter_customers_tool(request.customers, conditions)
    return result
