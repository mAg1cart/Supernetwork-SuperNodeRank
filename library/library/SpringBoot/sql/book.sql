/*
 Navicat MySQL Data Transfer

 Source Server         : xihua
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : localhost:3307
 Source Schema         : prac

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 22/06/2024 11:24:21
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

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

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES (9, '20211880115', '十万个为什么', 15.00, '苏格与', '温州大学出版社', '2022-12-05', '0', 19, 0);
INSERT INTO `book` VALUES (10, '20211880119', '五万个为什么', 20.00, '聂家辉', '温州大学出版社', '2022-12-01', '1', 24, 0);
INSERT INTO `book` VALUES (11, '20211880106', '一万个为什么', 16.00, '丁奕中', '温州大学出版社', '2022-12-02', '1', 14, 0);
INSERT INTO `book` VALUES (12, '20211880114', '计算机操作系统', 32.00, '凌浩晨', '温州大学出版社', '2022-12-03', '0', 6, 0);
INSERT INTO `book` VALUES (13, '20211880118', '伊索寓言', 25.00, '沈益威', '温州大学出版社', '2022-12-04', '0', 13, 0);
INSERT INTO `book` VALUES (15, '20211880109', '格林童话', 20.00, '张超祥', '温州大学出版社', '2022-12-05', '1', 3, 0);
INSERT INTO `book` VALUES (16, '20211880100', '图书管理系统', 188.00, '聂家辉', '温州大学出版社', '2022-08-10', '1', 16, 0);
INSERT INTO `book` VALUES (17, '20211880128', '和另一个自己谈谈心', 12.00, '\r\n武志红', '中国友谊出版公司', '2021-01-01', '1', 12, 0);
INSERT INTO `book` VALUES (18, '20211880111', '全国计算机技术与软件专业技术资格(水平)考试. 系统分析师考试大纲', 12.00, '全国计算机技术与软件专业技术资格(水平)考试办公室', '清华大学出版社', '2004-05-22', '1', 2, 0);
INSERT INTO `book` VALUES (19, '20211880145', '简单减肥餐, 好吃不反弹', 20.00, '\r\n萨巴蒂娜', '中国轻工业出版社', '2022-07-07', '1', 1, 0);
INSERT INTO `book` VALUES (20, '20211880155', '其实她真的好喜欢你', 25.00, '\r\n莫妮打', '时代文艺出版社', '2022-02-02', '1', 0, 0);
INSERT INTO `book` VALUES (21, '20211880156', '导游业务. 第7版', 24.00, '\r\n全国导游人员资格考试教材编写组', '旅游教育出版社', '2022-08-22', '1', 0, 0);
INSERT INTO `book` VALUES (22, '20211880166', '法医秦明. 幸存者', 22.00, '\r\n法医秦明', '北京联合出版公司', '2022-02-22', '1', 0, 0);
INSERT INTO `book` VALUES (23, '20211880177', '中国书法史', 24.00, '\r\n徐建融', '浙江人民美术出版社', '2021-11-01', '1', 0, 0);
INSERT INTO `book` VALUES (24, '20211880199', '实用百草治百病', 22.00, '\r\n宋纬文', '福建科学技术出版社', '2021-09-22', '1', 0, 0);
INSERT INTO `book` VALUES (25, '20211880176', '烈火芳菲', 20.00, '赵方新', '北京十月文艺出版社', '2022-01-22', '1', 0, 0);
INSERT INTO `book` VALUES (28, '20211880188', '斗破苍穹', 30.00, '天蚕土豆', 'XX出版社', '2015-10-12', '1', 0, 0);

SET FOREIGN_KEY_CHECKS = 1;
