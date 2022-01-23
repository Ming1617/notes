# redis

### 特点

内存型 单进程单线程 非关系型

Ubuntu

安装：`sudo apt-get install redis-server`

安装后，Ubuntu会将redis列为开机自动启动项

占用端口:  127.0.0.1:6379

服务端启动/停止/重启

`sudo /etc/init.d/redis-server status|start|stop|restart`

客户端连接

`redis-cli -h ip地址 -p 6379 -a 密码`

 

配置文件所在路径  **/etc/redis/redis.conf**

思考？：mysql的配置文件在哪里？

`/etc/mysql/mysql.conf.d/mysqld.cnf`

 

修改配置文件前 先备份一下

`sudo cp /etc/redis/redis.conf /etc/redis/redis_bak.conf`

更改用户组为redis

`sudo chown redis:redis /etc/redis/redis_bak.conf`

redis配置文件(配置完配置会重启，配置失败将无法重启)

重启redis失败 ， 大概率为配置文件配置有误导致

解决方案1：终端中 直接执行`redis-server /etc/redis/redis.conf`启动服务

若有报错，按照报错提示修改**redis.conf**

解决方案2：还原备份后的配置文件

​	`sudo mv/etc/redis/redis.conf /etc/redis/redis_error.conf`

​	`sudo mv /etc/redis/redis_bak.conf /etc/redis/redis.conf`

1、requirepass  密码   // 配置密码

2、重启服务

​	`sudo /etc/init.d/redis-server restart`

3、客户端连接

​	`redis-cli -h 127.0.0.1 -p 6379 -a 123456`

​	`127.0.0.1:6379>ping`

开放远程连接

1、注释掉本地IP地址绑定

69行：`#bind 127.0.0.1：：1`

2、关闭保护模式（把yes改为no）

88行：`protected-mode no`

3、重启服务

`sudo /etc/init.d/redis-server restart`

## 命令介绍

即无关于具体得数据类型

#### select number

说明：切换数据库（默认redis有16个数据库，0-15为具体数据库的编号，默认进入redis为db0）

#### info

说明：查看redis服务的整体情况

#### keys表达式

说明：查找所有符合给定模式的key（生产环境不要用）

样例：

​	KEYS*匹配数据库中所有key

​	KEYS h？llo匹配hello，hallo和hxllo等

#### type key

说明：返回当前键的数据类型

#### exists key

说明：返回：返回当前键是否存在

返回值：1代表当前key存在；0代表当前key不存在

#### del key

说明：删除key

#### rename key newkey

说明：重命名当前key的名字

#### flushdb

说明:清楚当前所在数据库数据

#### flushall

说明：清楚所有数据库数据



## 数据类型

#### **字符串**

1、字符串。数字，都会转为字符串来存储

2、以二进制的方式存储在内存中

**注意：**

**key命名规范**

​		可采用 - wang：email

**key命名原则**

​		1、key值不宜过长消耗内存，且在数据中查找这类键值的计算成本高

​		2、不宜过短，可读性较差

**值**

​		1、一个字符类型的值最多能存储521M内容

##### **常用命名-必须掌握**

**存数据**(字符串)

`set key value nx ex`

说明：设置一个字符串的key

特殊参数：

​		nx  --> notexist 代表当key不存在时，才存储这个key

​		ex  --> expire 过期时间，单位s

**取数据**

`get key`

说明：获取key的值

返回值：key的值 或者 "nil"

`strlen key`

说明：获取key存储值的长度

`getrange key start stop`

说明：获取知道范围切片内容【包含start stop】

`setrange key index value`

说明：从索引值开始，用value替换原内容；返回最新长度

`mset key1 value1 key2 value2 key3 value3`

说明：批量添加key和value

`mget key1 key2 key3`

说明：批量获取key的值

#### 数值操作

`incrby key` 步长 将key增加指定步长

`decrby key` 步长 将key减少指定步长

`incr key`：+1操作

`decr key`：-1操作

`incrbyfloat key step`  对浮点数进行操作

#### 应用场景

**缓存**

说明：将mysql中的数据存储到redis字符串类型中

**并发计数-点赞/秒杀**

说明：通过redis单进程单线程的特点，由redis负责计数，并发问题转为串行问题

