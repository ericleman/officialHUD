CREATE TABLE handsfiles (filename text primary key, room text,modified text);
CREATE TABLE settings (parameter text primary key, display text, value text);
INSERT INTO settings (parameter,display) values ("username_winamax","Winamax Username"),
        ("username_pokerstars","Pokerstars Username"),
        ("hands_winamax","Pokerstars Hands Folder"),
        ("hands_pokerstars","Pokerstars Hands Folder");