
解决方案

参考：https://www.cnblogs.com/mannyzhoug/archive/2013/08/27/3284572.html

对超过2TB的硬盘进行分区需要使用parted
root@HQ-V-YFBY:~# /sbin/parted /dev/sdc 
GNU Parted 3.2
Using /dev/sdc
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) mklabel gpt
(parted) help
  align-check TYPE N                        check partition N for TYPE(min|opt) alignment
  help [COMMAND]                           print general help, or help on COMMAND
  mklabel,mktable LABEL-TYPE               create a new disklabel (partition table)
  mkpart PART-TYPE [FS-TYPE] START END     make a partition
  name NUMBER NAME                         name partition NUMBER as NAME
  print [devices|free|list,all|NUMBER]     display the partition table, available devices, free space, all found partitions, or a particular partition
  quit                                     exit program
  rescue START END                         rescue a lost partition near START and END
  resizepart NUMBER END                    resize partition NUMBER
  rm NUMBER                                delete partition NUMBER
  select DEVICE                            choose the device to edit
  disk_set FLAG STATE                      change the FLAG on selected device
  disk_toggle [FLAG]                       toggle the state of FLAG on selected device
  set NUMBER FLAG STATE                    change the FLAG on partition NUMBER
  toggle [NUMBER [FLAG]]                   toggle the state of FLAG on partition NUMBER
  unit UNIT                                set the default unit to UNIT
  version                                  display the version number and copyright information of GNU Parted
(parted) mkpart primary ext4 
Start? 1G
End? 512G
(parted) mkpart logical ext4
Start? 512G
End? 2T
# 查看空闲空间
Model: VMware Virtual disk (scsi)
Disk /dev/sdc: 4294967296s
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 

Number  Start        End          Size         File system  Name     Flags
        34s          1953791s     1953758s     Free Space
 1      1953792s     999999487s   998045696s   ext4         primary
 2      999999488s   4294965247s  3294965760s  ext4         logical
        4294965248s  4294967262s  2015s        Free Space


查看磁盘对应的 UUID
blkid
lsblk -f 可以查看硬盘UUID

partprobe: 通知系统分区表的变化