**带有效期的验证码**

说明：借助过期时间，存放验证码；到期后，自动消亡

#### 练习

1、查看db0库中所有的键

`select 0` 

`keys*`

2、设置键trill：username对应值为user001，并查看

`set trill：username user001`

3、获取trill：username值长度

`strlen trill：username`

4、一次性设置trill：password、trill：gender、trill：fansnumber 并查看（值自定义）

`mset trill：password 123 trill：gebder M trill：fansnumber500`

5、查看键trill：score是否存在

`exists trill：score`

6、增加10个粉丝[fansnumber]

`incrby trill：fansnumber 10`

7、增加2个粉丝（一个一个加）

`incr trill：fansnumber`

8、有3个粉丝取消关注你了

`decrby trill：fansnumber 3`

9、又有1个粉丝取消关注你了

`decr trill：fansnumber`

10、思考、思考、思考...清楚当前库

`flushdb`

11、一万个思考之后，清楚所有库

`flushall`

#### 过期时间

默认情况下，key没有过期时间，需要手动指定

方案1：直接用set的ex参数

`set key value ex 3`

方案2：使用expire通用命令

​		1、`set key value`

​		2、`expire key 5 #秒`

​		3、`pexpire key 5 #毫秒`

#### 检查过期时间

查看过期时间 `ttl key - 通用命令`

返回值：

​		-1：代表当前key没有过期时间

​		>0：代表当前key的剩余存活时间

​		-2：代表当前key不存在

删除过期时间`persist key`

说明：把带有过期时间的key变为永久不过期

返回值：1代表删除过期时间成功/0代表当前key没过期时间 or key不存在

#### 删除机制

每个redis数据库中，都会有一个特殊的容器负责存储带有过期时间的key以及它对应的过期时间，这个容器称之为'过期字典'

**针对过期字典中的key，redis结合 惰性删除和定期删除两大机制，有效删除过期数据**

##### 惰性删除

当调用key时，检查是否过期，如果过期则删除

![image-20220121134330475](.\redis_img\image-20220121134330475.png)

##### 定期删除

主动定期扫描过期字典中的数据，检查是否过期

详见伪代码 - check_key.py

##### 最大内存检查

最后一道保险-maxmemory配置选项

一旦内存量超过最大限制（单位为字节），redis会在执行命令时触发 内存淘汰

（需手动在redis配置文件中激活maxmemory配置项）

**主要淘汰机制**（maxmemory参数）

**volatile-lru**:从已设置过期时间的内存数据集中挑选最近最少使用的数据 淘汰；

**volatile-ttl**：从已设置过期时间的内存数据集中挑选即将过期的数据淘汰

**volatile-random**：从已设置过期时间的内存数据集中任意挑选数据淘汰；

**allkeys-lru**：从内存数据集中挑选最近最少使用的数据淘汰；

**allkeys-random**：从数据集中任意挑选数据淘汰；

**no-enviction**：禁入大多写命令

#### 列表

##### 基础概念

1、元素是字符串类型

2、列表头尾增删快，中间增删慢，增删元素是常态

3、元素可重复

4、最多可包含2^32-1个元素

5、索引同python列表

##### 常用命令

###### 增加数据

1、`LPUSH key value1 value2`

说明：从列表头部压入元素

返回：list最新的长度

2、`RPUSH key value1 value2`

说明：从列表尾部压入元素

返回：list最新的长度

3、`RPOPLPUSH scr dst`

说明：从列表src尾部弹出1个元素，压入到列表dst的头部

返回：被弹出的元素

4、`LINSERT key after|before value newvalue`

说明：在列表指定元素后 / 前插入元素

返回：

​			1、如果命令执行成功，返回列表的长度

​			2、如果没有找到pivot，返回-1

​			3、如果key不存在或为空列表，返回0

###### **查看数据**

5、查看列表中元素

`LRANGE key start stop`

start：开始索引

stop：结束索引

6、获取列表长度

###### **删除数据**

`LLEN key`

7、从列表头部弹出1个元素

`LPOP key`

8、从列表尾部弹出1个元素

`RPOP key`

9、列表头部，阻塞弹出，列表为空时阻塞

`BLPOP key timeout`

