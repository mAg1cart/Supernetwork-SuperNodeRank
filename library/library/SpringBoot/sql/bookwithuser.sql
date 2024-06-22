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

 Date: 22/06/2024 11:23:57
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

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
  `prolong` int NULL DEFAULT NULL COMMENT '续借次数',
  `delete_flag` smallint NULL DEFAULT 0 COMMENT '假删标志,0正常,1删除',
  PRIMARY KEY (`book_name`) USING BTREE,
  INDEX `id`(`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of bookwithuser
-- ----------------------------
INSERT INTO `bookwithuser` VALUES (21, '20211880106', '一万个为什么', 'xiaoxiong', '2023-10-12 18:05:55', '2023-12-11 18:05:55', 0, 0);
INSERT INTO `bookwithuser` VALUES (21, '20211880119', '五万个为什么', 'db', '2023-09-20 18:52:30', '2023-11-19 18:52:30', 0, 0);
INSERT INTO `bookwithuser` VALUES (31, '20211880118', '伊索寓言', 'xiaoxiaos', '2023-10-12 18:22:24', '2023-12-11 18:22:24', 0, 0);
INSERT INTO `bookwithuser` VALUES (27, '20211880100', '图书管理系统', '12', '2022-12-29 08:48:36', '2023-03-29 08:48:36', 0, 0);
INSERT INTO `bookwithuser` VALUES (33, '20211880145', '简单减肥餐, 好吃不反弹', 'acer', '2024-06-22 11:04:42', '2024-07-22 11:04:42', 1, 0);
INSERT INTO `bookwithuser` VALUES (5, '20211880114', '计算机操作系统', 'realme', '2023-11-23 18:05:04', '2023-12-23 18:05:04', 2, 0);

SET FOREIGN_KEY_CHECKS = 1;
