


-- CREATE DATABASE /*!32312 IF NOT EXISTS*/`yinliu` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `yinliu`;



DROP TABLE IF EXISTS `t_user`;

-- CREATE TABLE `t_user` (
--   `id` int(11) NOT NULL AUTO_INCREMENT,
--   `userName` varchar(20) DEFAULT NULL,
--   `password` varchar(20) DEFAULT NULL,
--   PRIMARY KEY (`id`)
-- ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


-- insert  into `t_user`(`id`,`userName`,`password`) values (1,'root','123456');



-- 创建表
CREATE TABLE t_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    add_user_permission TINYINT(1) NOT NULL DEFAULT 0,
    edit_user_permission TINYINT(1) NOT NULL DEFAULT 0,
    delete_user_permission TINYINT(1) NOT NULL DEFAULT 0,
    add_data_permission TINYINT(1) NOT NULL DEFAULT 0,
    edit_data_permission TINYINT(1) NOT NULL DEFAULT 0,
    delete_data_permission TINYINT(1) NOT NULL DEFAULT 0
);

-- 插入root用户
INSERT INTO t_user (username, password, add_user_permission, edit_user_permission, delete_user_permission, add_data_permission, edit_data_permission, delete_data_permission) 
VALUES ('root', '123456', 1, 1, 1, 1, 1, 1);

INSERT INTO t_user (username, password, add_user_permission, edit_user_permission, delete_user_permission, add_data_permission, edit_data_permission, delete_data_permission) 
VALUES ('wy', '111', 0, 0, 0, 0, 0, 0);