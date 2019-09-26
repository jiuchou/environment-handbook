* Python字符串不区分大小写替换

```python
import re

s = 'Hello World, HELLO PYTHON'
print re.sub(r'(?i)hello', 'My', s)
```
