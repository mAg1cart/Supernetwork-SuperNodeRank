/*
 Navicat MySQL Data Transfer

 Source Server         : shop
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : localhost:3307
 Source Schema         : prac

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 24/06/2024 19:16:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for lend_record
-- ----------------------------
DROP TABLE IF EXISTS `lend_record`;
CREATE TABLE `lend_record`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `reader_id` bigint NOT NULL COMMENT '读者id',
  `isbn` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '图书编号',
  `bookname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '图书名',
  `lend_time` datetime(0) NULL DEFAULT NULL COMMENT '借书日期',
  `return_time` datetime(0) NULL DEFAULT NULL COMMENT '还书日期',
  `status` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '0：未归还 1：已归还',
  `borrownum` int NOT NULL COMMENT '此书被借阅次数',
  `delete_flag` smallint NULL DEFAULT 0 COMMENT '假删标志,0正常,1删除',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of lend_record
-- ----------------------------
INSERT INTO `lend_record` VALUES (1, 2, '2024002', '五万个为什么', '2024-01-01 13:38:36', '2024-03-01 13:38:36', '1', 1, 0);
INSERT INTO `lend_record` VALUES (2, 2, '2024004', '计算机操作系统', '2022-12-26 17:31:05', '2023-01-01 13:38:22', '1', 1, 0);
INSERT INTO `lend_record` VALUES (3, 2, '2024002', '五万个为什么', '2023-01-01 13:38:36', '2023-03-01 13:38:36', '1', 2, 0);
INSERT INTO `lend_record` VALUES (4, 2, '2024002', '五万个为什么', '2024-04-01 13:38:36', '2024-05-01 13:38:36', '1', 3, 0);
INSERT INTO `lend_record` VALUES (5, 5, '2024001', '十万个为什么', '2024-06-06 19:30:59', '2024-07-06 19:30:59', '1', 1, 0);
INSERT INTO `lend_record` VALUES (6, 5, '2024004', '计算机操作系统', '2024-05-06 19:25:59', '2024-06-06 19:25:59', '1', 1, 0);
INSERT INTO `lend_record` VALUES (7, 5, '2024001', '十万个为什么', '2024-06-06 19:30:59', '2024-07-06 19:30:59', '1', 2, 0);
INSERT INTO `lend_record` VALUES (8, 33, '2024003', '一万个为什么', '2024-06-06 18:05:55', NULL, '0', 1, 0);
INSERT INTO `lend_record` VALUES (9, 33, '2024010', '简单减肥餐, 好吃不反弹', '2024-06-22 11:04:42', NULL, '0', 1, 0);
INSERT INTO `lend_record` VALUES (10, 3, '2024002', '五万个为什么', '2024-06-20 18:52:30', NULL, '0', 4, 0);
INSERT INTO `lend_record` VALUES (11, 6, '2024005', '伊索寓言', '2024-06-04 18:22:24', NULL, '0', 1, 0);
INSERT INTO `lend_record` VALUES (12, 4, '2024007', '图书管理系统', '2024-06-01 08:48:36', NULL, '0', 1, 0);
INSERT INTO `lend_record` VALUES (13, 5, '2024004', '计算机操作系统', '2024-06-07 18:05:04', NULL, '0', 1, 0);


SET FOREIGN_KEY_CHECKS = 1;



-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `isbn` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '图书编号',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '名称',
  `price` decimal(10, 2) NULL DEFAULT NULL COMMENT '价格',
  `author` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '作者',
  `publisher` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '出版社',
  `create_time` date NULL DEFAULT NULL COMMENT '出版时间',
  `status` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '1' COMMENT '0：未归还 1：已归还',
  `borrownum` int NOT NULL DEFAULT 0 COMMENT '此书被借阅次数',
  `delete_flag` smallint NULL DEFAULT 0 COMMENT '假删标志,0:正常 1:被删除',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 29 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = DYNAMIC;

------设置触发器不能修改isbn------------
CREATE TRIGGER prevent_specific_isbn_update
BEFORE UPDATE ON book
FOR EACH ROW
BEGIN
    DECLARE error_message VARCHAR(255);
    
    -- 检查是否尝试更新特定的 ID
    IF OLD.isbn is not null THEN
        SET NEW.isbn=OLD.isbn;
			
    END IF;
END

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES (9, '2024001', '十万个为什么', 15.00, '苏格与', '温州大学出版社', '2022-12-05', '1', 2, 0);
INSERT INTO `book` VALUES (10, '2024002', '五万个为什么', 20.00, '聂家辉', '温州大学出版社', '2022-12-01', '1', 4, 0);
INSERT INTO `book` VALUES (11, '2024003', '一万个为什么', 16.00, '丁奕中', '温州大学出版社', '2022-12-02', '0', 2, 0);
INSERT INTO `book` VALUES (12, '2024004', '计算机操作系统', 32.00, '凌浩晨', '温州大学出版社', '2022-12-03', '0', 2, 0);
INSERT INTO `book` VALUES (13, '2024005', '伊索寓言', 25.00, '沈益威', '温州大学出版社', '2022-12-04', '0', 1, 0);
INSERT INTO `book` VALUES (15, '2024006', '格林童话', 20.00, '张超祥', '温州大学出版社', '2022-12-05', '0', 0, 0);
INSERT INTO `book` VALUES (16, '2024007', '图书管理系统', 188.00, '聂家辉', '温州大学出版社', '2022-08-10', '0', 1, 0);
INSERT INTO `book` VALUES (17, '2024008', '和另一个自己谈谈心', 12.00, '\r\n武志红', '中国友谊出版公司', '2021-01-01', '0', 0, 0);
INSERT INTO `book` VALUES (18, '2024009', '全国计算机技术与软件专业技术资格(水平)考试. 系统分析师考试大纲', 12.00, '全国计算机技术与软件专业技术资格(水平)考试办公室', '清华大学出版社', '2004-05-22', '1', 0, 0);
INSERT INTO `book` VALUES (19, '2024010', '简单减肥餐, 好吃不反弹', 20.00, '\r\n萨巴蒂娜', '中国轻工业出版社', '2022-07-07', '1', 1, 0);
INSERT INTO `book` VALUES (20, '2024011', '其实她真的好喜欢你', 25.00, '\r\n莫妮打', '时代文艺出版社', '2022-02-02', '1', 0, 0);
INSERT INTO `book` VALUES (21, '2024012', '导游业务. 第7版', 24.00, '\r\n全国导游人员资格考试教材编写组', '旅游教育出版社', '2022-08-22', '1', 0, 0);
INSERT INTO `book` VALUES (22, '2024013', '法医秦明. 幸存者', 22.00, '\r\n法医秦明', '北京联合出版公司', '2022-02-22', '1', 0, 0);
INSERT INTO `book` VALUES (23, '2024014', '中国书法史', 24.00, '\r\n徐建融', '浙江人民美术出版社', '2021-11-01', '1', 0, 0);
INSERT INTO `book` VALUES (24, '2024015', '实用百草治百病', 22.00, '\r\n宋纬文', '福建科学技术出版社', '2021-09-22', '1', 0, 0);
INSERT INTO `book` VALUES (25, '2024016', '烈火芳菲', 20.00, '赵方新', '北京十月文艺出版社', '2022-01-22', '1', 0, 0);
INSERT INTO `book` VALUES (28, '2024017', '斗破苍穹', 30.00, '天蚕土豆', 'XX出版社', '2015-10-12', '1', 0, 0);




-- ----------------------------
-- Table structure for bookwithuser
-- ----------------------------
DROP TABLE IF EXISTS `bookwithuser`;
CREATE TABLE `bookwithuser`  (
  `id` bigint NOT NULL COMMENT '读者id',
  `isbn` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '图书编号',
  `book_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '图书名',
  `nick_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '读者姓名',
  `lendtime` datetime(0) NULL DEFAULT NULL COMMENT '借阅时间',
  `deadtime` datetime(0) NULL DEFAULT NULL COMMENT '应归还时间',
  `prolong` smallint NULL DEFAULT NULL COMMENT '续借次数,0表示不能续借,1表示还可以续借',
  `delete_flag` smallint NULL DEFAULT 0 COMMENT '假删标志,0正常,1删除',
  PRIMARY KEY (`book_name`) USING BTREE,
  INDEX `id`(`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of bookwithuser
-- ----------------------------
INSERT INTO `bookwithuser` VALUES (33, '2024003', '一万个为什么', 'acer', '2024-06-06 18:05:55', '2024-07-06 18:05:55', 1, 0);
INSERT INTO `bookwithuser` VALUES (3, '2024002', '五万个为什么', 'huawei', '2024-06-20 18:52:30', '2024-07-20 18:52:30', 0, 0);
INSERT INTO `bookwithuser` VALUES (6, '2024005', '伊索寓言', 's4vior', '2024-06-04 18:22:24', '2024-07-04 18:22:24', 0, 0);
INSERT INTO `bookwithuser` VALUES (4, '2024007', '图书管理系统', 'xiaomi', '2024-06-01 08:48:36', '2024-07-01 08:48:36', 1, 0);
INSERT INTO `bookwithuser` VALUES (33, '2024010', '简单减肥餐, 好吃不反弹', 'acer', '2024-06-22 11:04:42', '2024-07-22 11:04:42', 1, 0);
INSERT INTO `bookwithuser` VALUES (5, '2024004    ', '计算机操作系统', 'realme', '2024-06-07 18:05:04', '2024-07-07 18:05:04', 1, 0);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '用户名',
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '密码',
  `salt` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `nick_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '姓名',
  `phone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '电话号码',
  `sex` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '性别',
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '地址',
  `role` int NOT NULL COMMENT '角色、1：管理员 2：普通用户',
  `alow` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '是否允许借阅',
  `delete_flag` smallint NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = '用户信息表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'admin', '9bc2a1e9747d67958ae5e642b9417cbf82f5adb4bffe0a5ee8bbd092110a8ec0', '691c53732d9b771d3ef149325bd1549e', 'hh', '1007', '女', '蚌埠', 1, '1', 0);
INSERT INTO `user` VALUES (2, 'iphone', '23b000344256b92af86ccf614d83877cfbc8e964d9bb2af14641060901e4a7b9', '3370dffc45c0151ab55e1cf7856e6ebd', '66', '1005', '男', '上海', 2, '1', 0);
INSERT INTO `user` VALUES (3, 'huawei', '744bc62245f45e7e1331597a1c39e57eef35ead7e5fc77639a78b8e54933129f', 'cd40044b23b2bd6817d0554f831d7847', '哈哈', '1019', '男', '北京', 2, '1', 0);
INSERT INTO `user` VALUES (4, 'realme', '13e66c8e7b2fec108da072000bd3b8e3ee5232f50128086fc16eea1f69a0fd08', '3279870ca6e92742b6ceb58c6e03ac80', '丁真', '1003', '男', '内江', 2, '1', 0);
INSERT INTO `user` VALUES (5, 'xiaomi', 'f29ea5fe6876652ebab324bf2b846bfeead1f043186a106c2f8b626af485eb96', '617c7c1df7e5010a62e6e256acd83863', 'yy', '1000', '女', '成都', 2, '1', 0);
INSERT INTO `user` VALUES (33, 'acer', 'b16b78e1ea93c68c24598119bee60a19c0945e19f650e96bb2eb644a592f2429', '7a2b5b160862449de38876409f0e3646', '321', '1002', '男', '理塘', 2, '1', 0);

SET FOREIGN_KEY_CHECKS = 1;