getopt_long()使用方法

https://blog.csdn.net/lyh66/article/details/50098739



#### C开源编译


warning: incompatible implicit declaration of built-in function ‘memset’ [enabled by default]

未包含对应的头文件



## 1 编译

### 1.1 libtools编译

**autoscan**
`warning: missing AC_CHECK_FUNCS([strtol]) wanted by`

- 解释
  - https://stackoverflow.com/questions/19069781/can-not-autoconf-for-cgminer-missing-ac-check-funcs/19488853#19488853
- 解决方案
  - https://www.cnblogs.com/simonid/p/6374306.html

- https://www.jianshu.com/p/245540099da4

### 1.2 指定链接时使用的版本库

* 参考：[如何指定链接时使用的库版本？](http://www.it1352.com/783773.html)

使用

```bash
gcc app.o -l:libmy.so.1 -o app
```

替代

```bash
gcc app.o -lmy -o app
```

## 2 代码块

### 2.1 字符串替换函数

来源：http://bbs.chinaunix.net/thread-611241-1-1.html

```C
#include <stdio.h>

#define MAX_MSG_LENGTH 512

// 替换字符串中特征字符串为指定字符串
int ReplaceStr(char *sSrc, char *sMatchStr, char *sReplaceStr)
{
    int  StringLen;
    char caNewString[MAX_MSG_LENGTH];

    char *FindPos = strstr(sSrc, sMatchStr);
    if( (!FindPos) || (!sMatchStr) )
        return -1;

    while( FindPos )
    {
        memset(caNewString, 0, sizeof(caNewString));
        StringLen = FindPos - sSrc;
        strncpy(caNewString, sSrc, StringLen);
        strcat(caNewString, sReplaceStr);
        strcat(caNewString, FindPos + strlen(sMatchStr));
        strcpy(sSrc, caNewString);

        FindPos = strstr(sSrc, sMatchStr);
    }

    return 0;
}
 
int main()
{
    char str[512] = "system#SPACE#213#SPACE#2#SPACE#3";
    ReplaceStr(str, "#SPACE#", " ");
    puts(str);

    return 0;
}
```

