-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

--Quantos cliente assinaram a lista de presença entre os dias 25/08/2025 e 30/08/2025?

SELECT
p.DescNomeProduto,
COUNT(DISTINCT t.IdCliente) QtdeClientes,
FROM transacoes t
LEFT JOIN transacao_produto tp ON tp.IdTransacao = t.IdTransacao
LEFT JOIN produtos p ON p.IdProduto = tp.IdProduto

WHERE p.DescNomeProduto = 'Lista de presença' 
AND substr(t.DtCriacao,1,10) >= '2025-08-25' AND substr(t.DtCriacao,1,10) < '2025-08-30'
