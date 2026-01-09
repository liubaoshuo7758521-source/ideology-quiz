#include <stdio.h>
#include <string.h>

int main() {
    int n;
    scanf("%d", &n);

    // 核心数据：记录每个哈希分组的【用户数】和【字典序最小的用户信息】
    int count[101] = {0};          // 每个哈希ID的用户数量
    char min_name[101][11] = {0};  // 每个哈希ID下字典序最小的用户名
    char min_gender[101][7] = {0}; // 对应性别
    int min_level[101] = {0};      // 对应等级

    for (int i = 0; i < n; i++) {
        char name[11], gender[7];
        int level;
        scanf("%s %s %d", name, gender, &level);

        // 1. 计算哈希ID
        int hash = 1;
        for (int j = 0; name[j] != '\0'; j++) {
            hash = (hash * (unsigned char)name[j]) % 101;
        }

        // 2. 更新当前哈希分组的信息
        count[hash]++; // 用户数+1
        // 若该分组无记录，或当前用户名更小，则更新最小用户信息
        if (count[hash] == 1 || strcmp(name, min_name[hash]) < 0) {
            strcpy(min_name[hash], name);
            strcpy(min_gender[hash], gender);
            min_level[hash] = level;
        }
    }

    // 3. 找目标分组：数量最多，哈希ID最小
    int max_count = 0, target_hash = 0;
    for (int i = 0; i < 101; i++) {
        if (count[i] > max_count) {
            max_count = count[i];
            target_hash = i;
        } else if (count[i] == max_count && i < target_hash) {
            target_hash = i;
        }
    }

    // 4. 输出结果
    printf("%s %s %d %d\n", min_name[target_hash], min_gender[target_hash], 
           min_level[target_hash], target_hash);

    return 0;
}