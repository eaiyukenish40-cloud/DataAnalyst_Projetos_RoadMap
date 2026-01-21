-- Qual o produto mais transacionado
-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

SELECT
    IdProduto,
    COUNT(IdProduto) AS qtdeProduto
FROM transacao_produto
GROUP BY IdProduto
ORDER BY qtdeProduto DESC
