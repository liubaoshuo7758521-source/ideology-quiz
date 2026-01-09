#include <stdio.h>

// 定义学生结构体
struct Student {
    int id;
    char name[15];
    int grade;
    int cls;
};

int main() {
    // 1. 声明并初始化固定学生变量
    struct Student s1 = {1003, "Bob", 3, 10};
    
    // 2. 读取输入的学生信息
    struct Student s2;
    scanf("%d %s %d %d", &s2.id, s2.name, &s2.grade, &s2.cls);
    
    // 3. 比较年级，输出年级小的学生信息
    if (s1.grade < s2.grade) {
        printf("%d %s %d %d\n", s1.id, s1.name, s1.grade, s1.cls);
    } else {
        printf("%d %s %d %d\n", s2.id, s2.name, s2.grade, s2.cls);
    }
    
    return 0;
}