10、列表尾部，阻塞弹出，列表为空时阻塞

`BRPOP key timeout`

关于BLPOP和BRPOP说明

​		1、如果弹出的列表不存在或者为空，就会阻塞

​		2、超时时间设置为0，就是永久阻塞，直到有数据可以弹出

​		3、如果多个客户端阻塞在同一个列表上，使用First In First Service原则，先到先服务。

11、`LREM key count value`

说明：删除指定元素

​		count>0:表示从头部开始向尾部搜索，移除与value相等的元素，数量为count

​		count<0：表示从尾部开始向表头搜索，移除与value相等的元素，数量为count

​		count=0：移除表中所有与value相等的值

返回：被移除元素的数量

12、 `LTRIM key start stop`

说明：保留指定范围内的元素

返回：ok

场景：

保存微博评论最后500条

`LTRIM weibo：comments 0 499`

###### 更新数据

13、`LSET key index newvalue`

说明：设置list指定索引的值

##### 应用场景

1、存储微博评论，做切割，只保留最新的xx个

2、生产者消费者模型，做中检层，存放生产者的任务

##### 练习

1、查看所有的键

`keys *`

2、向列表spider：urls中以RPUSH放入如下几个元素：01_baidu.com、02_taobao.com、03_sina.com、04_jd.com、05_xxx.com

`RPUSH spider:urls 01_baidu.com`

3、查看列表中所有元素

`LRANGE spide:urls 0 -1`

4、查看列表长度

`LLEN spider:urls`

5、将列表中01_baidu.com改为01_tmall.com

`LSET spider:urls 0 01_tmall.com`

6、在列表中04_jd.com之后再加1个元素02_taobao.com

`LINSERT spider：urls after 04_jd.com 02_taobao.com`

7、弹出列表中的最后一个元素

`PROP spider：urls`

8、删除列表中所有的02_taobao.com

`LREM spider：urls 0 02_taobao.com`

9、剔除列表中的其他元素，只剩前3条

`LTRIM spider:urls 0 2`

#### 哈希

##### 定义

1、由field和关联的value组成的键值对

2、field和value是字符串类型

3、一个hash中最多包含2^32-1个键值对

##### 优缺点

优点：

1、节约内存空间-特定条件下【1、字段小于512个，2、value不能超过64字节】

2、可按需获取字段的值

缺点（不适合hash情况）

1、使用过期键功能：键过期功能只能对键进行过期操作，而不能对散列的字段进行过期操作

2、存储消耗大于字符串结构

##### 常用命令

1、设置单个字段

`HSET key field value`

`HSETNX key field value`

2、设置多个字段

`HMSET key field value field value`

3.返回字段个数

`HLEN key`

4、判断字段是否存在（不存在返回0）

`HEXISTS key field`

5、返回字段值

`HGET key field`

6、返回多个字段值

`HMGET key field field`

7、返回所有的键值数

`HGETALL key`

8、返回所有字段名

`HKEYS key`

9、返回所有值

`HVALS key`

10、删除指定字段

`HDEL key field`

11、在字段对应值上进行整数增量运算

`HINCRBY key field increment`

`HINCRBYFLOAT key field increment`

##### python操作hash

1、更新一条数据的属性，没有则新建

`hset（name，key，value）`

2、读取这条数据的指定属性，返回字符串类型

`hget（name，key）`

3、批量更新数据（没有则新建）属性，参数为字典

`hmset（name，mapping）`

4、批量读取数据（没有则新建）属性

`hmget（name，keys）`

##### 应用场景

**1、用户维度数据统计**

原理:基于hash压缩特点，和字段可计数

用户维度统计

​		统计数包括:关注数、粉丝数、喜欢商品数、发帖数用户为key，不同维度为fie1d， value为统计数比如关注了5人
​				`HSET user : 10000 fans 5`

​				`HINCRBY user : 10000 fans 1`

**2、缓存-redis+mysql+hash组合使用**

原理：hashkey按需取出字段数据，也比较适合做缓存

示例：

​			用户想要查询个人信息

​			1、到redis缓存中查询个人信息

​			2、redis中查询不到，到mysql中查询，并缓存到redis

​			3、再次查询个人信息

