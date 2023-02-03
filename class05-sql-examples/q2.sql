SELECT p1.name, p1.surname, p2.name, p2.surname, r.marriage_date
FROM mariage_records r
 INNER JOIN person p1 ON r.person1_id = p1.id
 INNER JOIN person p2 ON r.person2_id = p2.id;
