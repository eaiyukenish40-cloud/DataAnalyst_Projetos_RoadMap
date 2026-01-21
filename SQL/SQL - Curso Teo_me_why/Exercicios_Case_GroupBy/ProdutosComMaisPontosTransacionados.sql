--Qual o produto com mais pontos transacionados?
-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

SELECT
    idProduto,
    SUM(vlProduto*QtdeProduto) AS TotalPontosTrans
FROM transacao_produto 
GROUP BY idProduto
ORDER BY TotalPontosTrans DESC