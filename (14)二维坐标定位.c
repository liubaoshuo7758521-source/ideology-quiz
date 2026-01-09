#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    // 统计x分组：x范围-100~100 → 偏移100映射到0~200的数组下标
    int x_count[201] = {0};  // 记录每个x对应的点数
    int y_sum[201] = {0};    // 记录每个x对应的y坐标总和
    // 统计y分组：同理y范围-100~100
    int y_count[201] = {0};  // 记录每个y对应的点数
    int x_sum[201] = {0};    // 记录每个y对应的x坐标总和

    // 读取点并统计
    for (int i = 0; i < n; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        // 处理x分组：x+100是偏移后的下标
        x_count[x + 100]++;
        y_sum[x + 100] += y;
        // 处理y分组：y+100是偏移后的下标
        y_count[y + 100]++;
        x_sum[y + 100] += x;
    }

    // 任务1：找x分组中点数最多（x最小）的组，计算y平均值
    int max_x_cnt = 0, target_x = -101;
    for (int i = 0; i <= 200; i++) {
        int current_x = i - 100;
        if (x_count[i] > max_x_cnt || (x_count[i] == max_x_cnt && current_x < target_x)) {
            max_x_cnt = x_count[i];
            target_x = current_x;
        }
    }
    double avg_y = (double)y_sum[target_x + 100] / max_x_cnt;

    // 任务2：找y分组中点数最多（y最小）的组，计算x平均值
    int max_y_cnt = 0, target_y = -101;
    for (int i = 0; i <= 200; i++) {
        int current_y = i - 100;
        if (y_count[i] > max_y_cnt || (y_count[i] == max_y_cnt && current_y < target_y)) {
            max_y_cnt = y_count[i];
            target_y = current_y;
        }
    }
    double avg_x = (double)x_sum[target_y + 100] / max_y_cnt;

    // 输出结果（保留2位小数）
    printf("%.2f\n%.2f\n", avg_y, avg_x);
    return 0;
}