##### 练习

新建django项目rmysite1,数据库rmysite,应用user,
1，模型类User,字段id[主键], username[用户名], desc[个人描述]2，个人信息页–显示指定用户的用户名和个人描述
建议url : /user/info/<id>显示内容字符串即可用户名: xxx;个人描述: xxx【优先走缓存，缓存过期时间自定义】
3，个人信息更新页
可在当前页进行个人描述修改
注意:个人信息页走缓存.用户更新个人信息后,缓存清空

##### 哈希碰撞

输入不同，但是座位号相同

python：用开放地址法处理-哈希碰撞（根据当前位置+偏移量重新计算hash值）

扩容：当已经使用的座位数超过总座位数的三分之二。4倍/2倍（>5w）

座位重排（rehash）：旧数据的位置要根据新数组的长度，重新计算。删除key时，py采用伪删除，方便查找时还原路径【保持探测链】

redis：哈希碰撞-单链表

扩容-used/len（数组）>5肯定扩 >1可能扩

第一个大于used*2的2的n次方 2 4 2 的3次方大于4 2的3次方rehash渐进式的rehash，准备两个座位表，新旧座位表。

#### 集合

##### 基础概念

1、无序、去重

2、元素是字符串类型

3、最多包含2^32-1个元素

类似于python中所学集合

##### 常用命令

1、增加一个或者多个元素，自动去重；返回值为成功插入到集合的元素个数

`SADD key member1 member2`

2、查看集合中所有元素

`SMEMBERS key`

3、删除一个或者多个元素，元素不存在自动忽略

`SREM key member1 member2`

4、元素是否存在

`SISMEMBER key member`

5、随机返回集合中指定个数的元素。默认为1个

`SRANDMEMBER key [count]`

6、弹出成员

`SPOP key [count]`

7、返回集合中元素的个数

`SCARD key`

8、把元素从源集合移动到目标集合

`SMOVE source destination member`

9、差集（number 1 1 2 3 number2 1 2 4结果为3）

`SDIFF key1 key2`

10、差集保存到另一个集合中

`SDIFFSTORE destination key1 key2`

11、交集

`SINTER key1 key2`

`SINTERSTORE destination key1 key2`

12、并集

`SUNION key1 key2`

`SUNIONSTORE destination key1 key2`

##### 应用场景

社交类平台，共同好友  -  交集

纯随机类抽奖

防止元素重复

黑/白名单

思考：如何做一位每位学生都是随机考题的考试系统

#### 有序集合

##### 基础概念

1、有序、去重

2、元素是字符串类型

3、每个元素都关联着一个浮点数分值（score），并安装分值从小到大的顺序排列集合中的元素（分值可以相同）

4、最多包含2^32-1元素

##### 常用命令

1、在有序集合中添加一个成员 返回值为 成功插入到集合中的元素个数

`zadd key score member`

2、查看指定区间元素（升序）

`zrange key start stop [withscores]`

3、查看指定区间元素（降序）

`zrevrange key start stop [withscores]`

4、查看指定元素的分值

`zscore key member`

5、返回指定区间元素

`zrangebyscore key  min max [withscores] [limit offset count]`

参数说明：

​		min/max：最小值/最大值区间，默认闭区间（大于等于或小于等于）；（min，可开启开区间即（大于或小于））

​		offset：跳过多少个元素

​		count：返回几个

limit选项跟mysql一样

6、删除成员

`zrem key member`

7、增加或者减少分值

`zincrby key increment member`

8、返回元素排名

`zrank key member`

9、返回元素逆序排名

`zrevrank key member`

10、删除指定区间内的元素（默认闭区间，可做开区间）

`zremrangebyscore key min max`

11、返回集合中元素个数

`zcard key`

12、返回指定范围中元素的个数（默认闭区间，可做开区间）

`zcount key min max`

13、并集

`zunionstore destination numkeys key [weights 权重值] [AGGREGATE SUM|MIN|MAX]`

​		#zunionstore salary3 2 salary salary2 weights 1 0.5 AGGREGATE MAX

​		#2代表集合数量，weights之后 权重1给salary，权重0.5给salary2集合，算完权重之后执行聚合AGGREGATE

14、交集

