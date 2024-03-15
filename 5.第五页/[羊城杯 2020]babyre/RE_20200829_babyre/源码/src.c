#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <sys/mman.h>
#include <stdlib.h>
#include "aes.h"
#include <openssl/des.h>
// gcc -s aes.c aes.h src.c -o -lcrypto re
int judge(uint8_t *key);

// ads = 0x402219
// end = 0x4022F8
// while ads <= end:
// 	patch_byte(ads, get_byte(ads)^0x99)
// 	ads += 1
// print "OK"
uint8_t des_en[16] = {0x0a,0xf4,0xee,0xc8,0x42,0x8a,0x9b,0xdb,0xa2,0x26,0x6f,0xee,0xee,0xe0,0xd8,0xa2};
uint8_t enc[31] = {01,21,32,31,14,25,76,37,82,19,10,21,22,32,77,102,131,148,76,23,85,91,23,45,12,75,84,23,44,11,23};

uint8_t kk[32] = {0xbd,0xad,0xb4,0x84,0x10,0x63,0xb3,0xe1,0xc6,0x84,0x2d,0x6f,0xba,0x88,0x74,0xc4,0x90,0x32,0xea,0x2e,0xc6,0x28,0x65,0x70,0xc9,0x75,0x78,0xa0,0x0b,0x9f,0xa6};
// flag{924a9ab2163d390410d0a1f670}
uint8_t key[0x10];
uint8_t vdata[0x20] = {0x30,0xe4,0xd2,0xc3,0xef,0x75,0xed,0xa8,0xe1,0xa1,0x73,0x81,0xe2,0xe9,0xab,0xc8,0xbf,0xca,0x52,0xe8,0xed,0x6b,0xa2,0x39,0x86,0x21,0xd0,0xf6,0x50,0x3e,0xf3,0x5c};

uint8_t Prime_Constants_char[] = {
	31, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43, 43, 47, 53, 59, 61, 67, 85, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251};

uint8_t CRC32_table[] = {
	1, 2, 3, 4, 150, 48, 7, 11, 44, 97, 14, 238, 186, 81, 9, 153, 25, 65, 109, 71};

uint8_t Base64_table[] = {
	17, 66, 28, 68, 69, 70, 71, 99, 73, 74, 16, 76, 8, 0, 79, 80, 81, 82, 66, 84, 85, 86, 99, 88, 89, 90, 23, 98, 72, 56, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 43, 47};

// Constants are the integer part of the sines of integers (in radians) * 2^32.
const uint32_t k[64] = {
	0x176aa478, 0x28c7b756, 0xa42070db, 0xc1bdceee,
	0x357c0faf, 0x4787c62a, 0xa8304613, 0x1d469501,
	0x398098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
	0x1b901122, 0xfd987193, 0xa679438e, 0x49b40821,
	0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
	0xa62f105d, 0x02441453, 0xd8a1e681, 0xc7d3fbc8,
	0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
	0xa9e3e905, 0xfcefa1f8, 0x676f02d9, 0x8d2a4c8a,
	0xfffa3942, 0x1771f681, 0x6d9d6122, 0xfde5380c,
	0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
	0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
	0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
	0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
	0x651b59c3, 0x8f0ccc92, 0xffeee47d, 0x85845dd1,
	0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
	0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d3bb};

// r specifies the per-round shift amounts
const uint32_t r[] = {7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
					  5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
					  4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
					  6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21};

// leftrotate function definition
#define LEFTROTATE(x, c) (((x) << (c)) | ((x) >> (32 - (c))))

void to_bytes(uint32_t val, uint8_t *bytes)
{
	bytes[0] = (uint8_t)val;
	bytes[1] = (uint8_t)(val >> 8);
	bytes[2] = (uint8_t)(val >> 16);
	bytes[3] = (uint8_t)(val >> 24);
}

uint32_t to_int32(const uint8_t *bytes)
{
	return (uint32_t)bytes[0] | ((uint32_t)bytes[1] << 8) | ((uint32_t)bytes[2] << 16) | ((uint32_t)bytes[3] << 24);
}

