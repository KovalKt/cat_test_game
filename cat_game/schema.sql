drop table if exists user;
create table user (
  id integer primary key autoincrement,
  username text not null,
  email text not null,
  password text not null,
  games_played integer default 0,
  authenticated boolean
);