`zinterstore destination numkeys key [weights 权重值] [AGGREGATE SUM|MIN|MAX]`

参数同并集

##### 应用场景

各种排行榜

## pyredis

#### 基础概念

除用redis客户端进行redis操作外，也可以使用python直接操作redis

检查当前Ubuntu是否安装

​	`sudo pip3 freeze|grep -i 'redis'`

安装Python的redis模块

​	`sudo pip3 install redis`

#### 操作流程

1、建立连接对象

`import redis`

`#创建数据库链接对象`

`r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='17')`

2、链接对象.redis命令即可

​		例如：`r.set(key,value)`

​		说明：大部分命令跟redis终端中使用雷同

## 位图操作

### 定义

1、位图不是真正的数据类型，它是定义在字符串类型中

![image2](.\redis_img\image2.png)

2、一个字符串类型的值最多能存储512M字节的内容，位上限：2^32

#### 常用命令

##### SETBIT命令

说明：设置某位置上的二进制值

语法：SETBIT key offset value

参数：offset-偏移量 从0开始

​		   value-0或者1

示例：

`#默认扩展位以0填充`

`127.0.0.1:6379> SET mykey ab`

`OK`

`127.0.0.1:6379>GET mykey`

`"ab"`

`127.0.0.1:6379>SETBIT mykey 0 1`

`(integer) 0`

`127.0.0.1:6379>GET mykey`

`"\xelb"   #16进制返回`

##### GETBIT命令

说明：获取某一位上的值

语法：GETBIT key offset

示例

​		`127.0.0.1:6379>GETBIT mykey 3`

​		`（integer）0`

​		`127.0.0.1:6379>GETBIT mykey 0`

​		`（integer） 1`

##### BITCOUNT命令

说明：统计键所有对应的值中有多少个1

语法：BITCOUNT key start end

参数：start/end 代表的是字节索引

示例：

`127.0.0.1:6379>SET mykey1 ab`

`OK`

`127.0.0.1:6379>BITCOUNT mykey`

`（integer）6`

`127.0.0.1:6379>BITCOUNT mykey 0 0`

`(integer)  3`

##### 应用场景

​        假设现在我们希望记录自己网站上的用户的上线频率，比如说，计算用户A上线了多少天，用户B上线了多少天，诸如此类，以此作为数据，从而决定让哪些用户参加重要活动——这个模式可以使用SETBIT和BITCOUNT来实现。

​          比如说，每当用户在某一天上线的时候，我们就使用SETBIT，以用户名作为 key ，将那天所代表的网站的上线日作为offset参数，并将这个offset 上的为设置为1。

​          举个例子，如果今天是网站上线的第100天，而用户peter在今天阅览过网站，那么执行命令SETBIT peter 100 1;如果明天peter也继续阅览网站，那么执行命令SETBIT peter 101 1，以此类推。

​			当要计算 peter总共以来的上线次数时，就使用BITCOUNT命令:执行BITCOUNT peter ,得出的结果就是peter 上线的总天数。

##### 性能测试

​			网站运行10年，占用的空间也只是每个用户10*365比特位(bit)，也即是每个用户456字节。对于这种大小的数据来说, BITCOUNT的处理速度就像GET和INCR操作一样快。

##### python中使用位图

py中操纵位图跟终端中执行完全一样

1、生成链接对象r

2、调用r.setbit / getbit / bitcount

## 高级技巧

### 事务

#### 基础概念

场景：小明账户100元，小红账户50元

需求:小明转账50元给小红

数据库语句:<1,小明账户-50元><2,小红账户+50元>

问题:如果执行1句时，数据库进程死掉了...

事务是逻辑上对数据的的一组操作,这组操作要么一次全部成功，或者这组操作全部失败;是不可分割的一个工作单位

##### 事务四大特性(ACID)

原子性(Atomicity)

一致性(Consistency)

隔离性(lsolation)

持久性(Durability)

**1，原子性(Atomicity)**

事务中所有操作是不可再分割的原子单位。事务中所有操作要么全部执行成功，要么全部执行失败

**2，一致性(Consistency)**

是事务对数据完整性约束的遵循。这些约束可能包括主键约束、外键约束或是一些用户自定义约束。事务执行的前后都是合法的数据状态，不会违背任何的数据完整性

