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

 Date: 22/06/2024 12:21:01
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '用户名',
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '密码',
  `nick_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '姓名',
  `phone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '电话号码',
  `sex` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '性别',
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '地址',
  `role` int NOT NULL COMMENT '角色、1：管理员 2：普通用户',
  `alow` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '是否允许借阅',
  `delete_flag` smallint NULL DEFAULT 0 COMMENT '假删标志,0正常,1删除',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 35 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = '用户信息表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'admin', '123', '管理员', '12345678910', '男', '西华大学', 1, '1', 0);
INSERT INTO `user` VALUES (2, 'iphone', '123', '张三', '12', '男', '西华大学', 2, '1', 0);
INSERT INTO `user` VALUES (3, 'huawei', '123', '李四', '12345678912', '男', '西华大学', 2, '1', 0);
INSERT INTO `user` VALUES (4, 'xiaomi', '123', '王五', '12345678913', '男', '西华大学', 2, '1', 0);
INSERT INTO `user` VALUES (5, 'realme', '123', '周六', '12345678914', '男', '西华大学', 2, '1', 0);
INSERT INTO `user` VALUES (6, 's4vior', '123', '宏七', '12345678915', '男', '西华大学', 2, '1', 0);
INSERT INTO `user` VALUES (33, 'acer', '123', '牢八', '12345678916', '男', '西华大学', 2, '1', 0);

SET FOREIGN_KEY_CHECKS = 1;
