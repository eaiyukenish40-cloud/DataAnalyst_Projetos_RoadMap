-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

-- Qual clientes assinaram a lista de presença no dia 25/08/2025?

SELECT
    t.IdCliente,
    substr(t.DtCriacao,1,10) AS Datas
FROM transacoes t
LEFT JOIN transacao_produto tp ON tp.IdTransacao = t.IdTransacao
LEFT JOIN produtos p ON p.IdProduto = tp.IdProduto

WHERE p.DescNomeProduto LIKE 'Lista de presença' AND Datas = '2025-08-25'
GROUP BY IdCliente