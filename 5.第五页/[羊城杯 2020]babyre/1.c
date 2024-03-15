#include <openssl/des.h>
#include <stdio.h>
#include <string.h>
#define MAX_LINE 1024
#pragma warning(disable  : 4996)
int main1(void)
{
	//输入密钥
	//DES_cblock key ;
	//memcpy(key, ("88888888"), 8);
	const_DES_cblock key = "1234567";
	//随机密钥
	//DES_random_key(&key);

	DES_key_schedule schedule;			// 密钥
	//转换成schedule
	DES_set_key_checked(&key, &schedule);		//设置密钥

	const_DES_cblock input = "hehehe";  //对字符串进行加密
	DES_cblock output;

	printf("明文: %s\n", input);

	//加密
	// 参数：输入数据、输出数据、密钥、模式
	DES_ecb_encrypt(&input, &output, &schedule, DES_ENCRYPT);
	printf("Encrypted!\n");

	printf("密文: ");
	int i;
	for (i = 0; i < sizeof(input); i++)
		printf("%02x", output[i]);
	printf("\n");

	//解密
	// 参数：输入数据、输出数据、密钥、模式
	DES_ecb_encrypt(&output, &input, &schedule, DES_DECRYPT);
	printf("Decrypted!\n");
	printf("cleartext:%s\n", input);
	return 0;

	
}

// DES CBC模式加密，
// 参数：input一般是明文输入 output一般是密文输出
// 难点：len的确定
int cryper1(unsigned char input[], const char *key)
{
	//const char *keystring = "this is my key";
	//DES_cblock key;
	DES_key_schedule key_schedule;
	const_DES_cblock *keystring = (const_DES_cblock *)key;
	//生成一个 key
	//DES_string_to_key(keystring, &key);//根据该字符串，生成一组经过计算的Key,可跳过这步
	DES_set_key_unchecked(keystring, &key_schedule);
	//if (DES_set_key_checked(keystring, &key_schedule) != 0) {
	//	printf("convert to key_schedule failed.\n");
	//	return -1;
	//}

	//需要加密的字符串
	//unsigned char input[] = "this is a text being encrypted by openssl";
	// 最少给len开辟这么多空间 加入input为1 则给len 8个字节空间，凑够一个分组
	size_t len = (sizeof(input) + 7) / 8 * 8;		// size_t 近似于 int
	unsigned char *output = (unsigned char *)malloc(len + 1);
	//IV
	DES_cblock ivec;
	//将向量初始化为0
	//IV设置为0x0000000000000000
	memset((char*)&ivec, 0, sizeof(ivec));

	//加密
	//参数说明
	/*
	input： 输入数据；（8字节长度--好像不一定）
	output： 输出数据；（8字节长度）
	length： 数据长度；（这里数据长度不包含初始化向量长度）
	schedule：密钥；
	ivec： 初始化向量；（一般为8个字节0）
	enc：加密：DES_ENCRYPT ， 解密：DES_DECRYPT；*/
	DES_ncbc_encrypt(input, output, sizeof(input), &key_schedule, &ivec, DES_ENCRYPT);

	//输出加密以后的内容
	for (int i = 0; i < len; ++i)
		printf("%02x", output[i]);
	printf("\n");

	memset((char*)&ivec, 0, sizeof(ivec));
	//memset(ivec, 0, sizeof(ivec));    // 经过测试，这个也行

	//解密
	DES_ncbc_encrypt(output, input, len, &key_schedule, &ivec, DES_DECRYPT);

	printf("%s\n", input);

	free(output);
	return EXIT_SUCCESS;
}

// 自己编写的des_CBC模式编程模型
void cryper(unsigned char input[], const char* key)
{
	const_DES_cblock* keystring = (const_DES_cblock*)key;
	DES_key_schedule key_schedule;
	//初始化向量
	DES_cblock ivec;
	memset(ivec, 0, sizeof(ivec));
	size_t len = (sizeof(input) + 7) / 8 * 8;
	unsigned char* output = (unsigned char*)malloc(len+1);
	// 生成密钥
	DES_set_key_unchecked(keystring, &key_schedule);
	// 加密
	DES_cbc_encrypt(input, output, sizeof(input), &key_schedule, &ivec, DES_ENCRYPT);
	// 输出加密后的结果
	printf("密文：");
	for (int i = 0; i < len; ++i) {
		printf("%02x", output[i]);
	}
	printf("\n");
	//解密
	memset(ivec, 0, sizeof(ivec));
	DES_cbc_encrypt(output, input, len,&key_schedule, &ivec, DES_DECRYPT);
	printf("明文：");
	printf("%s", input);
}

int main(void)
{
	//对文件进行加密
	//char buf[1024];
	//FILE *fp = fopen("test.txt", "r");
	//int len;		//字符个数
	//fgets(buf, MAX_LINE, fp);
	//
	//len = strlen(buf);
	//buf[len - 1] = '\0';  /*去掉换行符*/
	//printf("%s %d \n", buf, len - 1);
	//char cryptext[1024] = { 0 };
	unsigned char input[] = "iamyourbaba";
	const char* key = "123456789";
	cryper(input,key);		//加密后的结果哦通过cryptext带回
	getchar();
	//fclose(fp);

}
