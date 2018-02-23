# c

```c
//导出函数接口，dll中可以调用
    _declspec(dllexport) void go() //export method,call in load
    {
        int a = 2;
    }
```