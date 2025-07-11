🗂️ Tabela fnde_data_municipality
Estrutura que centraliza os dados‑chave de cada município utilizados nos sistemas do FNDE – essencial para relacionar programas, repasses, conselhos e escolas de forma padronizada.

| **Coluna**     | **Tipo / Restrições**                        | **Descrição funcional**                                                                                                                                                                           |


| **Campo**          | **Tipo / Restrições**                    | **Descrição** funcional                                                                                                                                                               | **Relacionamento Possível** |
| -------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `id`           | bigint, PK, auto\_increment, NOT NULL | Identificador técnico exclusivo (chave surrogate). Facilita integrações internas e evita dependência de códigos externos como IBGE.                                               | —                       |
| `name`         | varchar(255), NOT NULL                | Nome oficial do município, para relatórios e consultas amigáveis (ex.: “Salvador”, “Porto Alegre”).                                                                               | —                       |
| `ibge_code`    | varchar(20), NULL                     | Código IBGE do município, armazenado como texto para preservar zeros à esquerda e permitir versões estendidas (ex.: “2927408”). Base para cruzamentos estatísticos e geográficos. | —                       |
| `state`        | varchar(2), NULL                      | Sigla da Unidade da Federação (UF) do município (ex.: “BA”, “RS”).                                                                                                                | —                       |
| `siscacs_code` | varchar(20), NULL                     | Código do município no sistema **SISCACS**/SIGPC; utilizado para identificar entes em programas de controle social do FNDE.                                                       | —                       |
| `inuid`        | int unsigned, UNIQUE, NULL            | Identificador único da entidade no **SIMEC/SIGECON** (ex.: INUID\_ENTIDADE). Facilita a integração com APIs e bases federais do FNDE.                                             | —                       |


🔗 Possíveis relacionamentos

Esta tabela é o ponto central de referência para municípios e provavelmente está relacionada por chave estrangeira com diversas outras tabelas que usam o município como base, por exemplo:

| Tabela Referenciada            | Campo Local da FK            | Campo da Tabela `fnde_data_municipality`   |
| ------------------------------ | ---------------------------- | ------------------------------------------ |
| `fnde_data_mandatoconselho`    | `municipality_id`            | `id`                                       |
| `fnde_data_informacoesibge`    | `municipality_id`            | `id`                                       |
| `fnde_data_convenio`           | `municipioId`                | `ibge_code` (possivelmente comparado)      |
| `fnde_data_cnpjmunicipio`      | Pode usar `siscacs_code`     | `siscacs_code`                             |
| `fnde_data_fndeprogramas`      | `municipio_codigo`           | `ibge_code`                                |
| `fnde_data_fndeprogramassigpc` | `municipio_id` (varchar(10)) | Pode se relacionar via `ibge_code` ou `id` |


### Índices
- Index em (`id`, `name`, `ibge_code`, `state`,`siscacs_code`,`inuid`) conforme definido em `Meta.indexes`.






