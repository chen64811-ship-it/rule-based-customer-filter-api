from typing import List, Dict

OPERATORS = {
    ">=": lambda a, b: a >= b,
    "<=": lambda a, b: a <= b,
    ">": lambda a, b: a > b,
    "<": lambda a, b: a < b,
    "==": lambda a, b: a == b,
}

def evaluate_condition(customer: Dict, condition: Dict):
    field = condition["field"]
    op = condition["operator"]
    value = condition["value"]

    # 字段不存在
    if field not in customer:
        return False, f"{field} 字段不存在"

    actual = customer[field]

    # 操作符不存在
    if op not in OPERATORS:
        return False, f"不支持操作符 {op}"

    # 类型检查（加分点）
    if not isinstance(actual, type(value)):
        return False, f"{field} 类型不匹配"

    try:
        result = OPERATORS[op](actual, value)
    except Exception as e:
        return False, f"计算错误: {str(e)}"

    if not result:
        return False, f"{field} 不满足 {op} {value}"

    return True, "通过"
def filter_customers_tool(customers: List[Dict], conditions: List[Dict]):

    # 空列表处理
    if not customers:
        return {"matched": [], "unmatched": []}

    if not conditions:
        return {"matched": customers, "unmatched": []}
    matched = []
    unmatched = []

    for customer in customers:
        failed = []

        for cond in conditions:
            ok, msg = evaluate_condition(customer, cond)
            if not ok:
                failed.append(msg)

        if not failed:
            matched.append(customer)
        else:
            unmatched.append({
                "customer": customer,
                "failed": failed
            })

    return {
        "matched": matched,
        "unmatched": unmatched
    }
def filter_customers(customers: List[Dict], conditions: List[Dict]):
    # 1️⃣ 空输入处理
    if not customers:
        return {"matched": [], "unmatched": []}

    if not conditions:
        return {"matched": customers, "unmatched": []}

    matched = []
    unmatched = []

    for customer in customers:
        reasons = []
        passed = True

        for condition in conditions:
            ok, reason = evaluate_condition(customer, condition)

            if not ok:
                passed = False
                reasons.append(reason)

        if passed:
            matched.append(customer)
        else:
            unmatched.append({
                "customer": customer,
                "reasons": reasons
            })

    return {
        "matched": matched,
        "unmatched": unmatched
    }