**3，隔离性(lsolation)**

事务与事务之间互不打扰

**4，持久性(Durability)**

一个事务一旦成功提交，它对数据库的改变必须是永久的，即便是数据库发生故障也应该不回对其产生任何影响。

##### redis的事务

redis是弱事务型的数据库，并不具备ACiD的全部特性

redis具备隔离性:事务中的所有命令会被序列化、按顺序执行，在执行的过程中不会被其他客户端发送来的命令打断

不保证原子性: redis中的一个事务中如果存在命令执行失败,那么其他命令依然会被执行，没有回滚机制

##### 事务命令

1、MULTI #开启事务    MySQL    begin命令

2、命令1#执行命令

3、命令二

4-1、EXEC #提交到数据库执行  mysql  commit

4-2、DISCARD #取消事务  mysql rollback

##### 事务样例

`#开启事务`
`127.0.0.1:6379>MULTI`

`OK`

`#命令1入队列`
`127.0.0.1:6379> INCR n1`

`QUEUED`

`#命令2入队列`

`127.0.0.1:6379> INCR n2`

`QUEUED`

`#提交到数据库执行`

`127.0.0.1:6379>EXEC`

`1)(integer) 1`

`2)(integer) 1`

##### 事务特殊情况-命令语法错误

命令入队失败，直接字段discard退出这个事务

这个在命令在执行调用之前会发生错误。例如，这个命令可能有语法错误（错误的参数数量，错误的命令名)

处理方案:语法错误则自动执行discard

##### 事务特殊情况-类型操作错误

命令语法没错，但类型操作有误，则事务执行调用之后失败,无法进行事务回滚

​			当我们执行了一个由于错误的value的key操作会出现该现象(例如对着String类型的value施行了List命令操作)

处理方案:发生在EXEC之后的是没有特殊方式去处理的:即使某些命令在事务中失败，其他命令都将会被执行。![事务1](.\redis_img\事务1.png)

#### pipeline流水线

批量执行redis命令，减少通信io

原理:效仿redis的事务，客户端将多个命令打包，一次通信发给redis,可明显降低redis服务的请求数

注意:

​			1，此为客户端技术

​			2，如果一组命令中，一个命令需要上一个命令的执行结果才可以执行，则无法使用该技术

![pipeline流水线](.\redis_img\pipeline流水线.png)

##### python操作redis事务

python操作事务，需要依赖流水线技术

![pipeline流水线](.\redis_img\pipeline流水线.png)

##### watch-乐观锁

事务过程中，可对指定key进行监听，命令提交时，若被监听key对应的值未被修改，事务方可提交成功，否则失败

解决资源竞争的一种方式![watch-乐观锁](.\redis_img\watch-乐观锁.png)

python操作watch

信用卡提升额度，每次提升额度时，当前余额都变成原来的两倍

​				见test_watch.py

## 数据持久化

### 基础概念

wath-将数据从掉电易失的内存放到永久存储的设备上

why-因为所有的数据都在内存上，所以必须持久化

redis提供两种持久化方案

​		**ROB**     默认开启

​		**AOF**

### 数据持久化-RDB

1、保存真实的数据

2、将服务器包含的所有数据库以二进制文件的形式保存到硬盘里面

3、默认文件名：/var/lib/redis/dump.rdb

文件名即目录可在配置文件中修改【/etc/redis/redis.conf】

​		263行:dir/var/lib/redis  #表示rdb文件存放路径

​		253行：dbfilename dump.rdb # 文件名

#### 触发rdb持久化 - redis终端

方式1 redis终端中使用SAVE 或者BGSAVE命令

**SAVE**

`127.0.0.1:6379>SAVE`

`OK`

#特点

1、执行SAVE命令过程中，redis服务器将被阻塞，无法处理客户端发送的命令请求，在SAVE命令执行完毕后，服务器才会重新开始处理客户端发送的命令

2、如果RDB文件已经存在，那么服务器将自动使用新的RDB文件代替旧的RDB文件

**BGSAVE**

`127.0.0.1:6379>BGSAVE`

`Background saving started`

#执行过程中

1、客户端 发送 BGSAVE 给服务器

