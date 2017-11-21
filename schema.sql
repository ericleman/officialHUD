CREATE TABLE handsfiles (filename text not null, room text not null, modified text, primary key(filename, room));
CREATE TABLE settings (parameter text not null, display text, value text, primary key(parameter));

CREATE TABLE c_hands (hand_id text not null, room text not null, table_name text, stake text,
  hand_date text, players_at_start int, players_at_flop int, players_at_turn int, players_at_river int,
  pot real, rake real, winners text, card_flop_1 int, card_flop_2 int, card_flop_3 int, card_turn int, card_river int,
  note text, flag text, primary key(hand_id, room));

CREATE TABLE c_hands_players (hand_id text not null, room text not null, player text not null, card_1 int, card_2 int, position int, 
  pf_raise_count int, pf_limp boolean, pf_folp boolean, vpip boolean, primary key(hand_id, room, player));



INSERT INTO settings (parameter,display) values ("username_winamax","Winamax Username"),
        ("username_pokerstars","Pokerstars Username"),
        ("hands_winamax","Winamax Hands Folder"),
        ("hands_pokerstars","Pokerstars Hands Folder");

insert into handsfiles (filename, room, modified) values ('abc', 'Winamax', '2017-11-11 12:12:12.000'),
  ('xyz', 'Winamax', '2017-11-11 12:12:12.000'); 