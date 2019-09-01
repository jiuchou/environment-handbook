## 第一部分 工程参数

```
URL： 版本地址

REV： 版本号

module_unit： 依赖库信息

Proj_makecmd： 编译命令

PARAM： 环境变量，编译命令中使用

module_release： 生成库信息

module_source： 源代码归档信息
```

## 第二部分 模块编译系统流程说明

### 1 代码下载

> 前提
>
> - 版本地址 URL
> - 版本号 REV

下载代码到指定目录 `WORKSPACE/code_path`

```bash
svn checkout URL@REV code_path
```

### 2 前提条件

在 `WORKSPACE/code_path` 目录下创建指定的目录，目录层级如下

```
artifacts/
├── Debug
├── Logs
├── Modules
├── ProcessLogs
├── Release
├── ReleaseInfo
└── SC_Dist
```

### 3 下载依赖

> 前提
>
> ```json
> module_unit:[
>  {
>      // 依赖模块名
>      moduleName:"",
>      // 依赖模块vmp版本号，不使用
>      vmpVersion:"",
>      // 依赖库名
>      library:"",
>      // 依赖库编译生成地址，不使用
>      generatedfolder="路径",
>      // 依赖库存放地址（如果目录不存在，需创建）
>      targetfolder="",
>      // 依赖库的下载地址
>      downloadUrl:"",
>      // 流水号，不使用
>      pipelineHistoryId:""
>  },
>  {}
> ]
> ```

直接下载到指定目录 `targetfolder` 中，不使用原有策略（原有策略：下载到 `artifacts/Modules` 目录下再拷贝到 `targetfolder` 目录中）

- 静态库

- 代码库

  library的值是 `source.zip` 的时候，下载完成之后需要解压到targetfolder目录中，解压目录名为依赖模块名，源文件source.zip删除

### 4 编译

> 前提
>
> - Proj_makecmd： 通过工程参数传入
> - PARAM： 工程参数，作为 `Proj_makecmd` 中的环境变量

进入代码目录，执行编译命令 `Proj_makecmd`

### 5 归档

- 拷贝生成库到 `artifacts/Release` 目录，案例中最终文件为 `WORKSPACE/artifacts/Release/aaa/module_a_dir/module_a`

  ```json
  module_release: [
      {
          // 一定是文件，如果不是文件，报错
          "name": "module_a",
          // 目录名
          "generatedfolder": "aaa/module_a_dir"
      },
      {}
  ]
  ```

- 将 `artifacts` 目录移动为指定的目录 `WORKSPACE/artifacts`

- 源代码归档

  如果 `module_source` 的值为 `true`，则需要将编译完成的源代码压缩成source.zip，并归档到 `WORKSPACE/artifacts/Release` 目录下。

  > 前提
  >
  > module_source: true/false
