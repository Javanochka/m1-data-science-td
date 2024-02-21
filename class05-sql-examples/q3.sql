SELECT p1.name as name1, p1.surname as surname1, p2.name as name2, p2.surname as surname2, r.marriage_date as m_date
FROM mariage_records r
 INNER JOIN person p1 ON r.person1_id = p1.id
 INNER JOIN person p2 ON r.person2_id = p2.id;