2、服务端马上返回 `Background saving started` 给客户端

3、服务器 fork()子进程做这件事

4、服务器继续提供服务

5、子进程创建完RDB文件后再告知Redis服务器

**SAVE vs BGSAVE**

SAVE比BGSAVE快,因为需要创建子进程，消耗额外的内存

说明:可以通过查看日志文件来查看redis的持久化过程

logfile位置: `/var/log/redis/redis-server.log`
触发rdb持久化 - 设置配置文件

#redis配置文件默认

218行：`save 900 1`

219行：`save 300 10`

​		表示如果距离上一次创建RDB文件已经超过了300秒，并且服务器的所有数据库总共已经发生了不少于10次修改，那么自动执行VGSAVE

220行：`save 60 10000`

​		1、只要三个条件中的任何一个被满足时，服务器就会自动执行BGSAVE

​		2、每次创建RDB文件之后，服务器为实现自动持久化而设置的时间计数器和次数计数器就会被清零，并重新开始计数，所有多个保存条件的效果不会叠加

#### 触发rdb持久化 - redis关闭

redis在正常关闭时，也会执行保存rdb操作

注意：异常关闭，无法自动触发RDB操作

#### 特殊说明

1、创建RDB文件需要将服务器所有的数据库的数据都保存起来，这是一个非常消耗资源和时间的操作，所以服务器需要隔一段时间才创建一个新的RDB文件，也就是说，创建RDB文件不能执行的过于频繁，否则会严重影响服务器的性能

2、可能丢失数据

### 数据持久化 - AOF

#### 基础概念

1、存储的是命令，而不是真实数据

2、默认不开启

​		开启方式（修改配置文件）

​		1、 /etc/redis/redis.conf

​		672行：appendonly yes #把no改成yes

​		676行：appendfilename “appendonly.aof”

​		2、重启服务

​		sudo /etc/init.d/redis-server restart

#### 执行原理

1、每当有修改数据库的命令被执行时，

2、因为AOF文件里面存储了服务器执行过的所有数据库修改的命令，所以给定一个AOF文件.服务器只要重新执行一遍AOF文件里
面包含的所有命令，就可以达到还原数据库的目的

用户可以根据自己的需要对AOF持久化进行调整， 让Redis在遭遇意外停机时不丢失任何数据，或者只丢失一秒钟的数据，这比RDB持久化丢失的数据要少的多

#### 特殊说明

虽然服务器执行一个修改数据库的命令，就会把执行的命令写入到AOF文件，但这并不意味着AOF文件持久化不会丢失任何数据，在目前常见的操作系统中，执行系统调用write函数，将一些内容写入到某个文件里面时，为了提高效率，系统通常不会直接将内容写入硬盘里面，而是将内容放入一个内存缓存区(buffer)里面等到缓冲区被填满时才将存储在缓冲区里面的内容真正写入到硬盘里。

1、AOF持久化:当—条命令真正的被写入到硬盘里面时，这条命令才不会因为停机而意外丢失
2、AOF持久化在遭遇停机时丢失命令的数量，取决于命令被写入到硬盘的时间
3、越早将命令写入到硬盘，发生意外停机时丢失的数据就越少，反之亦然

#### 相关优化配置

#打开配置文件 ： /etc/redis/redis.conf 找到相关策略如下

1、701行:alwarys

​		服务器每写入一条命令，就将缓冲区里面的命令写入到硬盘里面，服务器就算意外停机，也不会丢失已经成功执行的命令数据

2、702行：everysec（#默认）

​		服务器每一秒将缓冲区里面的命令写入到硬盘里面，这种模式下，服务器即使遭遇意外停机，最多只丢失1秒的数据

3、703行：no

​		服务器不主动将命令写入硬盘由操作系统决定何时将缓冲区里面的命令写入到硬盘里面，丢失命令数量不确定

#### AOF重写

**思考：AOF文件中是否会产生很多的冗余命令？**
为了让AOF文件的大小控制在合理范围，避免胡乱增长，redis提供了AOF重写功能，通过这个功能，服务器可以产生一个新的AOF文件
		-- 新的AOF文件记录的数据库数据和原由的AOF文件记录的数据库数据完全一样
		-- 新的AOF文件会使用尽可能少的命令来记录数据库数据，因此新的AOF文件的提及通常会小很多
		--AOF重写期间，服务器不会被阻塞，可以正常处理客户端发送的命令请求