void md5(const uint8_t *initial_msg, size_t initial_len, uint8_t *digest)
{

	// These vars will contain the hash
	uint32_t h0, h1, h2, h3;

	// Message (to prepare)
	uint8_t *msg = NULL;

	size_t new_len, offset;
	uint32_t w[16];
	uint32_t a, b, c, d, i, f, g, temp;

	// Initialize variables - simple count in nibbles:
	h0 = 0xe3198231;
	h1 = 0xbca35162;
	h2 = 0x18badcfe;
	h3 = 0x87134212;

	//Pre-processing:
	//append "1" bit to message
	//append "0" bits until message length in bits ≡ 448 (mod 512)
	//append length mod (2^64) to message

	for (new_len = initial_len + 1; new_len % (512 / 8) != 448 / 8; new_len++)
		;

	msg = (uint8_t *)malloc(new_len + 8);
	memcpy(msg, initial_msg, initial_len);
	msg[initial_len] = 0x80; // append the "1" bit; most significant bit is "first"
	for (offset = initial_len + 1; offset < new_len; offset++)
		msg[offset] = 0; // append "0" bits

	// append the len in bits at the end of the buffer.
	to_bytes(initial_len * 8, msg + new_len);
	// initial_len>>29 == initial_len*8>>32, but avoids overflow.
	to_bytes(initial_len >> 29, msg + new_len + 4);

	// Process the message in successive 512-bit chunks:
	//for each 512-bit chunk of message:
	for (offset = 0; offset < new_len; offset += (512 / 8))
	{

		// break chunk into sixteen 32-bit words w[j], 0 ≤ j ≤ 15
		for (i = 0; i < 16; i++)
			w[i] = to_int32(msg + offset + i * 4);

		// Initialize hash value for this chunk:
		a = h0;
		b = h1;
		c = h2;
		d = h3;

		// Main loop:
		for (i = 0; i < 64; i++)
		{

			if (i < 16)
			{
				f = (b & c) | ((~b) & d);
				g = i;
			}
			else if (i < 32)
			{
				f = (d & b) | ((~d) & c);
				g = (5 * i + 1) % 16;
			}
			else if (i < 48)
			{
				f = b ^ c ^ d;
				g = (3 * i + 5) % 16;
			}
			else
			{
				f = c ^ (b | (~d));
				g = (7 * i) % 16;
			}

			temp = d;
			d = c;
			c = b;
			b = b + LEFTROTATE((a + f + k[i] + w[g]), r[i]);
			a = temp;
		}

		// Add this chunk's hash to result so far:
		h0 += a;
		h1 += b;
		h2 += c;
		h3 += d;
	}

	// cleanup
	free(msg);

	//var char digest[16] := h0 append h1 append h2 append h3 //(Output is in little-endian)
	to_bytes(h0, digest);
	to_bytes(h1, digest + 4);
	to_bytes(h2, digest + 8);
	to_bytes(h3, digest + 12);
}

void generatekey(uint8_t *key)
{
	uint8_t digest[0x40];
	md5(Base64_table, 64, digest);
	md5(CRC32_table, 20, digest + 0x10);
	md5(Prime_Constants_char, 53, digest + 0x20);
	md5(k, 64 * 4, digest + 0x30);
	md5(digest, 0x40, key);
}

// int judge(uint8_t *ttt);

 
void rc4_init(unsigned char* s_box, unsigned char* key, unsigned int key_len)
{
    unsigned char Temp[256];
    int i;
    for (i = 0; i < 256; i++)
    {
        s_box[i] = (5*i+2)%256;//顺序填充S盒
        Temp[i] = key[(3*i+1)%key_len];//生成临时变量T
    }
    int j = 0;
    for (i = 0; i < 256; i++)//打乱S盒
    {
        j = (j + s_box[(7*i+1)%255] + Temp[(i*4+1)%255]) % 256;
        unsigned char tmp = s_box[i];
        s_box[i] = s_box[j];
        s_box[j] = tmp;
    }
}

void smc()
{
  generatekey(key);
  int (*p)(char *s);
  p = judge;
  // uint8_t k[4]= {0,0,0,0};
  // key = {0x9a,0xef,0x86,0x2e,0x07,0xcd,0xc3,0x08,0x31,0x83,0x52,0xf7,0xc6,0x7b,0x80,0x45};
  // k[0] = key[1];
  // k[1] = key[3];
  // k[2] = key[5];
  // k[3] = key[7];
  //k = {0xef,0x2e,0xcd,0x08}
  int key_len=16;
  int n = 0x23c; //n的绝对值表示v的长度，取正表示加密，取负表示解密 
  mprotect(0x000400000, 0x3000, PROT_READ | PROT_WRITE | PROT_EXEC);
  uint8_t *pt = (uint8_t *)p;
  unsigned char s_box[256];
  rc4_init(s_box, key, key_len);
  unsigned int i = 0, j = 0, t = 0;
  unsigned int Temp;
  for (Temp = 0; Temp < n; Temp++)
  {
	    i = (i + 1) % 256;
	    j = (j + s_box[i]) % 256;
	    unsigned char tmp = s_box[i];//s盒动态变化的原因就是不断进行了打乱
	    s_box[i] = s_box[j];
	    s_box[j] = tmp;
	    t = (s_box[i] + s_box[j]+7) % 256;
	    pt[Temp] ^= s_box[t];//明文中的一个字节和密钥流中的一个字节进行异或
	    // printf("0x%02x,", s_box[t]);
  }
}

