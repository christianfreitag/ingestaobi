-- init.sql
\c postgres
\c lojinha

CREATE SCHEMA Vendas;


CREATE TABLE Vendas.CompraProduto (
    id SERIAL,
    id_produto VARCHAR(20),
    produto VARCHAR(100),
    categoria VARCHAR(100),
    segmento VARCHAR(100),
    fabricante VARCHAR(50),
    loja VARCHAR(50),
    cidade VARCHAR(50),
    estado VARCHAR(50),
    vendedor VARCHAR(100),
    id_vendedor INTEGER,
    data_venda DATE,
    valor_venda DECIMAL(10,2)
);