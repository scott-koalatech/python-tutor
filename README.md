# python-tutor

以下是一些基础到中级的 **Python Tutor** 题目，可以用来探查编程水平。这些题目涵盖基础语法、数据结构、算法、以及代码逻辑的应用能力。

---

### **基础题目**
1. **计算平方和**
   - 输入一个整数 n，输出从 1 到 n 的所有整数的平方和。
   - 示例输入：`5`  
     输出：`1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55`

2. **列表的反转**
   - 输入一个列表，返回它的逆序列表。
   - 示例输入：`[1, 2, 3, 4, 5]`  
     输出：`[5, 4, 3, 2, 1]`

3. **寻找最大值**
   - 输入一个列表，返回其中的最大值。
   - 示例输入：`[4, 7, 1, 9, 3]`  
     输出：`9`

4. **斐波那契数列**
   - 输入一个整数 n，输出斐波那契数列的前 n 项。
   - 示例输入：`6`  
     输出：`[0, 1, 1, 2, 3, 5]`

---

### **进阶题目**
5. **统计单词频率**
   - 给定一段文本，统计每个单词出现的次数，并按降序输出。
   - 示例输入：`"the cat and the dog"`  
     输出：`{'the': 2, 'cat': 1, 'and': 1, 'dog': 1}`

6. **字符串回文检测**
   - 输入一个字符串，判断它是否是回文（正读和反读相同）。
   - 示例输入：`"racecar"`  
     输出：`True`

7. **计算平均值**
   - 输入一组学生的分数，返回最高分、最低分以及平均分。
   - 示例输入：`[85, 90, 78, 92, 88]`  
     输出：`最高分: 92, 最低分: 78, 平均分: 86.6`

8. **括号匹配检测**
   - 输入一个字符串，判断其中的括号是否成对出现且顺序正确。
   - 示例输入：`"(a + b) * (c + d)"`  
     输出：`True`

---

### **高级题目**
9. **二维列表转置**
   - 输入一个二维列表，输出其转置矩阵。
   - 示例输入：`[[1, 2], [3, 4], [5, 6]]`  
     输出：`[[1, 3, 5], [2, 4, 6]]`

10. **寻找素数**
    - 输入一个整数 n，返回小于 n 的所有素数。
    - 示例输入：`10`  
      输出：`[2, 3, 5, 7]`

11. **冒泡排序**
    - 实现一个简单的冒泡排序算法，对输入的列表进行排序。
    - 示例输入：`[3, 1, 4, 1, 5]`  
      输出：`[1, 1, 3, 4, 5]`

12. **学生成绩分类**
    - 根据成绩将学生分为以下类别：
      - >= 90: A
      - >= 80: B
      - >= 70: C
      - < 70: D
    - 示例输入：`[85, 92, 78, 65, 89]`  
      输出：`['B', 'A', 'C', 'D', 'B']`

---

### **综合题目**
13. **猜数字游戏**
    - 随机生成一个 1-100 的整数，用户输入数字，返回 "大了"、"小了" 或 "猜对了"。
    - 示例：
      ```
      随机数：42
      用户输入：50 -> 输出："大了"
      用户输入：30 -> 输出："小了"
      用户输入：42 -> 输出："猜对了"
      ```

14. **统计某字符出现次数**
    - 输入一个字符串和一个字符，返回该字符在字符串中出现的次数。
    - 示例输入：`"hello world", "o"`  
      输出：`2`

15. **二维列表中的最大值**
    - 输入一个二维列表，返回其中的最大值及其位置。
    - 示例输入：`[[3, 5, 1], [4, 8, 2], [7, 6, 9]]`  
      输出：`最大值: 9, 位置: (2, 2)`
