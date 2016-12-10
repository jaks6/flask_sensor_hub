drop table if exists 'values';
create table 'values' (
  id integer primary key autoincrement,
  name text not null,
  value real not null,
  'timestamp' text not null
);