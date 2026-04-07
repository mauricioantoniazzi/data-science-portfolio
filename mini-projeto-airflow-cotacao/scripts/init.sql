-- Criar a tabela de staging para o mini projeto de cotações
CREATE TABLE IF NOT EXISTS staging_cotacoes (
    id SERIAL PRIMARY KEY,
    moeda VARCHAR(10) NOT NULL,
    valor DECIMAL(10, 4) NOT NULL,
    data_cotacao TIMESTAMP NOT NULL,
    processado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Opcional: Criar um índice para acelerar buscas por data
CREATE INDEX IF NOT EXISTS idx_data_cotacao ON staging_cotacoes(data_cotacao);