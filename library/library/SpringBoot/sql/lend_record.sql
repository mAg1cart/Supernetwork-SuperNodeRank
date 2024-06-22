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

 Date: 22/06/2024 11:24:14
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
) ENGINE = InnoDB AUTO_INCREMENT = 2030043149 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of lend_record
-- ----------------------------
INSERT INTO `lend_record` VALUES (-2048151551, 21, '20211880119', '五万个为什么', '2023-01-01 13:38:36', '2023-09-20 18:43:23', '1', 19, 0);
INSERT INTO `lend_record` VALUES (-1859469311, 21, '20211880114', '计算机操作系统', '2022-12-26 17:31:05', '2023-01-01 13:38:22', '1', 4, 0);
INSERT INTO `lend_record` VALUES (-1851039742, 21, '20211880100', '图书管理系统', '2022-12-23 19:30:59', '2022-12-23 19:32:00', '1', 13, 0);
INSERT INTO `lend_record` VALUES (-1691627519, 27, '20211880100', '图书管理系统', '2022-12-29 08:48:36', NULL, '0', 16, 0);
INSERT INTO `lend_record` VALUES (-1230368766, 21, '20211880115', '十万个为什么', '2022-12-24 15:10:31', '2022-12-24 15:17:51', '1', 13, 0);
INSERT INTO `lend_record` VALUES (-1171603454, 21, '20211880106', '一万个为什么', '2021-12-26 17:31:01', '2022-12-31 15:58:52', '1', 12, 0);
INSERT INTO `lend_record` VALUES (-1007984639, 21, '20211880115', '十万个为什么', '2022-12-23 19:34:28', '2022-12-23 19:34:33', '1', 12, 0);
INSERT INTO `lend_record` VALUES (-785686526, 21, '20211880115', '十万个为什么', '2022-12-23 19:31:28', '2022-12-23 19:32:05', '1', 11, 0);
INSERT INTO `lend_record` VALUES (-705966078, 28, '20211880115', '十万个为什么', '2022-12-29 09:22:08', '2023-10-12 18:23:44', '1', 18, 0);
INSERT INTO `lend_record` VALUES (-693452798, 21, '20211880100', '图书管理系统', '2022-12-26 17:31:07', '2022-12-27 13:16:54', '1', 15, 0);
INSERT INTO `lend_record` VALUES (-630497279, 21, '20211880109', '格林童话', '2022-12-23 19:31:31', '2022-12-23 19:32:10', '1', 2, 0);
INSERT INTO `lend_record` VALUES (-483696639, 21, '20211880118', '伊索寓言', '2022-12-23 19:31:29', '2022-12-23 19:32:11', '1', 9, 0);
INSERT INTO `lend_record` VALUES (-391421951, 21, '20211880128', '和另一个自己谈谈心', '2022-12-23 19:35:41', '2022-12-23 19:35:46', '1', 11, 0);
INSERT INTO `lend_record` VALUES (-177598462, 21, '20211880115', '十万个为什么', '2022-12-24 15:23:24', '2022-12-24 15:23:33', '1', 15, 0);
INSERT INTO `lend_record` VALUES (-18128895, 21, '20211880111', '全国计算机技术与软件专业技术资格(水平)考试. 系统分析师考试大纲', '2022-12-23 19:31:35', '2022-12-23 19:32:15', '1', 1, 0);
INSERT INTO `lend_record` VALUES (19632129, 21, '20211880106', '一万个为什么', '2022-12-31 16:05:24', '2023-01-01 13:38:29', '1', 13, 0);
INSERT INTO `lend_record` VALUES (262901761, 21, '20211880109', '格林童话', '2022-12-31 15:58:56', '2023-01-01 13:38:24', '1', 3, 0);
INSERT INTO `lend_record` VALUES (611016705, 21, '20211880119', '五万个为什么', '2022-12-23 19:31:28', '2022-12-23 19:31:57', '1', 18, 0);
INSERT INTO `lend_record` VALUES (749342722, 21, '20211880115', '十万个为什么', '2022-12-24 15:26:33', '2022-12-24 15:29:49', '1', 16, 0);
INSERT INTO `lend_record` VALUES (761970690, 21, '20211880118', '伊索寓言', '2022-12-26 17:31:02', '2023-01-01 13:38:28', '1', 12, 0);
INSERT INTO `lend_record` VALUES (1001086978, 21, '20211880118', '伊索寓言', '2022-12-23 19:33:59', '2022-12-23 19:34:02', '1', 10, 0);
INSERT INTO `lend_record` VALUES (1017778177, 21, '20211880115', '十万个为什么', '2022-12-24 15:19:35', '2022-12-24 15:19:50', '1', 14, 0);
INSERT INTO `lend_record` VALUES (1172967426, 21, '20211880100', '图书管理系统', '2022-12-24 15:28:35', '2022-12-24 15:30:12', '1', 14, 0);
INSERT INTO `lend_record` VALUES (1181442050, 21, '20211880106', '一万个为什么', '2022-12-23 19:31:29', '2022-12-23 19:32:06', '1', 11, 0);
INSERT INTO `lend_record` VALUES (1290493954, 21, '20211880118', '伊索寓言', '2022-12-23 19:35:39', '2022-12-23 19:35:44', '1', 11, 0);
INSERT INTO `lend_record` VALUES (1412087809, 21, '20211880128', '和另一个自己谈谈心', '2022-12-26 17:31:04', '2023-01-01 13:38:26', '1', 12, 0);
INSERT INTO `lend_record` VALUES (1428905986, 21, '20211880114', '计算机操作系统', '2022-12-23 19:31:30', '2022-12-23 19:32:08', '1', 3, 0);
INSERT INTO `lend_record` VALUES (1659592705, 21, '20211880119', '五万个为什么', '2022-12-23 19:30:59', '2022-12-23 19:31:18', '1', 17, 0);
INSERT INTO `lend_record` VALUES (1735090177, 21, '20211880118', '和另一个自己谈谈心', '2022-12-23 19:33:57', '2022-12-23 19:34:03', '1', 2, 0);
INSERT INTO `lend_record` VALUES (1756061697, 21, '20211880118', '和另一个自己谈谈心', '2022-12-23 19:31:33', '2022-12-23 19:32:13', '1', 1, 0);
INSERT INTO `lend_record` VALUES (2030043138, 21, '20211880119', '五万个为什么', '2023-09-20 18:43:26', '2023-09-20 18:43:31', '1', 20, 0);
INSERT INTO `lend_record` VALUES (2030043139, 21, '20211880119', '五万个为什么', '2023-09-20 18:43:33', '2023-09-20 18:43:46', '1', 21, 0);
INSERT INTO `lend_record` VALUES (2030043140, 21, '20211880119', '五万个为什么', '2023-09-20 18:43:48', '2023-09-20 18:50:27', '1', 22, 0);
INSERT INTO `lend_record` VALUES (2030043141, 21, '20211880111', '全国计算机技术与软件专业技术资格(水平)考试. 系统分析师考试大纲', '2023-09-20 18:51:02', '2023-09-20 18:51:18', '1', 2, 0);
INSERT INTO `lend_record` VALUES (2030043142, 21, '20211880119', '五万个为什么', '2023-09-20 18:52:30', NULL, '0', 23, 0);
INSERT INTO `lend_record` VALUES (2030043143, 21, '20211880106', '一万个为什么', '2023-10-12 18:05:55', NULL, '0', 14, 0);
INSERT INTO `lend_record` VALUES (2030043144, 31, '20211880114', '计算机操作系统', '2023-10-12 18:22:13', '2023-10-12 18:22:40', '1', 5, 0);
INSERT INTO `lend_record` VALUES (2030043145, 31, '20211880118', '伊索寓言', '2023-10-12 18:22:24', NULL, '0', 13, 0);
INSERT INTO `lend_record` VALUES (2030043146, 28, '20211880115', '十万个为什么', '2023-10-12 18:23:45', NULL, '0', 19, 0);
INSERT INTO `lend_record` VALUES (2030043147, 5, '20211880119', '五万个为什么', '2023-11-23 18:05:02', NULL, '0', 24, 0);
INSERT INTO `lend_record` VALUES (2030043148, 5, '20211880114', '计算机操作系统', '2023-11-23 18:05:04', NULL, '0', 6, 0);
INSERT INTO `lend_record` VALUES (2030043149, 33, '20211880100', '图书管理系统', '2024-06-22 11:04:25', NULL, '0', 17, 0);
INSERT INTO `lend_record` VALUES (2030043150, 33, '20211880100', '图书管理系统', '2024-06-22 11:04:26', NULL, '0', 17, 0);
INSERT INTO `lend_record` VALUES (2030043151, 33, '20211880145', '简单减肥餐, 好吃不反弹', '2024-06-22 11:04:42', NULL, '0', 2, 0);

SET FOREIGN_KEY_CHECKS = 1;
