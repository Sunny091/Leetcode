# LeetCode Java 練習

## 目錄結構

```
java/
├── pom.xml                 # Maven 配置 (JUnit 5)
└── src/
    ├── main/java/com/leetcode/
    │   └── _題號_題目名稱/
    │       └── Solution.java       # 解題程式
    └── test/java/com/leetcode/
        └── _題號_題目名稱/
            └── SolutionTest.java   # 單元測試
```

## 環境需求

- Java 21
- Maven

## 使用方式

### 1. 建立新題目

手動建立以下檔案：

**解題程式** `src/main/java/com/leetcode/_題號_題目名稱/Solution.java`：
```java
package com.leetcode._題號_題目名稱;

public class Solution {
    public static ReturnType methodName(ParamType param) {
        // TODO: 實作解答
    }
}
```

**測試程式** `src/test/java/com/leetcode/_題號_題目名稱/SolutionTest.java`：
```java
package com.leetcode._題號_題目名稱;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    public void Test1() {
        // TODO: 加入測試案例
        assertEquals(expected, Solution.methodName(input));
    }
}
```

### 2. 執行測試

單一題目測試：
```bash
cd java
mvn test -Dtest="com.leetcode._題號_題目名稱.SolutionTest"
```

執行所有測試：
```bash
cd java
mvn test
```

### 3. 編譯專案

```bash
cd java
mvn compile
```
