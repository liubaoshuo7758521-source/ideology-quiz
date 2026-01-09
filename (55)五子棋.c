#include <stdio.h>
#include <string.h>

#define SIZE 10

// 检查指定玩家是否获胜
int checkWin(char board[SIZE][SIZE], char player) {
    // 定义4个方向：右、下、右下、左下
    int dirs[4][2] = {{0, 1}, {1, 0}, {1, 1}, {1, -1}};
    
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] != player) continue;
            
            // 遍历4个方向
            for (int d = 0; d < 4; d++) {
                int count = 1;
                int x = i + dirs[d][0];
                int y = j + dirs[d][1];
                
                // 延伸统计连续相同棋子
                while (x >= 0 && x < SIZE && y >= 0 && y < SIZE && board[x][y] == player) {
                    count++;
                    x += dirs[d][0];
                    y += dirs[d][1];
                    if (count == 5) return 1; // 找到5连，返回获胜
                }
            }
        }
    }
    return 0; // 未获胜
}

int main() {
    char board[SIZE][SIZE];
    // 读取10x10棋盘
    for (int i = 0; i < SIZE; i++) {
        scanf("%s", board[i]);
    }
    
    if (checkWin(board, 'W')) {
        printf("W\n");
    } else if (checkWin(board, 'B')) {
        printf("B\n");
    } else {
        printf("N\n");
    }
    
    return 0;
}