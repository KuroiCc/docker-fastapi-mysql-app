USE app
CREATE TABLE IF NOT EXISTS users
(
    id         int(12) primary key auto_increment,
    username   varchar(100) not null,
    password   varchar(100) not null,
    created_at datetime     not null default CURRENT_TIMESTAMP
) CHARACTER SET UTF8
  COLLATE utf8_general_ci;

CREATE TABLE IF NOT EXISTS articles
(
    id         int(12) primary key auto_increment,
    user_id    int(12)       not null,
    title      varchar(1000) not null,
    body       varchar(1000) not null,
    created_at datetime      not null default CURRENT_TIMESTAMP,
    image_path varchar(100)
) CHARACTER SET UTF8
  COLLATE utf8_general_ci;
