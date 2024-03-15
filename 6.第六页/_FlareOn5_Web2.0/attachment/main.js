// 创建一个单例实例变量 'instance'，初始值为 null
let instance = null;

// 创建一个空字符串变量 'wasm_stdout'，用于存储来自 WebAssembly 模块的输出
let wasm_stdout = "";

// 创建一个 WeakMap 变量 'memoryStates'，用于存储对象的内存状态
let memoryStates = new WeakMap();

// 它基于这个 Stack Overflow 回答提供的解决方案：https://stackoverflow.com/a/901144/87207
// @param {string} name - 要获取的查询参数的名称
// @param {string} url - 可选参数，要解析的 URL，默认为当前窗口的 URL
// @returns {string|null} - 查询参数的值，如果不存在则返回 null


function getParameterByName(name, url) {  //该函数从给定的 URL 中获取查询参数的值。
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

// 执行系统调用的函数。
// @param {Object} instance - WebAssembly 实例对象
// @param {number} n - 系统调用的编号
// @param {Array} args - 系统调用的参数数组
// @returns {number} - 系统调用的结果
function syscall(instance, n, args) {
    switch (n) {
    default:
        console.log("Syscall " + n + " NYI.");
        break;
    case /* brk */ 45: return 0;
    case /* writev */ 146:
        return instance.exports.writev_c(args[0], args[1], args[2]);
    case /* mmap2 */ 192:
        //debugger;
        const memory = instance.exports.memory;
        let memoryState = memoryStates.get(instance);
        const requested = args[1];
        if (!memoryState) {
            memoryState = {
                object: memory,
                currentPosition: memory.buffer.byteLength,
            };
            memoryStates.set(instance, memoryState);
        }
        let cur = memoryState.currentPosition;
        if (cur + requested > memory.buffer.byteLength) {
            const need = Math.ceil((cur + requested - memory.buffer.byteLength) / 65536);
            memory.grow(need);
        }
        memoryState.currentPosition += requested;
        return cur;
    }
}

/**
 * allocate a region of the given size within the given WebAssembly instance.
 * 在给定的WebAssembly实例中分配给定大小的区域。
 */
function wasm_alloc(instance, size) {
    return syscall(instance, /* mmap */ 192, [0, size]);
}

/**
 * write the given data at the given address within the WebAssembly instance.
 * 将给定数据写入WebAssembly实例中的给定地址。
 */
function wasm_write(instance, address, buf) {
    const membuf = new Uint8Array(instance.exports.memory.buffer, address);

    for (var i = 0; i < buf.byteLength; i++) {
        membuf[i] = buf[i];
    }
    return null;
}

/**
 * read the given number of bytes from the given address within the given WebAssembly instance.
 * 从给定WebAssembly实例中的给定地址读取给定字节数。
 */
function wasm_read(instance, address, size) {
    const membuf = new Uint8Array(instance.exports.memory.buffer);
    return membuf.slice(address, address + size);
}

fetch("test.wasm").then(response =>response.arrayBuffer()).then(bytes =>
  WebAssembly.instantiate(bytes, {
    env: {
      __eqtf2: function() {},  // FPU符号等于
      __multf3: function() {},  // FPU乘法
      __unordtf2: function() {},  // FPU无序
      __addtf3: function() {},  // FPU加法
      __eqtf2: function() {},  // FPU符号等于
      __multf3: function() {},  // FPU乘法
      __subtf3: function() {},  // FPU减法
      __netf2: function() {},  // FPU不等于
      __fixunstfsi: function() {},  // 将无符号整数转换为单精度浮点数
      __floatunsitf: function() {},  // 将无符号整数转换为双精度浮点数
      __fixtfsi: function() {},  // 将单精度浮点数转换为整数
      __floatsitf: function() {},  // 将双精度浮点数转换为整数
      __extenddftf2: function() {},  // 将单精度浮点数转换为双精度浮点数

      /* trampoline to our js syscall handler */
      __syscall0: function __syscall0(n) { return syscall(instance, n, []); },  // 系统调用0个参数
      __syscall1: function __syscall1(n, a) { return syscall(instance, n, [a]); },  // 系统调用1个参数
      __syscall2: function __syscall2(n, a, b) { return syscall(instance, n, [a, b]); },  // 系统调用2个参数
      __syscall3: function __syscall3(n, a, b, c) { return syscall(instance, n, [a, b, c]); },  // 系统调用3个参数
      __syscall4: function __syscall4(n, a, b, c, d) { return syscall(instance, n, [a, b, c, d]); },  // 系统调用4个参数
      __syscall5: function __syscall5(n, a, b, c, d, e) { return syscall(instance, n, [a, b, c, d, e]); },  // 系统调用5个参数
      __syscall6: function __syscall6(n, a, b, c, d, e, f) { return syscall(instance, n, [a, b, c, d, e, f]); },  // 系统调用6个参数
 
      putc_js: function (c) {
        // 将字符编码转换为字符串
        c = String.fromCharCode(c);
        // 检查字符是否为换行符
        if (c == "\n") {
          // 如果是换行符，则打印累积的输出并重置输出字符串
          console.log(wasm_stdout);
          wasm_stdout  = "";
        } else {
          // 如果不是换行符，则将字符追加到输出字符串中
          wasm_stdout += c;
        }
      }
    }
  })
).then(results => {
    instance = results.instance;// 获取 WebAssembly 实例

    let a = new Uint8Array([
        0xE4, 0x47, 0x30, 0x10, 0x61, 0x24, 0x52, 0x21, 0x86, 0x40, 0xAD, 0xC1, 0xA0, 0xB4, 0x50, 0x22, 0xD0, 0x75, 0x32, 0x48, 0x24, 0x86, 0xE3, 0x48, 0xA1, 0x85, 0x36, 0x6D, 0xCC, 0x33, 0x7B, 0x6E, 0x93, 0x7F, 0x73, 0x61, 0xA0, 0xF6, 0x86, 0xEA, 0x55, 0x48, 0x2A, 0xB3, 0xFF, 0x6F, 0x91, 0x90, 0xA1, 0x93, 0x70, 0x7A, 0x06, 0x2A, 0x6A, 0x66, 0x64, 0xCA, 0x94, 0x20, 0x4C, 0x10, 0x61, 0x53, 0x77, 0x72, 0x42, 0xE9, 0x8C, 0x30, 0x2D, 0xF3, 0x6F, 0x6F, 0xB1, 0x91, 0x65, 0x24, 0x0A, 0x14, 0x21, 0x42, 0xA3, 0xEF, 0x6F, 0x55, 0x97, 0xD6

        //0xB6, 0xFF, 0x65, 0xC3, 0xED, 0x7E, 0xA4, 0x00,
        //                     0x61, 0xD3, 0xFF, 0x72, 0x36, 0x02, 0x67, 0x91,
        //0xD2, 0xD5, 0xC8, 0xA7, 0xE0, 0x6E
    ]);

    let b = new Uint8Array(new TextEncoder().encode(getParameterByName("q")));// 编码输入参数为 Uint8Array

    let pa = wasm_alloc(instance, 0x200);// 为 a 分配内存空间
    wasm_write(instance, pa, a);// 将 a 写入内存空间

    let pb = wasm_alloc(instance, 0x200);// 为 b 分配内存空间
    wasm_write(instance, pb, b);// 将 b 写入内存空间
WebAssembly
    if (instance.exports.Match(pa, a.byteLength, pb, b.byteLength) == 1) {//执行WebAssembly，就是web的汇编
        // 如果匹配成功，则显示派对表情符号
        document.getElementById("container").innerText = "🎉";
    } else {
        // 如果匹配失败，则显示粪便表情符号
        document.getElementById("container").innerText = "💩";
    }
});
