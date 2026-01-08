import dashscope
import os

# 若使用新加坡地域的模型，请取消下列注释
# dashscope.base_http_api_url = "https://dashscope-intl.aliyuncs.com/api/v1"

messages = [
    {
        "role": "user",
        "content": [
            {
                "audio": "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20240916/xvappi/%E8%A3%85%E4%BF%AE%E5%99%AA%E9%9F%B3.wav"}
        ]
    }
]

response = dashscope.MultiModalConversation.call(
    # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    model="qwen3-omni-30b-a3b-captioner",
    messages=messages,
    stream=True,
    incremental_output=True
)

full_content = ""
print("流式输出内容为：")
for response in response:
    if response["output"]["choices"][0]["message"].content:
        print(response["output"]["choices"][0]["message"].content[0]["text"])
        full_content += response["output"]["choices"][0]["message"].content[0]["text"]
print(f"完整内容为：{full_content}")