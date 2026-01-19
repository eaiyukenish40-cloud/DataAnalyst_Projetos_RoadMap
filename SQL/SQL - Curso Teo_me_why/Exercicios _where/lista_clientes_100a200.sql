SELECT
idCliente, qtdePontos
FROM clientes
WHERE qtdePontos >= 100 AND qtdePontos <= 200
GROUP BY idCliente;