-- Quantos produtos são RPG?

-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

SELECT COUNT(*) AS QtdProdutosRPG
FROM produtos
WHERE DescCategoriaProduto = 'rpg';