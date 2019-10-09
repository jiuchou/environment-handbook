#-*- coding: utf-8 -*-

# =========================================================
# string operation code block
# =========================================================

# Python字符串不区分大小写替换
def ignore_character_replace(s, s1, s2):
    """string replace substring that ignore character
        import re
        s = 'Hello World, HELLO PYTHON'
        print re.sub(r'(?i)hello', 'My', s)
    """
    import re
    return re.sub("(?i)" + s1, s2, s)

def test_ignore_character_replace():
    s = 'Hello World, HELLO PYTHON'
    s1 = 'hello'
    s2 = 'My'
    print ignore_character_replace(s, s1, s2)

test_ignore_character_replace()

