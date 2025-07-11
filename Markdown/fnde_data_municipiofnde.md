Tabela: fnde_data_municipiofnde
Essa tabela armazena informações básicas sobre municípios que possuem dados relacionados ao FNDE (Fundo Nacional de Desenvolvimento da Educação). Ela pode ser usada como uma tabela de referência ou cadastro principal dos municípios participantes de programas educacionais federais, organizando dados como UF, nome, código IBGE e CNPJ da entidade municipal vinculada.

🔍 Descrição dos Campos


| **Campo**              | **Tipo**         | **Obrigatório / Restrição**       | **Descrição funcional**                                                                                                              | **Relacionamentos possíveis**                                                               |
| ------------------ | ------------ | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `id`               | bigint       | PK, NOT NULL, auto\_increment | Identificador único da linha; chave primária para relacionamentos e consultas.                                                     | —                                                                                       |
| `uf`               | varchar(2)   | NOT NULL                      | Sigla da Unidade Federativa (estado) do município (ex: "SP", "RJ", "BA").                                                          | —                                                                                       |
| `municipio_nome`   | varchar(150) | NOT NULL                      | Nome oficial do município (ex: "São Paulo", "Salvador").                                                                           | —                                                                                       |
| `municipio_codigo` | varchar(14)  | NOT NULL, UNIQUE              | Código do município (normalmente código IBGE, 7 dígitos, podendo ser estendido). Usado para relacionamentos padronizados.          | Relaciona-se logicamente com `ibge_code` da tabela `fnde_data_municipality`             |
| `cnpj`             | varchar(20)  | NOT NULL                      | CNPJ da entidade pública municipal responsável (ex: Prefeitura, Secretaria Municipal de Educação). Identificação jurídica oficial. | Pode se relacionar com o campo `cnpj` em outras tabelas, como `fnde_data_cnpjmunicipio` |

🔗 Possíveis Relacionamentos

| **Tabela Relacionada**                                                                         | **Campo FK na tabela atual**    | **Campo Referenciado**  | **Observações**                                                                         |
| ------------------------------------------------------------------------------------------ | --------------------------- | ------------------- | ------------------------------------------------------------------------------------ |
| `fnde_data_municipality`                                                                   | `municipio_codigo`          | `ibge_code`         | Relacionamento geográfico padrão pelo código IBGE.                                   |
| `fnde_data_cnpjmunicipio`                                                                  | `cnpj`                      | `cnpj`              | Relaciona o CNPJ da entidade municipal com a referência oficial da base FNDE.        |
| Outras tabelas FNDE que utilizem código IBGE do município ou CNPJ para cruzamento de dados | `municipio_codigo` e `cnpj` | `ibge_code`, `cnpj` | Usado para integrar dados de repasses, programas e monitoramento em nível municipal. |

## Resumo
Essa tabela é a principal referência para municípios com dados no FNDE, reunindo identificação geográfica (uf, municipio_nome, municipio_codigo) e identificação jurídica (cnpj) da entidade municipal.

O campo municipio_codigo é uma chave alternativa usada para relacionamentos com outras bases padronizadas.

O campo cnpj permite vínculo formal com a entidade municipal executora, possibilitando auditoria e cruzamentos legais.

Essencial para conectar dados de programas, repasses e monitoramento com o município correto e sua entidade pública responsável.

### Índices
- Index em (`id`,`uf`,`municipio_nome`,`municipio_codigo`,`cnpj`) conforme definido em `Meta.indexes`.