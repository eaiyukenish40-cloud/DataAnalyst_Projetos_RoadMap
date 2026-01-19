-- tabelas: clientes           produtos           transacao_produto  transacoes       

-- PRAGMA table_info('clientes');

-- listas_transacoes_1ponto
SELECT idTransacao,idCliente,DtCriacao 
FROM transacoes
WHERE QtdePontos = 1;

