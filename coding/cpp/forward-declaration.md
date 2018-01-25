# 前向声明 forward declaration

前向声明是一种，不完全类型声明，所以他并不能取代完全类型，对于编译器来说，在需要知其被声明对象大小和内容时，前向声明，己不可用。故其应用场景，仅限如下：

*   1，声明引用和指针
*   2，作函数(仅声明)，的返回类型或是参数类型。

下面给出了一个应用场景： 
A.h

```cpp
#ifndef __A__H__
#define __A__H__

#include <string>
class B;  // here is the forward declaration

class A {
public:
  B getBfromA();
  std::string who_are_you();

};
#endif
```

B.h

```cpp
#ifndef __B__H__
#define __B__H__

#include <string>

class A;  // Here is the forward declaration

class B {
public:
  A getAfromB();
  std::string who_are_you();
};

#endif
```

A.cpp

```cpp
#include "A.h"
#include "B.h"

B A::getBfromA() {
  return B();
}

std::string A::who_are_you() {
  return "I am A";
}
```

B.cpp

```cpp
#include "B.h"
#include "A.h"

A B::getAfromB() {
  return A();
}
std::string B::who_are_you() {
  return "I am B";
}
```

main.cpp

```cpp
#include "A.h"
#include "B.h"

#include <iostream>

int main() {
  A a;
  B b;

  A ab = b.getAfromB();
  B ba = a.getBfromA();

  std::cout << "ab is: " << ab.who_are_you() << endl;
  std::cout << "ba is: " << ba.who_are_you() << endl;

  return 0;
}
```
