-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

SELECT 
    COUNT(idCliente) AS QtdClientesComEmail
FROM clientes
WHERE flEmail = 1;

