#include <stdio.h>

struct Student {
    int id;
    char name[15];
    int grade;
    int cls;
    float score;
};

int main() {
    int n;
    scanf("%d", &n);
    struct Student stu[n];
    struct Student *p = stu;

    // 第一步：读入基础信息
    for (int i = 0; i < n; i++, p++) {
        scanf("%d %s %d %d", &(p->id), p->name, &(p->grade), &(p->cls));
    }

    // 第二步：更新成绩（使用同一个指针p，但每次重置）
    for (int i = 0; i < n; i++) {
        int target_id;
        float target_score;
        scanf("%d %f", &target_id, &target_score);
        
        // 每次搜索前重置p到数组开头
        p = stu;
        for (int j = 0; j < n; j++, p++) {
            if (p->id == target_id) {
                p->score = target_score;
                break;
            }
        }
        // 搜索结束后p指向找到的位置或数组末尾，但下次循环会重置
    }

    // 第三步：输出（需要重置p到开头）
    p = stu;
    for (int i = 0; i < n; i++, p++) {
        printf("%d %s %d %d %.1f\n", 
               p->id, p->name, p->grade, p->cls, p->score);
    }

    return 0;
}