**AOF重写触发**

1、客户端向服务器发送BGREWRITEAOF命令
`127.0.0.1:6379> BGREWRITEAOF`
`Background append only file rewriting started`
2、修改配置文件让服务器自动执行BGREWRITEAOF命令
`auto-aof-rewrite-percentage 100`

`auto-aof-rewrite-min-size 64mb`
#解释
		1、只有当AOF文件的增量大于100%时才进行重写，也就是大一倍的时候才触发
				#第一次重写新增:64M

​				#第二次重写新增:128M

​				#第三次重写新增:256M（新增128M)

##### AOF VS RDB

##### ![AOF VS RDB](.\redis_img\AOF VS RDB.png)

用redis用来存储真正数据，每一条都不能丢失，都要用always,有的做缓存，有的保存真数据，我可以开多个redis服务，不同业务使用不同的持久化，新浪每个服务器上有4个redis服务，整个业务中有上千个redis服务，分不同的业务，每个持久化的级别都是不一样的。

既有dump.rdb，又有appendonly.aof，恢复时找谁?
			**先找appendonly.aof**

## 高可用方案

### 基础概念

高可用-是系统架构设计中必须考虑的因素之一，它通常是指，通过设计减少系统不能提供服务的时间

目标：消除基础架构中的单点故障

​		redis单进程单线程模式，如果redis进程挂掉，相关依赖的服务就难以正常服务

redis高可用方案 - 主从搭建+哨兵

### 主从复制

1、一个Redis服务可以有多个该服务的复制品，这个RediS服务双为master，其他复制品成为slaves

2、master会一直将自己的数据更新同步给slaves，保持主从同步

3、只有master可以执行写命令, slave只能执行读命令

作用:分担了读的压力(高并发);提高可用性

原理:从服务器执行客户端发送的读命令，客户端可以连接slaves执行读请求，来降低master的读压力

#### 实现方式 - Linux命令行

命令：redis-server - -slaveof  <master-ip> <master-port> - -masterauth <master password>![linux实现主从复制](.\redis_img\linux实现主从复制.png)

#### 实现方式 - redis命令行

两条命令

​      1、>slaveof IP PORT 成为谁的从

​	  2、>slaveof no one     '自封为王'

#### 实现方式 - 配置文件

![配置文件](.\redis_img\配置文件.png)

### 哨兵

#### 基础概念

1、sentinel会不断检查Master和Slaves是否正常

2、每一个Sentinel可以监控任意多个Master和该Master下的slaves

原理：正如其名，哨兵进程定期与redis主从进行通信当哨兵认为redis主‘阵亡’后【通信无返回】，自动将切换工作完成

#### 准备环境

![哨兵-准备环境](.\redis_img\哨兵-准备环境.png)

#### 安装哨兵&使用哨兵

![安装哨兵&使用哨兵](.\redis_img\安装哨兵&使用哨兵.png)

#### 配置文件解读

#sentinel监听端口，默认是26379，可以修改

`port 26379`

#告诉sentinel去监听地址为ip:port的一个master，这里的master-name可以自定义，quorum是一个数字，指明当有多少个sentinel认为一个master失效时，master才算真正失效

`sentinel monitor <master-name> <ip> <redis-port> <quorum>`

#如果master有密码，则需要添加该配置
`sentinel auth-pass <master-name> <password>`

#master多久失联才认为是不可用了，默认是30秒
`sentinel down-after-milliseconds <master-name>`

`<milliseconds>`

#### python 操作 redis哨兵

`from redis.sentinel import sentinel`

#生成哨兵连接

`sentinel = Sentine1([( ' localhost'，26379)]，socket_timeout=0.1)`

#初始化master连接

`master = sentinel.master_for( 'tedu', socket_timeout=0.1，db=1)`

`slave = sentinel.slave_for( 'tedu ' , socket_timeout=0.1，db=1)`

#使用redis相关命令

`master. set( ' mymaster', 'yes ' )`

`print(slave.get( ' mymaster ' ))`

