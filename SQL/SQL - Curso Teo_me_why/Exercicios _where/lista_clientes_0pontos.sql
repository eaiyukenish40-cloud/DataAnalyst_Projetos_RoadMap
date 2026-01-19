SELECT
idCliente
FROM clientes
WHERE qtdePontos = 0
GROUP BY idCliente;