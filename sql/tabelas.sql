CREATE TABLE demonstracoes_contabeis (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  REG_ANS INT,
  DATA_EXTRACAO DATE,
  DATA_PROCESSAMENTO DATE,
  DATA_COMPETENCIA DATE,
  CD_CONTA_CONTABIL VARCHAR(20),
  DESCRICAO VARCHAR(255),
  VL_CONTA FLOAT
);

CREATE TABLE operadoras_ativas (
  REG_ANS INT,
  CNPJ VARCHAR(14),
  RAZAO_SOCIAL VARCHAR(255),
  NOME_FANTASIA VARCHAR(255),
  MODALIDADE VARCHAR(255),
  TIPO_PRESTADOR VARCHAR(255),
  LOGRADOURO VARCHAR(255),
  NUMERO VARCHAR(20),
  COMPLEMENTO VARCHAR(255),
  BAIRRO VARCHAR(255),
  MUNICIPIO VARCHAR(255),
  UF VARCHAR(2),
  CEP VARCHAR(8),
  DDD VARCHAR(2),
  TELEFONE VARCHAR(20),
  FAX VARCHAR(20),
  ENDERECO_ELETRONICO VARCHAR(255),
  DATA_REGISTRO DATE
);