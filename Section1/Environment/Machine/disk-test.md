Linux io读写速度测试

测试写
time dd if=/dev/zero of=test bs=8k count=1000000

测试读
time dd if=test of=/dev/null bs=8k count=1000000

测试读写
time dd if=test of=test1 bs=8k count=1000000
