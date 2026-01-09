#include <stdio.h>
#include <string.h>

// 成绩联合体：二选一存储分数/等级
typedef union {
    float score;   // 分数（浮点型）
    char grade;    // 等级（字符型：A/B/C等）
} ScoreUnion;

// 学生结构体：封装所有信息
typedef struct {
    int id;                // 学号
    char name[51];         // 名字（最多50字符，留1位存结束符）
    int score_type;        // 成绩类型：0=分数，1=等级
    ScoreUnion score_data; // 成绩数据（联合体）
} Student;

int main() {
    Student students[100]; // 最多存储100个学生
    int count = 0;         // 实际录入学生数

    // 循环读取输入，直到EOF
    while (1) {
        // 第一步：读取学号、姓名、成绩类型
        int read_ret = scanf("%d %s %d", 
                            &students[count].id, 
                            students[count].name, 
                            &students[count].score_type);
        if (read_ret != 3) break; // 读取失败（EOF）则退出

        // 第二步：根据成绩类型读取对应成绩
        if (students[count].score_type == 0) {
            // 读取分数（浮点型）
            scanf("%f", &students[count].score_data.score);
        } else if (students[count].score_type == 1) {
            // 读取等级（先清空缓冲区的换行/空格，再读字符）
            getchar(); // 跳过前面的空格/换行
            students[count].score_data.grade = getchar();
        }

        count++;
        if (count >= 100) break; // 达到100人上限则停止读取
    }

    // 遍历输出所有学生信息
    for (int i = 0; i < count; i++) {
        // 固定前缀输出
        printf("ID: %d, Name: %s, Score Type: %d, ",
               students[i].id, 
               students[i].name, 
               students[i].score_type);
        
        // 按类型输出成绩（分数/等级对应不同格式）
        if (students[i].score_type == 0) {
            printf("Score: %.1f\n", students[i].score_data.score);
        } else {
            printf("Grade: %c\n", students[i].score_data.grade);
        }
    }

    return 0;
}