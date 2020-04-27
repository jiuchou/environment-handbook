磁盘管理
0.磁盘分区

分区表
	MBR分区表：（MBR含义：主引导记录）
	所支持的最大卷：2T （1TB=1024GB)
	对分区的设置：最多4个主分区或3个主分区加一个扩展分区。

	GPT分区表:  (GPT含义：GUID 分区表）
	支持最大卷：18EB  （1EB=1024TB）
	每个磁盘最多支持128个分区

分区类型（FS-TYPE）
	primary：主分区，如果需要安装操作系统必须选择primary，可以引导
	logical：逻辑分区，不能安装操作系统，其他同primary
	extented：fdisk中的概念，必须进一步划分为逻辑分区（逻辑分区的编号从5开始计数），否则不能做文件系统
1.磁盘挂载
	1.1 常规磁盘挂载
	1.2 超大磁盘挂载
2.磁盘读写速度
	测试写
	time dd if=/dev/zero of=test bs=8k count=1000000
	测试读
	time dd if=test of=/dev/null bs=8k count=1000000
	测试读写
	time dd if=test of=test1 bs=8k count=1000000


2T以上的磁盘分区挂载

使用 fdisk 提示信息：
The size of this disk is 2 TiB (2199023255552 bytes). DOS partition table format can not be used on drives for volumes larger than 2199023255040 bytes for 512-byte sectors. Use GUID partition table format (GPT).

原因：
mbr格式最多只支持2T的硬盘，传统的fdisk方案无法进行分区，建议使用GPT格式解决。
一般情况下，硬盘厂商针对此问题都提供了程序，将多余的空间映射成另一个硬盘来避开MBR的问题。
linux下fdisk 工具不支持GPT，得使用另一个GNU发布的强大分区工具parted。

