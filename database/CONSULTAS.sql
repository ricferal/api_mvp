-- SQLite


--DELETE  FROM produto
--WHERE pk_produto = 2

-- SQLite
INSERT INTO produto
 (nome, quantidade, valor)
VALUES ("PRODUTO1",12,13);

UPDATE produto SET data_insercao = datetime('now','localtime')
WHERE pk_produto = 1

SELECT datetime('now','localtime');