int judge(uint8_t *key)
{
	//key = th1s1sth3n1c3k3y
	// flag=GWHT{th1s_gam3_1s_s0_c00l_and_d}
	uint8_t flag[60];
	scanf("%40s", flag);
	int len = strlen(flag);
	if (len != 32)
	{
		printf("Wrong!\n");
		exit(0);
	}
	struct AES_ctx ctx;
	AES_init_ctx(&ctx, key);
	AES_ECB_encrypt(&ctx, flag);
	AES_ECB_encrypt(&ctx, flag + 0x10);
	for(int i=0;i<32;i++)
		for(int j=0;j<i/4;j++)
		{
			flag[i] ^= flag[j];
		}
	// for(int i=0;i<32;i++)
	// {
	// 	printf("0x%02x,", flag[i]);
	// }
	// printf("-------------------------\n");

	int right = 1;
	
	for(int idx=1;idx<32;idx++)
	{
		uint8_t v15=0;
		v15=(((flag[idx-1]^0x13)*2+7)&0xff)^(flag[idx-1]%9+flag[idx]+2);
		enc[idx-1] = v15;
	}
	if(flag[31]==0xc4)
	{
		for (int i = 0; i < 31; i++)
	{
		if (enc[i] != kk[i])
		{
			right = 0;
		}
		// printf("0x%02x,", enc[i]);
	}
	}
	return right;
}
int main()
{
	smc();
	uint8_t input[60];
	scanf("%39s", input);
	int len = strlen(input);
	if (len != 16)
	{
		printf("Wrong!\n");
		exit(0);
	}

	// int (*p)(char *s);
	// p = judge;
	// mprotect(0x400000, 0xF000, PROT_READ | PROT_WRITE | PROT_EXEC);
	// uint8_t *pt = (uint8_t *)p;
	// // decrypt here
	// generatekey(key);
	// for (int i = 0; i < 224; i++)
	// {
	// 	uint8_t tmp = pt[i];
	// 	pt[i] = tmp ^ 0x99;
	// }
	
	
	//
	// key = {0x9a,0xef,0x86,0x2e,0x07,0xcd,0xc3,0x08,0x31,0x83,0x52,0xf7,0xc6,0x7b,0x80,0x45};
	// for (int i = 0; i < 16; ++i)
 //         printf("%02x", key[i]);
 //      printf("\n");
	
	  unsigned char *keystring = "this is my key";
      DES_cblock key;
      DES_key_schedule key_schedule;
 
      //生成一个 key
      DES_string_to_key(keystring, &key);
      if (DES_set_key_checked(&key, &key_schedule) != 0) {
          printf("convert to key_schedule failed.\n");
          return -1;
      }
 
      //需要加密的字符串
      
      // size_t len = (sizeof(input)+7)/8 * 8;  
      uint8_t output[60];
      //IV
      DES_cblock ivec;
 
      //IV设置为0x0000000000000000
      memset((char*)&ivec, 0, sizeof(ivec));
     
      //加密
      DES_ncbc_encrypt(input, output, sizeof(input), &key_schedule, &ivec, DES_ENCRYPT);
 
      //输出加密以后的内容
      // for (int i = 0; i < 16; ++i)
      //    printf("%02x", output[i]);
      // printf("\n");
 
 //      // memset((char*)&ivec, 0, sizeof(ivec));
 
 //      //解密
 //      // DES_ncbc_encrypt(output, input, len, &key_schedule, &ivec, 0);
      
 //      // printf("%s\n", input);
      for (int i = 0; i < 16; ++i)
         if(output[i]!=des_en[i])
         	puts("wrong!");

 //      // free(output);
 //      // return EXIT_SUCCESS;

	// // key = [
	// //	0xcb, 0x8d, 0x49, 0x35, 0x21, 0xb4, 0x7a, 0x4c, 
	// //  0xc1, 0xae, 0x7e, 0x62, 0x22, 0x92, 0x66, 0xce
	// //]
	if (judge(input))
	{
		printf("Correct!\n");
	}
	else
	{
		printf("Wrong!\n");
	}
	exit(0);
}
