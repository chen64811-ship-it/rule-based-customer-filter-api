from matcher import filter_customers_tool

# 测试数据和你之前的用例一致
test_data = {
    "customers": [
        {"name": "张三", "business_years": 3, "monthly_revenue": 250000},
        {"name": "李四", "business_years": 1, "monthly_revenue": 180000}
    ]
}

# 执行筛选并打印结果
result = filter_customers_tool(test_data)
print("✅ 匹配的客户：")
for c in result["matched"]:
    print(c)
print("\n❌ 未匹配的客户：")
for c in result["unmatched"]:
    print(c)