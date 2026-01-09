#include <stdio.h>

// 定义学生结构体（包含学号和数学成绩）
struct Student {
    int id;     // 学号（整型）
    float score;// 数学成绩（浮点型）
};

int main() {
    struct Student stu[3]; // 存储3个学生信息
    float sum = 0.0, avg;  // 总分、平均分
    int max_index = 0;     // 成绩最高的学生下标（初始为第一个）

    // 第一步：输入3个学生的信息
    for (int i = 0; i < 3; i++) {
        printf("%d", i+1);
        scanf("%d %f", &stu[i].id, &stu[i].score);
        sum += stu[i].score; // 累加总分
        // 更新成绩最高的学生下标
        if (stu[i].score > stu[max_index].score) {
            max_index = i;
        }
    }

    // 第二步：计算平均分
    avg = sum / 3.0;

    // 第三步：输出结果
    printf("%.2f\n", avg); // 保留2位小数
    printf("%d %.2f\n", stu[max_index].id, stu[max_index].score);

    return 0;
}