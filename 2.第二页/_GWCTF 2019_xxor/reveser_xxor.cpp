#include <stdio.h>  
#include <iostream>  
  
int main()  
{  
    unsigned int a[6] ={ 3746099070, 550153460, 3774025685, 1548802262, 2652626477, 2230518816 }; //将负号转化为无符号整形！
    unsigned int a2[4] = { 2,2,3,4};  
      
    unsigned int v3;  
    unsigned int v4;  
    int v5;  
      
    for (int i = 0; i < 6; i += 2)  
    {  
        v3 = a[i];  
        v4 = a[i+1];  
        v5 = 1166789954 * 64;  
          
        for (int j = 0; j < 64; ++ j )  
        {  
            v4 -= (v3 + v5 + 20) ^ ((v3 << 6) + a2[2]) ^ ((v3 >> 9) + a2[3]) ^ 16;  
            v3 -= (v4 + v5 + 11) ^ ((v4 << 6) + *a2) ^ ((v4 >> 9) + a2[1]) ^ 32;  
            v5 -= 1166789954;  
        }  
          
        a[i] = v3;  
        a[i+1] = v4;  
    }  
    for (int i = 0; i < 6; ++ i )  
    {  
        std::cout << *((char*)&a[i] + 2) << *((char*)&a[i] + 1) <<  *((char*)&a[i]);  
    }  
    return 0;  
}  
