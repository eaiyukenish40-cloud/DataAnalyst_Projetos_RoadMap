-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

-- Em 2024 quantas transações do produto lovers tivemos?

-- Foi necessário entender quais tabelas possuem as informações necessárias para responder a pergunta. Elas estavam em 3 tabelas diferentes:
-- A tabela produtos possui a descrição do produto (DescNomeProduto)
-- A tabela transacao_produto relaciona os produtos com as transações (IdTransacao e IdProduto)
-- A tabela transacoes possui a data de criação da transação (DtCriacao)
-- Assim, uma vez que idenficamos as informações necessárias de cada tabela, foi possível montar a query com os 2 joins necessários para relacionar as tabelas e filtrar as informações de 2024.
SELECT
COUNT(t.IdTransacao) AS QtdeTransacoes2024,
p.DescCategoriaProduto

FROM produtos p
JOIN transacao_produto tp ON p.IdProduto = tp.IdProduto

JOIN transacoes t ON tp.IdTransacao = t.IdTransacao
WHERE t.DtCriacao >= '2024-01-01' AND t.DtCriacao < '2025-01-01' 
GROUP BY p.DescCategoriaProduto
