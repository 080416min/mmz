text = "从百草园到三味书屋，鲁迅回忆童年的乐趣与读书的沉静。"
word_count = len(text)
with open("result.txt", "w") as f:
 f.write(f"字数：{word_count}\n文本内容：{text}")
print("生成完成")
html_content = f"""

<html>
<body>
<h1>文本分析结果</h1>
<p>字符数：{word_count}</p >
<p>原文：{text}</p >
</body>
</html>
"""
with open("index.html", "w", encoding="utf-8") as f:
 f.write(html_content)