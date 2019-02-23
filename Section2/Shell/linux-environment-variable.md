# Linux 环境变量

Shell 的环境变量分为 set, env 两种，其中 ，set 变量可以通过 export 工具导入到 env 变量中。

set 是显示设置shell变量，仅在本 shell 中有效；env 是显示设置用户环境变量 ，仅在当前会话中有效。换句话说，set 变量里包含了 env 变量，但 set 变量不一定都是 env 变量。这两种变量不同之处在于变量的作用域不同。显然，env 变量的作用域要大些，它可以在 subshell 中使用。