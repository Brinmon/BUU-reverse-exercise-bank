#include <iostream>

using namespace std;

char post[] = "20f0Th{2tsIS_icArE}e7__w"; // 后序遍历结果
char mid[] = "2f0t02T{hcsiI_SwA__r7Ee}"; // 中序遍历结果
void pre(int root, int start, int end)
{
    if (start > end)
        return;
    int i = start;
    while (i < end && mid[i] != post[root]) i++;  //定位根在中序的位置
    cout << mid[i];  //访问当前处理的树的根
    pre(root - 1 - (end - i), start, i - 1);  //递归处理左子树
    pre(root - 1, i + 1, end);  //递归处理右子树  
}

int main()
{
    pre(24, 0, 24);
    return 0;
}

// wctf2020{This_IS_A_7reE}
